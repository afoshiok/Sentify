<template>
    <section class="flex flex-col justify-center align-center min-h-screen">
        <section>
            <div class="flex justify-center">
                <textarea class="border-4 border-black px-2 m-2 rounded-md w-3/4" type="text" placeholder="Say anything..."></textarea>
            </div>
            <div class="mb-8">
                <label class="px-1">Number of songs</label>
                <input v-model="song_num" type="range" min="0" max="100" class="range range-primary" step="10"/>
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
                    <button @click="tops(seed_choice, range)">Preview</button>
                </div>
                
            </div> 
        </section>

        <!-- Renders preview of seeds -->
        <div v-if="!!preview_data && seed_choice == 'artists'" class="card w-72 bg-base-100">
            <figure class="px-4 pt-6">
                <img v-bind:src="preview_data[0].Photo" alt="Album/Arstist Cover" width="300" height="300" class="rounded-md">
            </figure>
            <div class="card-body items-center text-center">
                <h2 class="card-title">{{ preview_data[0].Name }}</h2>
                <p>{{ preview_data[0].Genres }}</p>
                <div class="card-actions">
                    <p>Popularity Score: {{ preview_data[0].Popularity }}</p>
                </div>
            </div>
        </div>
        <div v-else></div>


        <div class="mt-10 flex justify-center">
            <button class="bg-white rounded-lg h-14 w-72 flex flex-row justify-center items-center outline-4 outline-dashed">
                <span class="text-lg">Generate {{song_num}} song playlist!</span>
            </button>
        </div>
    </section>
</template>

<script setup lang="ts">
    import { ref, reactive, watch } from 'vue';
    import axios from 'axios'

    //State
    let song_num = ref(10)
    let range = ref('')
    let seed_choice = ref('artists')
    let preview_data = ref()

    //Methods
    function tops(seed: string, range: string){
        axios.get(`http://localhost:5000/tops/${seed}/${range}`)
        .then((response) => {
            console.log(response.data)
            preview_data.value = response.data
        })
        .catch((error) =>{
            console.log(error)
        })
    }
    //Debugging
    // watch(range, () => console.log(`${range.value}`) )
    // watch(seed_choice, () => console.log(`${seed_choice.value}`) )
    watch(preview_data, () => console.log(`${preview_data.value}`))

    
</script>