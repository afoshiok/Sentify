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
                        <input type="radio" name="Seed-Option" class="radio checked:bg-black" checked />
                        </label>
                    </div>
                    <div class="form-control">
                        <label class="label cursor-pointer">
                            <span class="label-text">Tracks</span> 
                            <input type="radio" name="Seed-Option" class="radio checked:bg-black" checked />
                        </label>
                    </div>
                </div>

                <!-- Select for Seed time range -->
                <div class="flex flex-col justify-center items-center">
                    <select class="bg-white select select-bordered w-3/4 max-w-xs">
                        <option disabled selected>Choose time range for seeds</option>
                        <option>Short</option>
                        <option>Medium</option>
                        <option>Long</option>
                    </select>
                    <button>Preview</button>
                </div>
                
            </div> 
        </section>
        <div class="mt-10 flex justify-center">
            <button class="bg-white rounded-lg h-14 w-72 flex flex-row justify-center items-center outline-4 outline-dashed">
                <span class="text-lg">Generate {{song_num}} playlist!</span>
            </button>
        </div>
    </section>
</template>

<script lang="ts">
    import { ref } from 'vue';

    export default {
        setup(){
            let song_num = ref(10)
            return {
                song_num
            }
        }
    }
    
</script>