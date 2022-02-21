<template>
  <nav class="bg-gray-900 py-4 text-white flex items-center justify-around">
    <div class="nav-brand mx-24">
      <router-link to="/"><strong>Djackets</strong></router-link>
    </div>
    <form class="flex items-center" action="/search">
      <input
        type="text"
        class="
          block
          p-2
          pl-6
          w-80
          text-gray-900
          bg-white-500
          rounded-tl rounded-bl
          border-0
        "
        placeholder="What are you looking for?"
        name="query"
      />
      <button class="bg-gray-500 p-2 rounded-tr rounded-br">
        <i class="bx bx-search-alt"></i>
      </button>
    </form>
    <div class="nav-menu flex items-center justify-between mx-24">
      <div class="nav-links">
        <router-link to="/summer" class="link hover:text-gray-200 items-center"
          ><i class="bx bx-sun mr-2"></i>Summer</router-link
        >
        <router-link to="/winter" class="link hover:text-gray-200"
          ><i class="bx bx-cloud-rain mr-2"></i>Winter</router-link
        >
        <router-link to="/cart" class="link hover:text-gray-200"
          ><i class="bx bx-cart mr-2"></i>Cart
          <span class="font-bold text-sky-300 absolute -mt-2"
            >{{ cartTotalLength > 0 ? cartTotalLength : "" }}
          </span></router-link
        >
      </div>
      <div class="buttons">
        <button
          class="
            bg-blue-500
            hover:bg-blue-700
            text-white
            font-bold
            py-2
            px-4
            rounded
            ml-6
          "
        >
          login
        </button>
      </div>
    </div>
  </nav>
</template>

<script lang='ts'>
export default {
  name: "NavBar",
  props: {
    cartTotalLength: Number,
  },
};
</script>

<style lang="scss" scoped>
.link {
  margin: 0 24px;
}
</style>