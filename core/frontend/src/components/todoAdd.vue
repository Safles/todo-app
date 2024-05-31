<script setup>
    import MaterialSymbolsAdd from '~icons/material-symbols/add';
    import axios from 'axios'
    import moment from 'moment'
</script>

<template>
    <div id="form_container">
        <form v-on:submit.prevent="postData()">
            <label for="task_name">Name:</label>
            <input type="text" name="task_name" placeholder="Input Name" v-model="data.name"/>
            <label for="task_desc">Description:</label>
            <input type="text" name="task_desc" placeholder="Input Description" v-model="data.desc">
            <label for="task_deadline">Deadline:</label>
            <input type="date" class="date" v-model="data.date">
            <button class="btn" style="margin-top: 10px;"><material-symbols-add/></button>
        </form>
    </div>
</template>
<script>
export default {
    data(){
        return{
            data:{
                name:null,
                desc:null,
                date:null,
            },
            date:moment()
        }
    }, methods: {
        async postData(){
            const response = await axios.post("http://127.0.0.1:8000/api/todo/",{
                name:this.data.name,
                desc:this.data.desc,
                deadline:this.data.date,
            })
            .then(function(response){
                console.log(response.data.success);
                alert("To Do Added!");
            })
            .catch(function(err){
                console.log(err);
            })
        }
    }, mounted(){
    }
}
</script>
