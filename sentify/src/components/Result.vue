<template>
    <h1> {{ resultObj }} </h1>
    <button class="mt-4 bg-white rounded-lg h-14 w-72 p-2 flex flex-row justify-center items-center outline-4 outline-dashed"> Show me the playlist! </button>
</template>

<script setup lang="ts">
import { ref, onBeforeMount } from 'vue';
import { useResultStore } from '../stores/loginStore';
const resultObj = ref()
const resultStore = useResultStore()
const playlistLink = ref('')


onBeforeMount(() => {
    resultObj.value = resultStore.result
    playlistLink.value = resultStore.result.links
})
</script>