<template>
  <div class="home">
    <div class="content p-12">
      <div class="title text-center font-bold text-3xl">
        <h2 class="text-4xl my-2">{{ category.name }} Djackets</h2>
      </div>
      <div class="products flex flex-wrap my-6 mx-12">
        <ProductBox
          v-for="product in category.products"
          :key="product.id"
          :product="product"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import axios from "axios";
import ProductBox from "./ProductBox.vue";

export default defineComponent({
  name: "CategoryComponent",
  data() {
    return {
      category: {
        name: "",
        products: [],
      },
    };
  },
  components: {
    ProductBox,
  },

  mounted() {
    this.getCategory();
  },

  watch: {
    $route(to) {
      if (to.name === "Category") {
        this.getCategory();
      }
    },
  },

  methods: {
    async getCategory() {
      const categorySlug = this.$route.params.category_slug;

      this.$store.commit("setIsLoading", true);

      const response = await axios.get(`/api/v1/products/${categorySlug}`);

      this.category = response.data;
      document.title = this.category.name + " | Djackets";

      this.$store.commit("setIsLoading", false);
    },
  },
});
</script>

<style scoped>
</style>