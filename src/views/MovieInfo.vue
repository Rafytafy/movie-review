<template>
  <div id="table">
    <b-table
      striped
      hover
      :items="movies"
      :fields="fields"
      :per-page="perPage"
      :current-page="currentPage"
      @row-clicked="movieSelected"
    ></b-table>

    <b-pagination
      class="pagination"
      v-model="currentPage"
      :total-rows="this.movies.length"
      :per-page="perPage"
      aria-controls="table"
    ></b-pagination>
    <div v-if="rowSelected">
      <h4>Selected Movie: {{this.selectedRow.Title}}</h4>
      <h4>Review Author: {{this.selectedRow.Author}}</h4>
      <p>{{this.selectedRow.Review}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieInfo",

  data() {
    return {
      perPage: 3,
      currentPage: 1,
      rowSelected: false,
      selectedRow: {
        Author: null,
        Date: null,
        Genre: null,
        Rating: null,
        ReleaseYear: null,
        Review: null,
        Title: null
      },
      movies: [],
      fields: [
        {
          key: "Title",
          label: "Title"
        },
        {
          key: "Genre",
          label: "Genre"
        },
        {
          key: "Release Year",
          label: "Released"
        },
        {
          key: "Rating",
          label: "Score"
        },
        {
          key: "Author",
          label: "Review Author"
        },
        {
          key: "Date",
          label: "Date-Published"
        }
      ]
    };
  },
    props: ["curr_user"],
    created() {
      if (this.curr_user.userName == "Admin") {
        alert("You must sign in before you can leave the Login page");
        this.$router.push("/");
      }
      
      for (let item in this.curr_user.reviews) {
            let movieEntry={
              'Title': this.curr_user.reviews[item].movieTitle,
              'Genre': this.curr_user.reviews[item].movieGenre,
              'Release Year': this.curr_user.reviews[item].movieYear,
              'Rating': this.curr_user.reviews[item].movieRating,
              'Author': this.curr_user.reviews[item].movieAuthor,
              'Date': this.curr_user.reviews[item].movieDate,
              'Review': this.curr_user.reviews[item].movieReview,
              }
            this.movies.push(movieEntry);
    }
    },
    methods: {
      movieSelected(record, index) {
        this.selectedRow.Author = record.Author;
        this.selectedRow.Title = record.Title;
        this.selectedRow.Review = record.Review;
        this.rowSelected = true;
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
