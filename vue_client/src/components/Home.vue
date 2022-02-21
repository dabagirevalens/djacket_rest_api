<template>
  <div class="home">
    <section class="welcome">
      <div class="hello text-center text-white bg-gray-900 py-24">
        <p class="text-4xl my-2">Welcome to Djackets</p>
        <p>Best online jackets store.</p>
      </div>
    </section>
    <div class="content p-12">
      <div class="title text-center font-bold text-3xl">
        <h2>Latest Products.</h2>
      </div>
      <div class="products flex flex-wrap">
        <ProductBox
          v-for="product in latestProducts"
          :key="product.id"
          :product="product"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import axios from "axios";
import ProductBox from "./ProductBox.vue";

import { defineComponent } from "vue";

export default defineComponent({
  name: "HomeComponent",
  data() {
    return {
      latestProducts: [],
    };
  },
  components: {
    ProductBox,
  },

  mounted() {
    this.getLatestProducts();
    document.title = "Home | Djackets";
  },

  methods: {
    async getLatestProducts() {
      this.$store.commit("setIsLoading", true);
      const response = await axios.get("/api/v1/latest-products/");
      this.latestProducts = response.data;
      this.$store.commit("setIsLoading", false);
    },
  },
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
</style>
