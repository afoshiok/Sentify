<template>
    <section class="flex flex-col justify-center items-center align-center min-h-[92vh] max-h-[92svh]" id="login_btn">
        <p class="pb-6 font-semibold text-lg">Your new playlist awaits😉</p>
        <button class="bg-white rounded-lg h-14 w-28 flex flex-row justify-center items-center outline-4 outline-dashed" @click="startAuthorization()">
            <span class="text-lg">Login</span>
            <svg class="py-1.5" fill="currentColor" stroke-width="0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" height="2.5em" width="2.5em" style="overflow: visible;"><path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.66 0 12 0zm5.521 17.34c-.24.359-.66.48-1.021.24-2.82-1.74-6.36-2.101-10.561-1.141-.418.122-.779-.179-.899-.539-.12-.421.18-.78.54-.9 4.56-1.021 8.52-.6 11.64 1.32.42.18.479.659.301 1.02zm1.44-3.3c-.301.42-.841.6-1.262.3-3.239-1.98-8.159-2.58-11.939-1.38-.479.12-1.02-.12-1.14-.6-.12-.48.12-1.021.6-1.141C9.6 9.9 15 10.561 18.72 12.84c.361.181.54.78.241 1.2zm.12-3.36C15.24 8.4 8.82 8.16 5.16 9.301c-.6.179-1.2-.181-1.38-.721-.18-.601.18-1.2.72-1.381 4.26-1.26 11.28-1.02 15.721 1.621.539.3.719 1.02.419 1.56-.299.421-1.02.599-1.559.3z"></path></svg>
        </button>
    </section>
</template>
<script lang="ts" setup>
    import axios from 'axios'
    import { useLoginStore } from '../stores/Stores';
    import { useRouter} from 'vue-router'

    const store = useLoginStore()
    const router = useRouter()

    let axiosConfig = {
        headers: {
            'Content-Type': 'application/json;charset=UTF-8',
            "Access-Control-Allow-Origin": "*",
        }
    };

    function user_login(){
        axios.get(`http://localhost:5000/auth/login`)
        .then((response) => {
            console.log(response.data)
            store.$patch({
                user: response.data.current_user
            })
            router.push({name: 'Playlist'})
        })
        // .then(() => {
        //     //FIXME: RUNNING INTO ERRORS HERE, REFER TO LAST CHATGPT SOLUTION. Hint: follow this guide - https://developer.spotify.com/documentation/web-api/tutorials/code-flow
        //     axios.get(store.user)
        // })
        .catch((error) =>{
            console.log(error)
            router.push({name: 'Error'})
        })
    }

    async function startAuthorization() {
        user_login()
    }

</script>