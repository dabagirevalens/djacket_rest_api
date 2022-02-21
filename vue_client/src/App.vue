<template>
  <div>
    <NavBar :cartTotalLength="cartTotalLength" />
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
  data() {
    return {
      cart: {
        items: [],
      },
    };
  },

  beforeCreate() {
    this.$store.commit("initializeStore");
  },

  mounted() {
    this.cart = this.$store.state.cart
  },

  computed :{
    cartTotalLength(){
      let totalLength = 0

      for(let i=0; i<this.cart.items.length; i++){
        totalLength += this.cart.items[i].quantity
      }

      return totalLength
    }
  }
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
