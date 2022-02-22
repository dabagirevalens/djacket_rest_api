<template>
  <div class="home">
    <div class="content p-12">
      <div class="title text-center">
        <h1 class="font-bold text-3xl">Search</h1>
        <p class="">Search term : "{{ query }}"</p>
      </div>
      <div class="products flex flex-wrap my-6 mx-12">
        <ProductBox
          v-for="product in products"
          :product="product"
          :key="product.id"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

import ProductBox from "./ProductBox.vue";

export default {
  name: "SearchComponent",
  components: {
    ProductBox,
  },
  data() {
    return {
      products: [],
      query: "",
    };
  },
  mounted() {
    document.title = "Search | Djackets";

    let uri = window.location.search.substring(1);
    let params = new URLSearchParams(uri);

    if (params.get("query")) {
      this.query = params.get("query");
      this.performSearch();
    }
  },

  methods: {
    async performSearch() {
      this.$store.commit("setIsLoading", true);
      const response = await axios.get(
        `/api/v1/products?search_query=${this.query}`
      );

      this.products = response.data;
      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>

<style lang="sass" scoped>
</style>