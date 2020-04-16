<template>
  <div>
    {{ $route.params.movie }}
    <div class="text">
      <h1>Genre</h1>
      <h3>Thriller</h3>
      <br />
      <h1>Year</h1>
      <p1>1994</p1>
      <br />
      <h1>Score</h1>
      <h3>5</h3>
      <br />
      <h1>Review</h1>
      <h3>Date</h3>
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
h1,
h2 {
  background-color: #af0404;
  background-size: 50% 50%;
  text-decoration: underline;
  text-decoration-color: gray;
  border: black 1px;
  margin-right: 300px;
  margin-left: 300px;
}
</style> 