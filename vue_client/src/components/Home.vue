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
      <div class="products flex flex-wrap justify-between">
        <div class="w-1/4 m-6" v-for="product in latestProducts" :key="product.id">
          <div
            class="
              max-w-sm
              bg-white
              rounded-lg
              border border-gray-200
              shadow-md
              dark:bg-gray-100 dark:border-gray-100
            "
          >
            <a href="#">
              <img
                class="rounded-t-lg h-80 w-full"
                :src="product.get_image"
                alt="product.name"
              />
            </a>
            <div class="p-5">
              <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900">
                {{ product.name }}
              </h5>
              <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
                {{ product.description }}
              </p>

              <p class="font-bold text-3xl my-1 text-gray-900">
                price : ${{ product.price }}
              </p>
              <a
                href="#"
                class="
                  inline-flex
                  items-center
                  py-2
                  px-3
                  text-sm
                  font-medium
                  text-center text-white
                  bg-blue-700
                  rounded-lg
                  hover:bg-blue-800
                  focus:ring-4 focus:ring-blue-300
                  dark:bg-blue-600
                  dark:hover:bg-blue-700
                  dark:focus:ring-blue-800
                "
              >
                Read more
                <svg
                  class="ml-2 -mr-1 w-4 h-4"
                  fill="currentColor"
                  viewBox="0 0 20 20"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    fill-rule="evenodd"
                    d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                    clip-rule="evenodd"
                  ></path>
                </svg>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import axios from "axios";

import { defineComponent } from "vue";

export default defineComponent({
  name: "HomeComponent",
  data() {
    return {
      latestProducts: [],
    };
  },
  components: {},
  mounted() {
    this.getLatestProducts();
  },

  methods: {
    async getLatestProducts() {
      const response = await axios.get("/api/v1/latest-products/");
      this.latestProducts = response.data;
    },
  },
});
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
</style>
