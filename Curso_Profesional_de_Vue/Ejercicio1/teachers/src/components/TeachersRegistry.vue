<!-- Ejercicio 1 - Curso de Vue ADEMASS -->

<!-- Soy consciente de que está mal estructurado, pero por
practicidad realizo todo dentro de un solo compononte,
ya que así es la consigna del ejercicio. -->

<template>
<main>
    <div class="teacher-data-container">
        <div>
            <label for="name">Nombre </label>
            <input type="text" id="name" v-model="name" required>
        </div>
        <div>
            <label for="surname">Apellido </label>
            <input type="text" id="surname" v-model="surname" required>
        </div>
        <div>
            <label for="name">DNI o NIF </label>
            <input type="number" id="dni" v-model="dni" required>
        </div>
        <div>
            <input type="checkbox" id="checkin" v-model="checkin">
            <label for="checkin"> Documentación entregada</label>
        </div>
    </div>
    
    <div class="subjects-container">
        <div>
            <label for="subject">Materia </label>
            <input type="text" id="subject" v-model="subject">
            <br>
            <button class="add-subject-btn" v-on:click="addSubject()">Agregar Materia</button>
        </div>

        
        <div>
            <label for="subjects">Materias agregadas </label>
            <br>
            <select name="subjects" id="subjects" disabled size="5">
                <option v-for="(subj, index) in subjects" :key="index">{{ index + 1 }} | {{ subj }}</option>
            </select>
        </div>
    </div>
    
    <button class="add-teacher-btn" v-on:click="addTeacher()">Agregar Profesor</button>
    
    <div class="teachers-table">
        <caption><h3>Profesores activos</h3></caption>
        <table>
            <tr>
                <th></th>
                <th>Nombre</th>
                <th>Apellido</th>
                <th>DNI / NIF</th>
                <th>Materias</th>
                <th>Documentación<br>presentada</th>
            </tr>
            <tr v-for="(teacher, index) in teachers" v-bind:key="index">
                <td>{{ index + 1 }}</td>
                <td>{{ teacher.name }}</td>
                <td>{{ teacher.surname }}</td>
                <td>{{ teacher.dni }}</td>
                
                <td>
                    <select id="subjets-list">
                        <option v-for="(subj, index) in teacher.subjects" :key="index">{{ subj }}</option>
                    </select>
                </td>

                <td v-if="teacher.checkin">Sí</td>
                <td v-else>No</td>
            </tr>
        </table>
    </div>
</main>
</template>

<script setup>
    import { ref } from 'vue';

    // datos personales del profesor
    let name = ref()
    let surname = ref()
    let dni = ref()
    let subject = ref()
    let checkin = ref(false)

    // listado de materias por profesor
    let subjects = ref([])
    // colección (array) de profesores (object)
    let teachers = ref([])

    // añado una materia a la lista
    function addSubject() {
        subjects.value.push(subject.value)
        subject.value = ''
    }

    // añado un profesor a la lista de profesores
    const addTeacher = () => {
        teachers.value.push({
            name: name.value,
            surname: surname.value,
            dni: dni.value,
            subjects: subjects.value,
            checkin: checkin.value,
        })

        // una vez agregado un profesor, reseteo todos los valores
        name.value = ''
        surname.value = ''
        dni.value = ''
        checkin.value = false
        subjects.value = []
    }
</script>

<style scoped>
    caption {
        color: green;

    }
    main {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .teacher-data-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        width: 80vw;
        padding: 3vh 1vw;
        border: 1px solid green;
        border-radius: 10px 10px 0 0;
        color: #444;
        background-color: #DDD;
    }
    .subjects-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        /* align-items: start; */
        width: 80vw;
        padding: 2vh 1vw;
        border: 1px solid green;
        border-radius: 0 0 10px 10px;
        border-width: 0 1px 1px 1px;
        color: #444;
        background-color: #DDD;
    }
    .teachers-table {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .teachers-table table {
        border-collapse: collapse;
        width: 80vw;
    }
    .teachers-table th, td {
        text-align: center;
        padding: 10px;
        border: 1px solid green;
    }
    #subjects {
        width: 50vw;
        max-width: 300px;
    }
    .add-teacher-btn {
        color: green;
        background-color: lightgreen;
        width: 82vw;
        padding: 1rem 0;
        margin: 5vh;
        border: 0;
        border-radius: 10px;
        font-size: 2rem;
        font-weight: 300;
    }
    .add-teacher-btn:hover {
        color: lightgreen;
        background-color: green;
    }

    .add-subject-btn {
        padding: 10px;
        margin-top: 30px;
        margin-left: 65px;
    }
</style>