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
            <label for="priority">Priority</label>
            <select name="priority" id="prio" v-model="data.prio" @change="showValue()">
                <option value="high">High</option>
                <option value="medium">Medium</option>
                <option value="low">Low</option>
            </select>
            <button class="btn" style="margin-top: 10px;"><material-symbols-add/></button>
        </form>
    </div>
</template>
<script>
export default {
    data(){
        return{
            data:{
                status:false,
                name:null,
                desc:null,
                prio:null,
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
                priority:this.data.prio
            })
            .then(function(response){
                console.log(response.data.success);
                alert("To Do Added!");
            })
            .catch(function(err){
                console.log(err);
            })
        },
        showValue(){
            console.log(this.data.prio);
        }
    }, mounted(){
    }
}
</script>
