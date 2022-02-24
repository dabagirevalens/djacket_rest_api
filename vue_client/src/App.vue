<template>
  <div>
    <NavBar :cartTotalLength="cartTotalLength" />

    <div
      class="is-loading-message font-bold text-center"
      :class="{ 'is-loading': $store.state.isLoading }"
    >
      <span>Loading ......</span>
    </div>

    <router-view />

    <footer class="text-center font-bold">
      <p>&copy;2022 Djackets | all rights reserved.</p>
    </footer>
  </div>
</template>

<script>
import axios from 'axios';
import NavBar from "./components/Nav.vue";

export default {
  components: {
    NavBar,
  },
  data() {
    return {
      cart: {
        items: [],
      },
    };
  },

  beforeCreate() {
    this.$store.commit("initializeStore");

    const token = this.$store.state.token

    if(token){
      axios.defaults.headers.common['Authorization'] = "Token " + token
    }else{
      axios.defaults.headers.common['Authorization'] = ""
    }

  },

  mounted() {
    this.cart = this.$store.state.cart;
  },

  computed: {
    cartTotalLength() {
      let totalLength = 0;

      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity;
      }

      return totalLength;
    },
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

.is-loading-message{
  height: 0;
  overflow: hidden;

  &.is-loading{
    height: 40px;
  }
}
</style>
