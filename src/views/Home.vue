<template>
  <div>
    <h2>
      <em>Home</em>
    </h2>
    <div id="Home" v-if="this.mode == 'Home'">
      <span>
        <button class="home-btn" @click="createReview()">Create a Review</button>
        <button class="home-btn" @click="editReview()">Edit/Delete Review</button>
        <br />
        <br />
        <table id="hometable">
          <tr>
            <th>Top Ten Best Movies</th>
            <th>Genre</th>
          </tr>
          <tr>
            <td>Movie 1</td>
            <td>Genre 1</td>
          </tr>
          <tr>
            <td>Movie 2</td>
            <td>Genre 2</td>
          </tr>
          <tr>
            <td>Movie 3</td>
            <td>Genre 3</td>
          </tr>
          <tr>
            <td>Movie 4</td>
            <td>Genre 4</td>
          </tr>
          <tr>
            <td>Movie 5</td>
            <td>Genre 5</td>
          </tr>
        </table>
        <table id="hometable">
          <tr>
            <th>Top Ten Worst Movies</th>
            <th>Genre</th>
          </tr>
          <tr>
            <td>Movie 1</td>
            <td>Genre 1</td>
          </tr>
          <tr>
            <td>Movie 2</td>
            <td>Genre 2</td>
          </tr>
          <tr>
            <td>Movie 3</td>
            <td>Genre 3</td>
          </tr>
          <tr>
            <td>Movie 4</td>
            <td>Genre 4</td>
          </tr>
          <tr>
            <td>Movie 5</td>
            <td>Genre 5</td>
          </tr>
        </table>
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
  data() {
    return {
      path: "http://localhost:5000",
      mode: "Home"
    };
  },
  props: ["curr_user"],
  methods: {
    createReview() {
      this.mode = "createReview";
    },
    editReview() {
      this.mode = "editReview";
    },
    home() {
      this.mode = "Home";
    },
    postMessage() {
      axios({
        method: "post",
        url: this.path,
        headers: {
          "Content-type": "application/json"
        },
        data: {}
      }).then(res => {
        console.log(res);
      });
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
  color: darkgray;
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
