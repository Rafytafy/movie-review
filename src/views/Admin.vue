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

    <div id="admin" v-if="this.mode == 'user'">
      <span>
        <button @click="signIn()">Pick a user</button>
      </span>
    </div>

    <div id="createUser" v-if="this.mode=='createUser'">
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
      <br />
      <br />
      <hr />
      <button class="back-btn" @click="home()">Back</button>
    </div>

    <div id="signIn" v-if="this.mode =='signIn'">
      <label for="user select">Select a user from this list</label>
      <br />
      <span v-for="user in userList " v-bind:user="userList" v-bind:key="user.userName">
        <hr />
        <button class="formbtn" @click="selectUser(user)">{{user.userName}}</button>
        <hr />
      </span>
      <button class="back-btn" @click="home()">Back</button>
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
  props: ["curr_user"],
  data() {
    return {
      path: "http://localhost:5000",
      //Valid modes are admin, user, createUser,signIn
      mode: "admin",
      currUser: {
        userName: "Admin",
        reviews: null,
        movies: null
      },
      userList: [],

      backendData: {}
    };
  },
  created() {
    console.log("on admin create");
    this.currUser = this.curr_user;
    if (this.currUser.userName != "Admin") {
      this.mode = "user";
    }
    axios({
      method: "post",
      url: this.path,
      headers: {
        "Content-type": "application/json"
      },
      data: {
        header: "fetch",
        table: "users",
        content: ""
      }
    }).then(res => {
      this.backendData = res.data.content;
      this.userList = [];
      for (let item in this.backendData) {
        this.userList.push(this.backendData[item]);
      }
    });
  },
  methods: {
    createUser() {
      this.mode = "createUser";
    },

    signIn() {
      this.mode = "signIn";
    },
    home() {
      this.mode = "admin";
    },

    newUser() {
      // here we get the input from the text boxes and then send it to the backend. We reset mode to Admin so the
      // admin can create more users or sign in to any existing user.
      this.currUser.userName = document.getElementById("forminput").value;
      document.getElementById("forminput").value = "";
      this.dbInsert(this.currUser);
      this.mode = "admin";
    },

    selectUser(user) {
      // after we select a user, we want to change the mode to user and then redirect to the home page.

      this.currUser = user;
      this.$emit("user-selected", user);
      this.mode = "user";
      this.$router.push("/user");
    },
    showUsers() {},
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
          exception: false,
          exceptionText: "",
          content: obj
        }
      }).then(res => {
        if (res.data.exception) {
          alert(res.data.exceptionText);
        } else {
          // this gets the response from server.py, which is the entire users table
          // it then chooses the table entities as rows (username, movies, reviews) and pushes them into the backendData
          // object. If you look at the database.py function 'db_insert' you'll see that I created an
          // array of dicts (json object)s which represent each user and their reviews and movies. Here, we iterate
          // through that and choose each user and their corresponding data to be added to the userList, which is then
          // displayed once the user clicks the select user button.

          this.backendData = res.data.content;
          this.userList = [];
          for (let item in this.backendData) {
            this.userList.push(this.backendData[item]);
          }
        }
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
.back-btn {
  float: right;
  width: 200px;
  height: 75px;
  margin-right: 10px;
  margin-bottom: 10px;
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
