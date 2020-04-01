<template>
  <div>
    <b-form-input id="myDropdown" class="movie-input" v-model="text" v-on:click= "showMovies()" v-on:keyup.enter="searchMovie('Hello')" placeholder="Enter name of movie"></b-form-input>
    <div class="mt-2">Value: {{ text }}</div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        text: '',
        test:"",
        movies: [
          { movie: 'Pulp Fiction', genre: 'Drama/Crime', year: 1994, score: 0 },
          { movie: 'The GodFather', genre: 'Drama/Crime', year: 1972, score: 0 },
          { movie: 'Scarface', genre: 'Drama/Crime', year: 1983, score: 0 },
          { movie: 'Forest Gump', genre: 'Drama/Magical Realism', year: 1994, score: 0 }
        ]
      }
    },
    methods: {
      showMovies(){
        document.getElementById("myDropdown").classList.toggle("show");
        this.text= "FUCK"
      },
      searchMovie(t){
      }
    }
  }
</script>

<style>

  div {
    text-align: center;
  }
  .movie-input {
    width: 500px;
    margin-left:auto;
    margin-right:auto;
  }
</style>
