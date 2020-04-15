<template>
<div>
  <div id="table">
      <h2>
        Welcome,{{this.curr_user.userName}}
      </h2>
  </div>
</div>
</template>

<script>
import axios from 'axios';

  export default {
    name: "User",
    data() {
      return {
        path: 'http://localhost:5000',
        perPage: 3,
        currentPage: 1,
      }
    },
    props:['curr_user'],
    methods:{

      updateMovies(){
        axios({method:'post',
          url:this.path,
           headers: {
    'Content-type': 'application/json'
  },
  data: {
    movies: this.movies
  }

        }).then((res)=>{
          console.log(res);
        })
      },
    },
    computed: {
      rows() {
        return this.movies.length
      }
    }
  }
</script>

<style>

  .router-link-active,
  .router-link-exact-active,
  .router-link-active:hover,
  .router-link-exact-active:hover{
   color: white;
   cursor: pointer;
 }

  #table {
    border: 5px solid #414141;
    width: 1250px;
    margin-left:auto;
    margin-right:auto;
    background-color: #414141;
  }
 td,th{
    color: white;
  }
  body{
    background-color:#414141
  }
</style>
