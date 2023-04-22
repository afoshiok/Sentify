import { createApp } from 'vue'
import { createPinia } from 'pinia'
import './style.css'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import login from './components/Login.vue'
import playlist from './components/Playlist.vue'
import error from './components/Error.vue'

import "@fontsource/ibm-plex-mono"
import "@fontsource/jetbrains-mono"

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {path: '/', name: 'Hello', component: login},
        {path: '/playlist', name:'Playlist', component: playlist},
        {path: '/error', name:'Error', component: error}
    ]
})

createApp(App)
.use(router)
.use(createPinia())
.mount('#app')
