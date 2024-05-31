<script setup>
    import MaterialSymbolsAdd from '~icons/material-symbols/add';
    import IconParkSolidEnterKey from '~icons/icon-park-solid/enter-key';
    import axios from 'axios'
</script>

<template>
    <div id="form_container">
        <form v-on:submit.prevent="putData()">
            <label for="task_name">Name:</label>
            <input type="text" name="task_name" placeholder="Input Name" v-model="data.name"/>
            <label for="task_desc">Description:</label>
            <input type="text" name="task_desc" placeholder="Input Description" v-model="data.desc">
            <label for="task_deadline">Deadline:</label>
            <input type="date" class="date" v-model="data.deadline">
            <button class="btn" style="margin-top: 10px;"><icon-park-solid-enter-key/></button>
        </form>
    </div>
</template>
<script>
export default {
    data(){
        return{
            data:[],
            id:this.$route.params.id,
        }
    }, methods: {
        async putData(){
            const response = await axios.patch("http://127.0.0.1:8000/api/todo/",{
                id:this.id,
                name:this.data.name,
                desc:this.data.desc,
                deadline:this.data.deadline,
            })
            .then(function(response){
                console.log(response.data);
                alert("To Do Updated!");
            })
            .catch(function(err){
                console.log(err);
            })
        },
        async getData(){
            const response = await axios.get(`http://127.0.0.1:8000/api/edit_todo/${this.id}`)
            this.data = response.data;
        }
    }, mounted(){
        console.log(this.id);
        this.getData();
    }
}
</script>
