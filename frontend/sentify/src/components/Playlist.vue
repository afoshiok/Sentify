<template>
    <section class="flex flex-col justify-center items-center align-center min-h-screen">
        <form class="">
            <div>
                <textarea class="border-4 border-black px-2 m-2 rounded-md w-96" type="text" placeholder="Say anything..."></textarea>
            </div>
            <div class="mb-8">
                <label class="px-1">Number of songs</label>
                <input type="range" min="0" max="100" value="10" class="range range-primary" step="10"/>
            </div>
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
                <select class="select select-bordered w-3/4 max-w-xs">
                    <option disabled selected>Choose time range for seeds</option>
                    <option>Short</option>
                    <option>Medium</option>
                    <option>Long</option>
                </select>
            </div>
            
        </form>
    </section>
</template>