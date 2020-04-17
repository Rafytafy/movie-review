<template>
  <div>
    {{ $route.params.movie }}
    <div class="text">
      <img src="Pulp_fiction.jpg" />
      <div class="movietext">
        <h1>Genre</h1>
      </div>
      <h3>Thriller</h3>

      <div class="movietext">
        <h1>Year</h1>
      </div>
      <p1>1994</p1>
      <br />
      <div class="movietext">
        <h1>Score</h1>
      </div>
      <h3>5</h3>
      <br />
      <div class="movietext">
        <h1>Review</h1>
      </div>
      <h3>Date:</h3>
      <p1>April 15, 2020</p1>
      <br />
      <p1>Review goes here</p1>
    </div>
  </div>
</template>

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