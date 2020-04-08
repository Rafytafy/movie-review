import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home'
import Movies from '@/views/Movies'
import MovieInfo from '@/views/MovieInfo'

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
    },
    {
      path: '/movieInfo',
      name: 'MovieInfo',
      component: MovieInfo
    }

  ]
})
