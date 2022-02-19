<template>
    <WinterJackets />
</template>

<script lang="ts">
import { defineComponent } from 'vue'

import WinterJackets from '../components/WinterJackets.vue'

export default defineComponent({
   name : 'WinterJacketsView',
   components :{
       WinterJackets
   }
})
</script>

<style scoped>

</style>