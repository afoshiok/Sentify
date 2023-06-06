import { defineStore } from "pinia";
import { ref } from "vue";

export const useLoginStore = defineStore('login', () => {
    const user = ref('')

    return {user}
})

export const useLinkStore = defineStore('link', () => {
    const link = ref('')

    return {link}
} )

export const useResultStore = defineStore('result', () => {
    const neg = ref(0)
    const pos = ref(0)
    const neu = ref(0)
    const comp = ref(0)

    return {neg, pos, neu, comp}
} )