import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home'
import Movies from '@/views/Movies'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/movies',
      name: 'Movies',
      component: Movies
    }

  ]
})
