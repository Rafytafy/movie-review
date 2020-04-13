<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">
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
  <b-button> Submit </b-button>
  <b-button class="reset" type="reset" variant="danger"> Reset </b-button>
  </b-form>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        show: true,
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
        movies: ['Pulp Fiction', 'The GodFather', 'Scarface', 'Forest Gump']
      }
    },
    methods: {
      onReset(evt){
        evt.preventDefault()
        this.ratingSelected = null
        this.movie = null
        this.reviewText = null
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
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
