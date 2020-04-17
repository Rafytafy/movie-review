<template>
  <div>
    <h2>
      <em>Home</em>
    </h2>
    <div id="Home" v-if="this.mode == 'user'">
      <span>
        <button class="home-btn" @click="createReview()">Create a Review</button>
        <button class="home-btn" @click="editReview()">Edit/Delete Review</button>
      
        <br />
        <br />
    <b-table id="hometable"
     striped hover
    :items="movies"
    :fields="fields"
    @row-clicked="movieSelected"
    />

    <b-table id="hometable"
     striped hover
    :items="movies"
    :fields="fields"
    @row-clicked="movieSelected"
    />
      </span>
    </div>

    <div id="admin" v-if="this.mode == 'createReview'">
      <span>
        <createReviewComp v-bind:curr_user="this.curr_user" />
        <button class="back-btn" @click="home()">Back</button>
      </span>
    </div>
    <div id="admin" v-if="this.mode == 'editReview'">
      <span>
        <editReviewComp v-bind:curr_user="this.curr_user" />
        <button class="back-btn" @click="home()">Back</button>
      </span>
    </div>


  </div>
</template>

<script>
import axios from "axios";
import createReviewComp from "@/components/Review.vue";
import editReviewComp from "@/components/EditReview.vue";

export default {
  name: "Home",
  components: {
    createReviewComp,
    editReviewComp
  },
  props: ["curr_user"],
  created(){
    if (this.curr_user.userName != "Admin") {
      this.mode = "user";
    }
    else{
      if(this.curr_user.userName == "Admin"){
        alert('You must sign in before you can leave the Login page');
        this.$router.push("/");
      }
    }
    
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
              if(this.movies.length <= 10){
            this.movies.push(movieEntry);
              }
          }
        });
  },
  data() {
    return {
      path: "http://localhost:5000",
      mode: "",
      movies:[],
      fields:[
          {
            key: 'Title',
            label: 'Title'
          },
         
          {
            key: 'Rating',
            label: 'Score'
          },
          

        ]
    };
  },
  methods: {
    createReview() {
      this.mode = "createReview";
    },
    editReview() {
      this.mode = "editReview";
    },
    home() {
      this.mode = "user";
    },
   movieSelected(record, index){
      console.log('row clicked')
      console.log(record)
    }
  }
};
</script>

<style>
.router-link-active,
.router-link-exact-active,
.router-link-active:hover,
.router-link-exact-active:hover {
  color: white;
  cursor: pointer;
}

.home-btn {
  border: 5px solid transparent;
  width: 250px;
  height: 200px;
  border-radius: 10px;
  color: white;
  font-size: 25px;
  padding: 10px;
  background-color: #af0404;
  margin-left: auto;
  margin-right: 10px;
}
.back-btn {
  float: right;
  margin-right: 10px;
  margin-bottom: 10px;
}

body {
  background-color: #414141;
}
#hometable {
  display: inline;
  border-collapse: collapse;
  padding: 40px;
  border-radius: 10px solid black;
  border-radius: 10px;
}

#hometable td {
  text-align: center;
  padding: 10px;
  border-radius: 10px solid black;
  border-radius: 10px;
  border-top: 1px solid white;
  color: white;
}
#class {
  border-collapse: collapse;
  width: 60%;
}

#hometable th {
  text-align: center;
  background-color: #af0404;
  padding: 40px;
  padding-top: 8px;
  padding-bottom: 8px;
  text-align: center;
  padding: 10px;
}
#hometable th:first-child {
  border-radius: 10px 0 0 0;
}

#hometable th:last-child {
  border-radius: 0 10px 0 0;
}

#hometable th:only-child {
  border-radius: 10px 10px 0 0;
}
</style>
