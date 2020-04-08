<template>
  <div id="table">
    <b-table  striped hover
    :items="movies"
    :per-page="perPage"
    :current-page="currentPage"
    >
    <template v-slot:cell(movie)="data">
        <!-- `data.value` is the value after formatted by the Formatter -->
        <router-link :to="`/movieInfo/${data.value}`">
          {{ data.value }}
        </router-link>
      </template>
    </b-table>

    <b-pagination
      class="pagination"
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      aria-controls="table"
    ></b-pagination>
  </div>
</template>

<script>
  export default {
    name: "Movies",
    data() {
      return {
        perPage: 3,
        currentPage: 1,
        movies: [
          { movie: 'Pulp Fiction', genre: 'Drama/Crime', year: 1994, score: 0 },
          { movie: 'The GodFather', genre: 'Drama/Crime', year: 1972, score: 0 },
          { movie: 'Scarface', genre: 'Drama/Crime', year: 1983, score: 0 },
          { movie: 'Forest Gump', genre: 'Drama/Magical Realism', year: 1994, score: 0 },
          { movie: 'Pulp Fiction', genre: 'Drama/Crime', year: 1994, score: 0 },
          { movie: 'The GodFather', genre: 'Drama/Crime', year: 1972, score: 0 },
          { movie: 'Scarface', genre: 'Drama/Crime', year: 1983, score: 0 },
          { movie: 'Forest Gump', genre: 'Drama/Magical Realism', year: 1994, score: 0 },
          { movie: 'Pulp Fiction', genre: 'Drama/Crime', year: 1994, score: 0 },
          { movie: 'The GodFather', genre: 'Drama/Crime', year: 1972, score: 0 },
          { movie: 'Scarface', genre: 'Drama/Crime', year: 1983, score: 0 },
          { movie: 'Forest Gump', genre: 'Drama/Magical Realism', year: 1994, score: 0 },
          { movie: 'Pulp Fiction', genre: 'Drama/Crime', year: 1994, score: 0 },
          { movie: 'The GodFather', genre: 'Drama/Crime', year: 1972, score: 0 },
          { movie: 'Scarface', genre: 'Drama/Crime', year: 1983, score: 0 },
          { movie: 'Forest Gump', genre: 'Drama/Magical Realism', year: 1994, score: 0 }
        ]
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

  #table {
    border: 5px solid #EEE;
    width: 1250px;
    margin-left:auto;
    margin-right:auto;
  }


</style>
