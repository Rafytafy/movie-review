<template>
<div>
  <div id="table">

    <b-table class="test"
     striped hover
      :items="movies"
      :per-page="perPage"
      :current-page="currentPage">
      </b-table>

  </div>
</div>
</template>

<script>
import axios from 'axios';

  export default {
    name: "Home",
    data() {
      return {
        path: 'http://localhost:5000',
        connected:false,
        perPage: 3,
        currentPage: 1,
        movies: [
          { movie: 'Pulp Fiction', genre: 'Drama/Crime', year: 1994, score: 0 },
          { movie: 'The GodFather', genre: 'Drama/Crime', year: 1972, score: 0 },
          { movie: 'Scarface', genre: 'Drama/Crime', year: 1983, score: 0 },
          { movie: 'Forest Gump', genre: 'Drama/Magical Realism', year: 1994, score: 0 }
        ]
      }
    },
    methods:{
      postMessage(){
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

      getMessage(){
        axios.get(this.path).then((res)=>{
          this.message=res.data;
          console.log(res);
          this.connected=true;
        }).catch((error)=> {
          console.error(error);
        });
      }
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
