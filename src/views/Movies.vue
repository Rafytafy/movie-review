<template>
  <div id="table">
    <b-table  striped hover
    :items="movies"
    :fields="fields"
    :per-page="perPage"
    :current-page="currentPage"
    @row-clicked="movieSelected"
    >
    
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
import axios from "axios";
  export default {
    name: "Movies",
    data() {
      return {
        path: "http://localhost:5000",
        perPage: 3,
        currentPage: 1,
        movies: [
        ],
        fields:[
          {
            key: 'Title',
            label: 'Title'
          },
          {
            key: 'Genre',
            label: 'Genre'
          },
          {
            key: 'Release Year',
            label: 'Released'
          },
          {
            key: 'Rating',
            label: 'Score'
          },
          {
            key: 'Author',
            label: 'Review Author'
          },
          {
            key: 'Date',
            label: 'Date-Published'
          },

        ]
      }
    },
    computed: {
      rows() {
        return this.movies.length
      }
    },
    //created runs when page loads
    created()
      {
        axios({
          method: "post",
          url: this.path,
          headers: {
            "Content-type": "application/json"
          },
          data: {
            header: "fetch",
            table: "reviews",
            content: ""
          }
        }).then(res => {
          // this.movies = res.data.content;
          for (let item in res.data.content) {
            let movieEntry={
              'Title': res.data.content[item].movieTitle,
              'Genre': res.data.content[item].movieGenre,
              'Release Year': res.data.content[item].movieYear,
              'Rating': res.data.content[item].movieRating,
              'Author': res.data.content[item].movieAuthor,
              'Date': res.data.content[item].movieDate,
              'Review': res.data.content[item].movieReview,
              }
            this.movies.push(movieEntry);
          }
        });
  },
  methods:{
    movieSelected(record, index){
      console.log('row clicked')
      console.log(record)
    }
  }
};
</script>

<style>

  #table {
    border: 5px solid #414141;
    width: 1250px;
    margin-left:auto;
    margin-right:auto;
    color:white;
  }
 td,th {
  color:white;
}

</style>
