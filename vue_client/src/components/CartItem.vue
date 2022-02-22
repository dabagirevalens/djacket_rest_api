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
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="inline-flex w-6 h-6 text-red-600"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M15 12H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
        </button>
        <input
          type="text"
          name="qty"
          value="1"
          class="w-12 text-center bg-gray-100 outline-none"
        />
        <button>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="inline-flex w-6 h-6 text-green-600"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M12 9v3m0 0v3m0-3h3m-3 0H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"
            />
          </svg>
        </button>
      </div>
    </td>
    <td class="p-4 px-6 text-center whitespace-nowrap">
      ${{ getItemTotal(item) }}
    </td>
    <td class="p-4 px-6 text-center whitespace-nowrap">
      <button>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="w-6 h-6 text-red-400"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
          />
        </svg>
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
      return this.item.quantity * this.item.product.price;
    },
  },
});
</script>

<style scoped>
</style>