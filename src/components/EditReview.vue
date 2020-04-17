<template>
  <div>

    <h2><em>Edit Reviews Page</em></h2>
    <div>
      <b-table  striped hover
      :items="movies"
      >
      <template v-slot:cell(movie)="data">
          <!-- `data.value` is the value after formatted by the Formatter -->
          <router-link :to="`/movieInfo/${data.value}`">
            {{ data.value }}
          </router-link>
        </template>
      </b-table>
    </div>

  </div>
</template>

<script>
  export default {
    name: 'edit_review_comp',
    props: ["curr_user"],
    data() {
      return {
        //movies is hard coded, movies variable is a list of reviews that the current user has wrote
        movies: [
          {movie: "Scarface", score: 3}

        ]
      }
    },


  }
</script>

<style>

  #
  div {
    text-align: center;
  }
  button{
      border:5px solid transparent;
      border-radius: 10px;
      color:white;
      font-size: 20px;
      padding:10px;
      background-color:#af0404;
      margin-left:auto;
      margin-right:auto;

  }

  button:hover{
      opacity: .5;
  }
   .movie-entry, .movie-rating {
    width: 500px;
    margin-left:auto;
    margin-right:auto;
  }

  .textarea{
    width: 1000px;
    margin-left:auto;
    margin-right:auto;
  }
  .reset {
    background-color:#252525;
  }
  .genre-year {
    width: 300px;
    margin: 0 auto;
  }

</style>
