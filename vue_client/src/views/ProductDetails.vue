<template>
  <div
    class="
      product-page
      p-24
      grid grid-cols-3
      justify-items-center
      items-center
      gap-4
    "
  >
    <div class="content w-1/2">
      <img
        class="rounded-t-lg h-80 w-full"
        :src="product.get_image"
        alt="product.name"
      />
    </div>
    <div class="information">
      <h2 class="font-bold my-2">Information</h2>
      <div class="description">
        <h1 class="font-bold text-blue-500">{{ product.name }}</h1>
        <p>{{ product.description }}</p>
      </div>
      <p class="my-2">
        <strong>Price : </strong>
        <span class="text-blue-900 font-bold"> ${{ product.price }}</span>
      </p>

      <div class="add-to-cart-controls flex justify-between">
        <div class="control">
          <input
            type="number"
            name="number"
            min="1"
            v-model="quantity"
            class="
              shadow
              appearance-none
              border
              rounded
              w-full
              py-2
              px-3
              text-gray-700
              leading-tight
              focus:outline-none focus:shadow-outline
            "
          />
        </div>
        <div class="control">
          <button
            class="
              bg-blue-400
              hover:bg-blue-500
              text-white
              font-bold
              py-2
              px-4
              rounded
            "
            @click="addToCart"
          >
            Add to cart
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import axios from "axios";
import { defineComponent } from "vue";

export default defineComponent({
  name: "ProductDetails",
  data() {
    return {
      quantity: 1,
      product: {},
    };
  },

  mounted() {
    this.getProduct();
  },

  methods: {
    async getProduct() {
      const category_slug = this.$route.params.category_slug;
      const product_slug = this.$route.params.product_slug;

      const response = await axios.get(
        `/api/v1/products/${category_slug}/${product_slug}`
      );

      this.product = response.data;
    },

    addToCart() {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1;
      }

      const item = {
        product: this.product,
        quantity: this.quantity,
      };

      this.$store.commit("addToCart", item);
    },
  },
});
</script>

<style scoped>
</style>