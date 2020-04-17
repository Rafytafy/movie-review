<template>
  <div id="app">
    <h3 id="currentLogin">Currently Logged in as, {{userData.userName}}</h3>
    <div id="nav">
      <router-link to="/">Login</router-link>
      <router-link to="/user" class="router-link-active">Home</router-link>
      <router-link to="/movies" class="router-link-active">Movies</router-link>
    </div>
      <router-view v-on:user-selected="onSelect" v-bind:curr_user="userData"></router-view>
  </div>
</template>
<script>
export default {
  name: "App",
  data: function() {
    return {
      userData: {
        userName: "Admin",
        reviews: null,
        movies: null
      }
    };
  },
  methods: {
    onSelect(user) {
      this.userData = user;
    }
}
};
</script>

<style>
/* general styling tips for this project */
/*  The colors we will use are:
a grey -> #414141,
a dark grey -> #252525,
a red -> #ff0000,
and a dark red -> #af0404.
 all the text we display should be specified as 'white'.
*/
.router-link-active,
.router-link-exact-active,
.router-link-active:hover,
.router-link-exact-active:hover {
  color: white;
  cursor: pointer;
}
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  margin-top: 60px;
}
body {
  background-color: #414141;
}
#currentLogin{
  float:left;
  margin-top: -50px;
  text-emphasis: italic;
  font-size: 18px;
}
</style>
