import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/views/HelloWorld'
import Home from '@/views/Home'
import Review from '@/views/Review'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/qwer',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/review',
      name: 'Review',
      component: Review
    }
  ]
})
