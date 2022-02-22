<template>
  <div class="container p-8 mx-auto mt-12">
    <div class="w-full overflow-x-auto">
      <div class="my-2">
        <h3 class="text-xl my-2 font-bold tracking-wider">Shopping Cart</h3>
      </div>
      <table class="w-full shadow-inner" v-if="cartTotalLength">
        <thead>
          <tr class="bg-gray-100">
            <th class="px-6 py-3 font-bold whitespace-nowrap">Image</th>
            <th class="px-6 py-3 font-bold whitespace-nowrap">Product</th>
            <th class="px-6 py-3 font-bold whitespace-nowrap">Quantity</th>
            <th class="px-6 py-3 font-bold whitespace-nowrap">Price</th>
            <th class="px-6 py-3 font-bold whitespace-nowrap">Remove</th>
          </tr>
        </thead>
        <tbody>
          <CartItem
            v-for="item in cart.items"
            :initialItem="item"
            :key="item.id"
          />
        </tbody>
      </table>
      <p v-else class="text-center my-4 text-3xl">
        You have no products in your cart!!
      </p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import CartItem from "../components/CartItem.vue";

export default defineComponent({
  name: "CartView",

  components: {
    CartItem,
  },

  data :() => {
    return {
      cart: {
        items: [],
      },
    };
  },

  mounted() {
    this.cart = this.$store.state.cart;
  },

  computed: {
    cartTotalLength() {
      return this.cart.items.reduce((acc: number, curVal: { quantity: number; }) => {
        return (acc += curVal.quantity);
      }, 0);
    },
  },
});
</script>

<style scoped>
</style>