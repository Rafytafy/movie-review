<template>
  <div>
    <h2><em>Review Page</em></h2>
    <br>
    <h3>Movie title</h3>
    <b-form-input class="movie-entry" list="input-list" id="input-with-list"></b-form-input>
    <b-form-datalist id="input-list" :options="movies"></b-form-datalist>
    <br> <br> <br>
    <h3>Rating</h3>
    <b-form-select class="movie-rating" v-model="selected" :options="options"></b-form-select>
    <br> <br> <br> <br>
    <h3>Review</h3>
    <b-form-textarea
    id="textarea-rows"
    class="textarea"
    placeholder="Tall textarea"
    rows="8"
  ></b-form-textarea>
  <br>
  <button> Submit </button>
  <button> Reset </button>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        movies: ['Pulp Fiction', 'The GodFather', 'Scarface', 'Forest Gump']
      }
    },

  }
</script>

<style>

  div {
    text-align: center;
  }
  button{
      border:5px solid transparent;
      border-radius: 10px;
      color:white;
      font-size: 25px;
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

  .textarea
  {
    width: 1000px;
    margin-left:auto;
    margin-right:auto;
  }

</style>
