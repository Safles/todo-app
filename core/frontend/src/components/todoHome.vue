<script setup>
import axios from 'axios'
import TodoCard from '@/components/todoCard.vue'
</script>

<template>
  <div v-if="todo.length > 0">
            <TodoCard v-for="data in todo" 
            :todoID="data.id" 
            :todoName="data.name" 
            :todoDesc="data.desc"
            :todoDeadline="data.deadline"/>
        </div>
        <div v-else>
            <p style="text-align: center; color: red; font-weight: bold;">No To Do Available!</p>
        </div>
</template>
<script>
export default {
    data(){
        return{
            todo: [],
        }
    }, methods: {
        async loadToDoData() {
            const response = await axios.get("http://127.0.0.1:8000/api/todo/");
            this.todo = response.data;
        },
    }, mounted(){
        this.loadToDoData();
    }
}
</script>
