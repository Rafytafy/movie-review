<template>
  <div>
    <h2>
      <em>Home</em>
    </h2>
    <div id="Home" v-if="this.mode == 'Home'">
      <span>
        <button class="home-btn" @click="createReview()">Create a Review</button>
        <button class="home-btn" @click="editReview()">Edit/Delete Review</button>
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
</style>
