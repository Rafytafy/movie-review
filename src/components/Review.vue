<template>
  <div>

    <h2><em>Review Page</em></h2>
    <br>
    <h3>Movie title</h3>
    <b-form-input class="movie-entry" list="input-list" id="input-with-list" v-model="movie" ></b-form-input>
    <b-form-datalist id="input-list" :options="movies"></b-form-datalist>
    <br> <br> <br>
    <h3>Rating</h3>
    <b-form-select class="movie-rating" v-model="ratingSelected" :options="rating"></b-form-select>
    <br> <br> <br> <br>
    <h3>Review</h3>
    <b-form-textarea
    id="textarea-rows"
    class="textarea"
    placeholder="Tall textarea"
    rows="8"
    v-model="reviewText"
  ></b-form-textarea>
  <br>
  <button @click="onSubmit"> Submit </button>
  <button class="reset" @click="onReset" > Reset </button>
  </div>
</template>

<script>
  export default {
    name: 'create_review_comp',
    data() {
      return {
        ratingSelected: null,
        movie: null,
        reviewText: null,
        rating: [
          { value: null, text: 'Please select an option' },
          { value: 1, text: 'Poor(1)' },
          { value: 2, text: 'Below Average(2)' },
          { value: 3, text: 'Average(3)' },
          { value: 4, text: 'Above Average(4)'},
          { value: 5, text: 'Excellent!(5)' }
        ],
        //the movies array will hold the movies contating the matching starting values
        //Ex:Input = S
        //movies[] = ["Scarface", "Scary Movie", "School of Rock"]
        //limit 5 movies
        movies: ['Pulp Fiction', 'The GodFather', 'Scarface', 'Forest Gump']
      }
    },
    methods: {
      onReset(evt){
        this.ratingSelected = null
        this.movie = null
        this.reviewText = null
      },
      onSubmit(evt){
        //Code to transfer form data elements to database (movie, ratingSelected, reviewText)
      }
    }

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

</style>
