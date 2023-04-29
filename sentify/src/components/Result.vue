<template>
    <h1> {{ resultObj }} </h1>
    <button class="mt-4"></button>
</template>

<script setup lang="ts">
import { ref, onBeforeMount } from 'vue';
import { useResultStore } from '../stores/loginStore';
const resultObj = ref()
const resultStore = useResultStore()

onBeforeMount(() => {
    resultObj.value = resultStore
})
</script>