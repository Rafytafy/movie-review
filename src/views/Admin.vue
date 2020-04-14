<template>
  <div>
    <h2>
      <em>Welcome to Movie ReVues</em>
    </h2>
    <br />
    <br />
    <div id="admin" v-if="this.mode == 'admin'">
      <span>
        <button @click="createUser()">Create a user</button>
        <button @click="signIn()">Pick a user</button>
      </span>
    </div>
    <div id="createUser" v-if="this.mode=='createUser'">
      <div>
        <header>
          <em>Register a username</em>
        </header>
        <span id="input">
          <label for="username">Username</label>
          <input
            id="forminput"
            type="text"
            placeholder="enter your desired name"
            @keyup.enter="newUser()"
          />
        </span>
        <button @click="newUser()" class="formbtn">create user</button>
      </div>
    </div>
    <br />
    <br />
    <br />
    <br />
    <footer>
      <h5>Developers</h5>
      <ul>
        <li>Jaren Taylor</li>
        <li>Rafael Montes</li>
        <li>Daniel Christenson</li>
      </ul>
    </footer>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Home",

  data() {
    return {
      path: "http://localhost:5000",
      //Valid modes are admin, user, createUser,signIn
      mode: "admin",
      currUser: {
        userName: "",
        reviews: null,
        movies: null
      }
    };
  },
  methods: {
    createUser() {
      this.mode = "createUser";
    },
    signIn() {},
    newUser() {
      this.currUser.userName = document.getElementById("forminput").value;
      document.getElementById("forminput").value = "";
      console.log(this.currUser.userName);
      this.dbInsert(this.currUser);
    },
    //this takes an object and wraps it in a larger JSON to send to the db.
    dbInsert(obj) {
      axios({
        method: "post",
        url: this.path,
        headers: {
          "Content-type": "application/json"
        },
        data: {
            header: "insert",
            table: "users",
            content: obj 
        }
      }).then(res => {
        console.log(res);
      });
    }
  }
};
</script>

<style scoped>
#table {
  border: 5px solid #eee;
  width: 1250px;
  margin-left: auto;
  margin-right: auto;
}

ul li {
  display: inline;
  margin-right: 10px;
  list-style-type: none;
}

ul li::before {
  content: "\2022";
  color: white;
  font-weight: bold;
  display: inline-block;
  width: 1em;
  margin-left: -1em;
}

button {
  border: 5px solid transparent;
  width: 250px;
  height: 200px;
  border-radius: 10px;
  color: white;
  font-size: 25px;
  padding: 10px;
  background-color: #af0404;
  margin-left: auto;
  margin-right: auto;
}
.formbtn {
  border: 5px solid transparent;
  width: 200px;
  height: 75px;
  border-radius: 10px;
  color: white;
  font-size: 25px;
  padding: 10px;
  background-color: #af0404;
  margin-left: auto;
  margin-right: auto;
}

#forminput {
  border: 3px solid #252525;
  width: 334px;
  height: 75px;
  border-radius: 10px;
  font-size: 25px;
  padding: 10px;
  color: white;
  background-color: #414141;
  margin-left: auto;
  margin-right: auto;
}
label {
  font-size: 25px;
  color: white;
  text-emphasis: italic;
}
button:hover {
  opacity: 0.5;
}
</style>
