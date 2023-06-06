<template>
    <!-- <h1> {{ linkStore.link }} </h1>
    <h1>{{ resultStore.pos }}</h1> -->

    <section class="flex flex-col items-center justify-center min-h-screen">
        <h1 class="mb-4 text-5xl">POLARITY SCORES:</h1>
        <div class="grid grid-cols-4 space-x-4 h-52 min-w-full  max-lg:h-48 max-lg:flex max-lg:flex-wrap max-lg:items-center max-lg:justify-center max-lg:my-6 max-lg:mx-auto">
            <card class="border-4 border-black card bg-base-100 flex items-center justify-center max-lg:h-1/2 max-lg:m-2">
                <!-- POSITIVE POLARITY SCORE -->
                <h1 class="text-6xl max-lg:text-xl">{{ resultStore.pos }}</h1>
                <label class="max-lg:w-1/2">POSITIVE SCORE</label>
            </card>

            <card class="border-4 border-black card bg-base-100 flex items-center justify-center max-lg:h-1/2 max-lg:m-2">
                <!-- NEUTRAL POLARITY SCORE -->
                <h1 class="text-6xl max-lg:text-xl">{{ resultStore.neu }}</h1>
                <label class="max-lg:w-1/2">NEUTRAL SCORE</label>
            </card>

            <card class="border-4 border-black card bg-base-100 flex items-center justify-center max-lg:h-1/2 max-lg:m-2">
                <!-- NEGATIVE POLARITY SCORE -->
                <h1 class="text-6xl max-lg:text-xl">{{ resultStore.neg }}</h1>
                <label class="max-lg:w-1/2">NEGATIVE SCORE</label>
            </card>

            <card class="border-4 border-black card bg-base-100 flex items-center justify-center max-lg:h-1/2 max-lg:m-2">
                <!-- COMPOUND POLARITY SCORE -->
                <h1 class="text-6xl max-lg:text-xl">{{ resultStore.comp }}</h1>
                <label class="max-lg:w-1/2">COMPOUND SCORE</label>
            </card>
        </div>
        <button class="mt-4 bg-white rounded-lg h-14 w-72 p-2 flex flex-row justify-center items-center outline-4 outline-dashed"> <a :href="linkStore.link" target="_blank" rel="noopener noreferrer">Show me the playlist! </a></button>
        <a class="font-bold mt-4"><router-link to="/Playlist">Generate another one.</router-link></a>
        <p class="mx-auto px-4 mt-4"><strong class="font-bold">*Note:</strong>The playlist generated will be a public playlist, be sure to make it private if you want. </p>
    </section>
    
</template>

<script setup lang="ts">
import { ref, onBeforeMount } from 'vue';
import { useLinkStore, useResultStore } from '../stores/Stores';
const linkStore = useLinkStore()
const resultStore = useResultStore()
</script>