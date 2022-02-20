<template>
  <div>
    <NavBar />
    <router-view />

    <footer class="text-center font-bold">
      <p>&copy;2022 Djackets | all rights reserved.</p>
    </footer>
  </div>
</template>

<script>
import NavBar from "./components/Nav.vue";

export default {
  components: {
    NavBar,
  },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Ubuntu:wght@300;400&display=swap");
#app {
  font-family: "Ubuntu", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
