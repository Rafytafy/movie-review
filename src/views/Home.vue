<template>
  <div id="table">
    <b-table class="test" striped hover :items="movies"></b-table>
  </div>
</template>

<script>
  export default {
    name: "Home",
    data() {
      return {
        movies: [
          { movie: 'Pulp Fiction', genre: 'Drama/Crime', year: 1994, score: 0 },
          { movie: 'The GodFather', genre: 'Drama/Crime', year: 1972, score: 0 },
          { movie: 'Scarface', genre: 'Drama/Crime', year: 1983, score: 0 },
          { movie: 'Forest Gump', genre: 'Drama/Magical Realism', year: 1994, score: 0 }
        ]
      }
    }
  }
</script>

<style>
  #table {
    border: 5px solid #EEE;
    width: 1250px;
    margin-left:auto;
    margin-right:auto;
  }
</style>
