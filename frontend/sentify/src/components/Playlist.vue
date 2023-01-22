<template>
    <section class="flex flex-col justify-center items-center align-center min-h-[92vh]">
        <form class="">
            <div>
                <textarea class="border-4 border-black px-2 m-2 rounded-md w-96" type="text" placeholder="Say anything..."></textarea>
            </div>
            <div class="mx-4">
                <label class="px-1">Number of songs</label>
                <input type="range" min="0" max="100" value="25" class="range range-primary" step="25"/>
            </div>
            
        </form>
    </section>
</template>