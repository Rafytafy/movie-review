<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Login</router-link>
      <router-link to="/user" class="router-link-active">Home</router-link>
      <router-link to="/movies" class="router-link-active">Movies</router-link>
      <router-link to="">Review</router-link>
    </div>
    <router-view/>
  </div>
</template>
<script>
export default {
  name: 'App'
}
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
  .router-link-exact-active:hover{
   color: white;
   cursor: pointer;
 }
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  margin-top: 60px;
}
body{
  background-color: #414141;
}
</style>

