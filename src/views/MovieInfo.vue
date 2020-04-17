<template>
  <div>
    <div v-if="!isDeleted && mode === 'Home'">
      {{ selectedMovie }}
      <div class="text">
        <h1>Genre</h1>
        <h3>Thriller</h3>
        <br />
        <h1>Year</h1>
        <p1>1994</p1>
        <br />
        <h1>Score</h1>
        <h3>5</h3>
        <br />
        <h1>Review</h1>
        <h3>Date</h3>
        <p1>April 15, 2020</p1>
        <br />
        <p1>Review goes here</p1>
        <br />
        <!-- Check to see if current user is set
        If set then button will appear to edit or delete review-->
        <button v-if="curr_user" @click="editMovie()">Edit Review</button>
        <button v-if="curr_user" @click="deleteMovie()">Delete Review</button>
      </div>
    </div>
    <div v-if="isDeleted">
      <h1>MOVIE REVIEW DELETED</h1>
    </div>
    <div v-if="mode == 'editReview'">
      <createReviewComp v-bind:curr_user="this.curr_user" />
    </div>
  </div>
</template>

<script>
import createReviewComp from "@/components/Review.vue";

export default {
  name: "MovieInfo",
  components: {
    createReviewComp
  },
  data() {
    return {
      path: "http://localhost:5000",
      mode: "Home",
      isDeleted: false,
      selectedMovie: this.$route.params.movie,
      //movieReview holds values related to the currently selected review
      movieReview: {}
    };
  },
  props: ["curr_user"],
  methods: {
    deleteMovie() {
      this.isDeleted = true;
      //Write logic to delete review entry in database
    },
    editMovie() {
      this.mode = "editReview";
      //Write logic to delete review entry in data base then createReviewComp will handle inserting a new entry
    }
  },
  //created runs when page loads
  created: {
    getMovieReview() {
      //Make a call to backend to retrieve the movie review given the current user and movie
    }
  }
};
</script>
<style>
.text {
  text-align: center;
}
.movietext {
  background-color: #af0404;
  background-size: 50% 50%;
  text-decoration: underline;
  text-decoration-color: gray;
  border: black 1px;
  margin-right: 20%;
  margin-left: 20%;
}
</style>
