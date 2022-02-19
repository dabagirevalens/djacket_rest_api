<template>
    <SummerJackets />
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import SummerJackets from '../components/SummerJackets.vue'


export default defineComponent({
    name: 'SummerJacketsView',
    components :{
        SummerJackets
    }
})
</script>

<style scoped>

</style>