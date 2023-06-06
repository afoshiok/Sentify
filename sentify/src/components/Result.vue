<template>
    <!-- <h1> {{ linkStore.link }} </h1>
    <h1>{{ resultStore.pos }}</h1> -->

    <section class="flex flex-col items-center justify-center min-h-screen">
        <h1 class="mb-4 text-5xl">POLARITY SCORES:</h1>
        <div class="grid grid-cols-4 space-x-4 h-52 min-w-full">
            <card class="border-4 border-black card bg-base-100 flex items-center justify-center">
                <!-- POSITIVE POLARITY SCORE -->
                <h1 class="text-6xl">{{ resultStore.pos }}</h1>
                <label>POSITIVE SCORE</label>
            </card>

            <card class="border-4 border-black card bg-base-100 flex items-center justify-center">
                <!-- NEUTRAL POLARITY SCORE -->
                <h1 class="text-6xl">{{ resultStore.neu }}</h1>
                <label>NEUTRAL SCORE</label>
            </card>

            <card class="border-4 border-black card bg-base-100 flex items-center justify-center">
                <!-- NEGATIVE POLARITY SCORE -->
                <h1 class="text-6xl">{{ resultStore.neg }}</h1>
                <label>NEGATIVE SCORE</label>
            </card>

            <card class="border-4 border-black card bg-base-100 flex items-center justify-center">
                <!-- COMPOUND POLARITY SCORE -->
                <h1 class="text-6xl">{{ resultStore.comp }}</h1>
                <label>COMPOUND SCORE</label>
            </card>
        </div>
        <button class="mt-4 bg-white rounded-lg h-14 w-72 p-2 flex flex-row justify-center items-center outline-4 outline-dashed"> Show me the playlist! </button>
    </section>
    
</template>

<script setup lang="ts">
import { ref, onBeforeMount } from 'vue';
import { useLinkStore, useResultStore } from '../stores/Stores';
const linkStore = useLinkStore()
const resultStore = useResultStore()
</script>