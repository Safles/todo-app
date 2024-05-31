import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/components/todoHome.vue'
import TodoAdd from '@/components/todoAdd.vue'
import TodoEdit from '@/components/todoEdit.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    }
  ]
})
router.addRoute({path:'/todo_add', name: 'addTodo', component: TodoAdd})
router.addRoute({path:'/todo_edit/:id', name: 'editTodo', component: TodoEdit})

export default router
