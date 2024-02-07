import pandas as pd
from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.service import Service


def extract_matches(driver, year):
    """Extrae los partidos "faltantes" de la Copa del Mundo en un año determinado.

    Args:
        driver (selenium webdriver): webdriver de selenium instanciado con el servicio
        year (str or int): año del mundial

    Returns:
        pandas.core.frame.dataframe: dataframe con los partidos (equipos y resultados)
    """

    URL = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'
    
    driver.get(URL)

    matches = driver.find_elements('xpath', '//tr[@style="font-size:90%"]')
    # matches = driver.find_elements('xpath', '//tr[@itemprop="name"]')

    home = []
    score = []
    away = []
    for match in matches:
        home.append(match.find_element('xpath', './td[1]').text.replace('\xa0', ''))
        score.append(match.find_element('xpath', './td[2]').text.replace(' (a.e.t.)', ''))
        away.append(match.find_element('xpath', './td[3]').text.replace('\xa0', ''))

    df = pd.DataFrame({
        'home': home,
        'score': score,
        'away': away
    })

    df['Year'] = year

    return df


# Main #
service = Service(executable_path='./driver/geckodriver')
driver = webdriver.Firefox(service=service)

df_list = []
for year in range(1930, 2019, 4):
    # en estos años no se jugaron mundiales
    if year == 1942 or year == 1946: continue

    df_list.append(extract_matches(driver, year))
    
    sleep(1)

driver.close()

df_fifa = pd.concat(df_list, ignore_index=True)
df_fifa.to_csv('fifa_worldcup_missing_data.csv', index=False)
