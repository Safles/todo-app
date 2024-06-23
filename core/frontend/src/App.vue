<script setup>
</script>
<template>
  <div id="app">
    <div id="main">
    <p id="todo_main">TODO LIST</p>
    <div id="card-container"> 
        <RouterView/>
    </div>
  </div>
  </div>
</template>
<script>
  import TodoAdd from './components/todoAdd.vue';
  import TodoEdit from './components/todoEdit.vue';
  export default{
    components: {
      TodoAdd,
      TodoEdit,
    },
    methods: {

    }
  }
</script>
