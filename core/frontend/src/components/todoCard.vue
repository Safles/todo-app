<script setup>
    import MaterialSymbolsEdit from '~icons/material-symbols/edit';
    import MaterialSymbolsDelete from '~icons/material-symbols/delete';
    import axios from 'axios'
    import moment from 'moment'
</script>

<template>
    <div id="todo_card">
        <div class="text">
            <p class="task_name">{{ todoName }}</p>
            <p class="task_desk">{{ todoDesc }}</p>
            <p class="task_deadline">{{ convertedDate }} </p>
        </div>
        <div class="modifier">
            <router-link :to="`/todo_edit/${todoID}`"><material-symbols-edit class="modifier_button"/></router-link>
            <material-symbols-delete class="modifier_button" v-on:click="deleteData(todoID)" />
        </div>
    </div>
</template>
<script>
export default {
    data (){
        return {
            convertedDate : null,
        }
    }, methods: {
        convertDate(value){
            const date = moment(value)
            this.convertedDate = date.format('MMMM D, YYYY');
        },
        async deleteData(todo_id){
            const response = await axios.delete("http://127.0.0.1:8000/api/todo/", {data:{id:todo_id}})
            .then(function (response){
                console.log(response.data.message)
                location.reload();
            })
            .catch(function (err){
                console.log(err)
            })
        },
    },
    name: 'TodoCard',
    props: [
        'todoID',
        'todoName',
        'todoDesc',
        'todoDeadline',
    ], mounted(){
        this.convertDate(this.todoDeadline)
    }
}
</script>
