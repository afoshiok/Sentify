import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import login from './components/Login.vue'

import "@fontsource/ibm-plex-mono"
import "@fontsource/jetbrains-mono"

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {path: '/', name: 'Hello', component: login}
    ]
})

createApp(App)
.use(router)
.mount('#app')
