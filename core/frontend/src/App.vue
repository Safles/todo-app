<script setup>
  import MaterialSymbolsAdd from '~icons/material-symbols/add';
  import EpBack from '~icons/ep/back';
</script>
<template>
  <div id="app">
    <div id="main">
    <p id="todo_main">TODO LIST</p>
    <div id="card-container"> 
        <RouterView/>
    </div>
    <div id="button">
        <div v-if="$route.name === 'addTodo'">
          <a class="btn" href="/"><EpBack /></a>
        </div>
        <div v-else-if="$route.name === 'editTodo'">
          <a class="btn" href="/"><EpBack /></a>
        </div>
        <div v-else>
          <a class="btn" href="/todo_add"><material-symbols-add/></a>
        </div>
    </div>
  </div>
  </div>
</template>
<script>
  import TodoCard from './components/todoCard.vue';
  import TodoAdd from './components/todoAdd.vue';
  import TodoEdit from './components/todoEdit.vue';
  export default{
    components: {
      TodoCard,
      TodoAdd,
      TodoEdit,
    },
    methods: {

    }
  }
</script>
