import Vue from 'vue'
import Router from 'vue-router'
import Admin from '@/views/Admin'
import Home from '@/views/Home'
import Review from '@/views/Review'
import Movies from '@/views/Movies'
import MovieInfo from '@/views/MovieInfo'


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
      name: 'Home',
      component: Home
    },
    {
      path: '/review',
      name: 'Review',
      component: Review
    },
    {
      path: '/movies',
      name: 'Movies',
      component: Movies
    },
    {
      path: '/movieInfo/:movie',
      name: 'MovieInfo',
      component: MovieInfo

    }

  ]
})
