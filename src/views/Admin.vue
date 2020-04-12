<template> 
<div>
<h2> <em>Welcome to Movie ReVues</em> </h2>
<br><br>

<span>
<button> Create a user </button>
<button> Pick a user </button>
</span>

<br><br><br><br>
<footer> 
    <h5> Developers</h5>
    <ul>
        <li>Jaren Taylor</li>
        <li>Rafael Montes</li>
        <li>Daniel Christenson</li>
    </ul>
</footer>
</div>
</template>

<script>
  export default {
    name: "Home",

    data() {
      return {
          mode: 'Admin',

            }
      }
  }
</script>

<style scoped>
  #table {
    border: 5px solid #EEE;
    width: 1250px;
    margin-left:auto;
    margin-right:auto;
  }

  ul li{
      display:inline;
      margin-right:10px;
      list-style-type: none;
    }

    ul li::before{
        content: "\2022";  /* Add content: \2022 is the CSS Code/unicode for a bullet */
        color: white; /* Change the color */
        font-weight: bold; /* If you want it to be bold */
        display: inline-block; /* Needed to add space between the bullet and the text */
        width: 1em; /* Also needed for space (tweak if needed) */
        margin-left: -1em; /* Also needed for space (tweak if needed) */

    }

  button{
      border:5px solid transparent;
      width:250px;
      height:200px;
      border-radius: 10px;
      color:white;
      font-size: 25px;
      padding:10px;
      background-color:#af0404;
      margin-left:auto;
      margin-right:auto;
      
  }

  button:hover{
      opacity: .5;
  }
</style>
