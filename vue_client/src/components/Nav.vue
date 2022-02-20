<template>
  <nav
    class="bg-gray-900 py-4  text-white flex items-center justify-around"
  >
    <div class="nav-brand mx-24">
      <router-link to="/"><strong>Djackets</strong></router-link>
    </div>
    <div class="nav-menu flex items-center justify-between mx-24" >
      <div class="nav-links">
        <router-link to="/summer" class="link">Summer</router-link>
        <router-link to="/winter" class="link">Winter</router-link>
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
          "
        >
          login
        </button>
      </div>
    </div>
  </nav>
</template>

<script lang='ts'>
 export default{
   name: "NavBar",
 }
</script>

<style lang="scss" scoped>
    .link{
        margin: 0 24px;
    }
</style>