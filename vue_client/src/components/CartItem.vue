<template>
  <tr>
    <td>
      <div class="flex justify-center">
        <router-link :to="item.product.get_absolute_url">
          <img
            :src="item.product.get_image"
            class="object-cover h-24 w-24 rounded-2xl mt-4"
            :alt="item.product.name"
          />
        </router-link>
      </div>
    </td>
    <td class="p-4 px-6 text-center whitespace-nowrap">
      <router-link :to="item.product.get_absolute_url">{{
        item.product.name
      }}</router-link>
    </td>
    <td class="p-4 px-6 text-center whitespace-nowrap">
      <div>
        <button>
          <i
            class="bx bx-minus bg-red-600 text-white rounded-full"
            @click="decrementQuantity(item)"
          ></i>
        </button>
        <input
          type="text"
          name="qty"
          :value="item.quantity"
          class="w-12 text-center bg-gray-100 outline-none mx-1 rounded"
        />
        <button>
          <i
            class="bx bx-plus bg-green-600 text-white rounded-full"
            @click="incrementQuantity(item)"
          ></i>
        </button>
      </div>
    </td>
    <td class="p-4 px-6 text-center whitespace-nowrap">
      ${{ getItemTotal(item).toFixed(2) }}
    </td>
    <td class="p-4 px-6 text-center whitespace-nowrap">
      <button>
        <i
          class="bx bx-trash text-red-400 text-2xl"
          @click="removeItem(item)"
        ></i>
      </button>
    </td>
  </tr>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "CartItem",
  props: {
    initialItem: Object,
  },
  data() {
    return {
      item: this.initialItem,
    };
  },

  methods: {
    getItemTotal() {
      return this.item?.quantity * this.item?.product.price;
    },

    decrementQuantity(item: { quantity: number }) {
      item.quantity -= 1;

      if (item.quantity === 0) {
        this.$emit("removeFromCart", item);
      }

      this.updateCart();
    },

    incrementQuantity(item: { quantity: number }) {
      item.quantity += 1;
      this.updateCart();
    },

    removeItem(item: unknown) {
      this.$emit("removeFromCart", item);
      this.updateCart();
    },

    updateCart() {
      localStorage.setItem("cart", JSON.stringify(this.$store.state.cart));
    },
  },
});
</script>

<style scoped>
</style>