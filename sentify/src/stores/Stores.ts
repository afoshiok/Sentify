import { defineStore } from "pinia";
import { ref } from "vue";

export const useLoginStore = defineStore('login', () => {
    const user = ref('')

    return {user}
})

export const useResultStore = defineStore('result', () => {
    const result = ref('')

    return {result}
} )