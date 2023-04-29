<template>
    <section class="flex flex-col justify-center align-center min-h-screen">
        <section>
            <div class="flex justify-center">
                <textarea v-model="textbox" class="border-4 border-black px-2 pt-1 m-2 rounded-md w-3/4 placeholder-gray-600" type="text" placeholder="You feeling sad, happy...meh? Let me know!"></textarea>
            </div>
            <div class="my-8">
                <label class="px-1">Number of songs</label>
                <input v-model="song_num" type="range" min="10" max="100" class="range range-primary" step="10"/>
            </div>

            <!-- Radio buttons for Seed preference -->
            <h1 class="text-xl mb-2">Seeds</h1>
            <div class="grid grid-cols-2">
                <div class="pr-8">
                    <div class="form-control">
                        <label class="label cursor-pointer">
                        <span class="label-text">Artist</span> 
                        <input v-model="seed_choice" type="radio" name="Seed-Option" value="artists" class="radio checked:bg-black" checked/>
                        </label>
                    </div>
                    <div class="form-control">
                        <label class="label cursor-pointer">
                            <span class="label-text">Tracks</span> 
                            <input v-model="seed_choice" type="radio" name="Seed-Option" value="tracks" class="radio checked:bg-black"/>
                        </label>
                    </div>
                </div>

                <!-- Select for Seed time range -->
                <div class="flex flex-col justify-center items-center">
                    <select v-model="range" class="bg-white select select-bordered w-3/4 max-w-xs">
                        <option value="" disabled selected>Choose time range for seeds</option>
                        <option value="short_term">Short</option>
                        <option value="medium_term">Medium</option>
                        <option value="long_term">Long</option>
                    </select>
                    <button @click="tops(seed_choice, range)" class="hover:underline decoration-2 underline-offset-4">Preview</button>
                </div>
            </div> 
        </section>

        <!-- Renders preview of artist seeds -->
        <div v-if="!!preview_data" class="py-4 flex justify-center">
            <h1>Your top: {{ seed_choice }}</h1>
        </div>
        <ul v-if="!!preview_data && seed_choice == 'artists'" class="flex flex-row pt-8 overflow-x-scroll scrollbar scrollbar-thumb-primary">
            <li v-for="(item,index) in preview_data" class="px-2 pb-6">
                <div class="border-4 border-black card w-72 bg-base-100">
                    <figure class="px-4 pt-6">
                        <img v-bind:src="preview_data[index].Photo" alt="Album/Arstist Cover" width="300" height="300" class="rounded-md">
                    </figure>
                    <div class="card-body items-center text-center">
                        <h2 class="card-title">{{ preview_data[index].Name }}</h2>
                        <p>{{ preview_data[index].Genres }}</p>
                        <div class="card-actions">
                            <p>Popularity Score: {{ preview_data[index].Popularity }}</p>
                        </div>
                    </div>
                </div>
            </li>
        </ul>
        <div v-else></div>

        <!-- Renders preview of tracks seeds -->
        <ul v-if="!!preview_data && seed_choice == 'tracks'" class="flex flex-row pt-10 overflow-x-scroll scrollbar scrollbar-thumb-primary" >
            <li v-for="(item,index) in preview_data" class="px-2 pb-6">
                <div class="border-4 border-black card w-72 bg-base-100">
                    <figure class="px-4 pt-6">
                        <img v-bind:src="preview_data[index].Cover.url" alt="Album/Arstist Cover" width="300" height="300" class="rounded-md">
                    </figure>
                    <div class="card-body items-center text-center">
                        <h2 class="card-title">{{ preview_data[index].Name }}</h2>
                        <div v-for="item in preview_data[index].Artists">
                            <h3>{{ item }}</h3>
                        </div>
                        <p>{{ preview_data[index].Genres }}</p>
                        <div class="card-actions">
                            <p>Popularity Score: {{ preview_data[index].Popularity }}</p>
                        </div>
                    </div>
                </div>
            </li>
        </ul>
        <div v-else></div>

        <div class="mt-10 flex justify-center">
            <button @click="recommendations()" class="bg-white rounded-lg h-14 w-72 p-2 flex flex-row justify-center items-center outline-4 outline-dashed">
                <h1 class="text-md">Generate a {{song_num}} song playlist!</h1>
            </button>
        </div>
    </section>
</template>

<script setup lang="ts">
    import { ref, reactive, watch } from 'vue';
    import axios from 'axios'
    import { useResultStore } from '../stores/loginStore';
    import { useRouter }from 'vue-router'
    const router = useRouter()

    let axiosConfig = {
        headers: {
            'Content-Type': 'application/json;charset=UTF-8',
            "Access-Control-Allow-Origin": "*",
        }
    };



    //State
    let song_num = ref(10)
    let range = ref('')
    let seed_choice = ref('artists')
    let preview_data = ref()
    let textbox = ref('')
    const resultStore = useResultStore()


    //Methods
    function tops(seed: string, range: string){
        axios.get(import.meta.env.VITE_API_BASE_URL + `/tops/${seed}/${range}`)
        .then((response) => {
            console.log(response.data)
            preview_data.value = response.data
        })
        .catch((error) =>{
            console.log(error)
        })
    }

    function recommendations(){
        axios.post(import.meta.env.VITE_API_BASE_URL + '/recommendations', {
        type: seed_choice.value,
        term: range.value,
        songs: song_num.value,
        sentence: textbox.value
        }, axiosConfig)
        .then((response) =>{
            console.log(response)
            resultStore.$patch({result: response.data})
            router.push({name: 'Result'})
        })
        .catch((error) => {
            console.log(error)
        })
    }

    //Debugging
    // watch(range, () => console.log(`${range.value}`) )
    // watch(seed_choice, () => console.log(`${seed_choice.value}`) )
    // watch(preview_data, () => console.log(`${preview_data.value}`))
    // watch(body, () => console.log(`${body}`))

    
</script>