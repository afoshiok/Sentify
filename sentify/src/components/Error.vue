<template>
    <div class="flex flex-col justify-center min-h-screen">
        <div class="flex flex-row justify-center">
            <svg fill="currentColor" stroke-width="0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" height="15em" width="15em" style="overflow: visible;"><path d="M20 2H4c-1.103 0-2 .897-2 2v12c0 1.103.897 2 2 2h3v3.767L13.277 18H20c1.103 0 2-.897 2-2V4c0-1.103-.897-2-2-2zm0 14h-7.277L9 18.233V16H4V4h16v12z"></path><path d="M11 6h2v5h-2zm0 6h2v2h-2z"></path></svg>
            <div>
                <h1>Something went wrong...</h1>
                <RouterLink to="/"><h1 class="mt-4 hover:underline underline-offset-4">Back to home page</h1></RouterLink>
            </div>
        </div>
    </div>
</template>