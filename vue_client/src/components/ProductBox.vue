<template>
  <div class="w-1/4 my-6 mx-12">
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
      <a :href="product.get_absolute_url">
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
        <p class="font-bold text-1xl my-1 text-gray-900">
          price : <span class="text-blue-500">${{ product.price }}</span>
        </p>
        <router-link :to="product.get_absolute_url">
          <button
            class="
              bg-blue-400
              hover:bg-blue-500
              text-white
              font-bold
              py-2
              px-4
              mt-4
              rounded
            "
          >
            View details
          </button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProductBox",
  props: {
    product: Object,
  },
};
</script>