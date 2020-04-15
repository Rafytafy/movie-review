import Vue from 'vue'
import Router from 'vue-router'
import Admin from '@/views/Admin'
import Home from '@/views/Home'
import Movies from '@/views/Movies'
import MovieInfo from '@/views/MovieInfo'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Admin',
      props:true,
      component: Admin
    },
    {
      path: '/user',
      name: 'User',
      props:true,
      component: Home
    },
    {
      path: '/movies',
      name: 'Movies',
      props:true,
      component: Movies
    },
    {
      path: '/movieInfo/:movie',
      name: 'MovieInfo',
      props:true,
      component: MovieInfo

    }

  ]
})
