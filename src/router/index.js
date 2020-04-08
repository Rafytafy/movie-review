import Vue from 'vue'
import Router from 'vue-router'
import Admin from '@/views/Admin'
import Home from '@/views/Home'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Admin',
      component: Admin
    },
    {
      path: '/user',
      name: 'user',
      component: Home
    }
  ]
})
