<template>
    <header class="container mx-auto max-w-6xl flex justify-center">
        <h1 class="text-3xl">About</h1>
    </header>
    <p class="mt-4 mx-4">
        Sentify is a playlist generator that utilizes <a href="https://aws.amazon.com/what-is/sentiment-analysis/#:~:text=Sentiment%20analysis%20is%20the%20process,social%20media%20comments%2C%20and%20reviews." target="_blank" rel="noopener noreferrer" class="font-semibold hover:underline underline-offset-2">sentiment analysis</a>.
        You can generate playlist of up to 100 songs based on the polarity of a text input. With the help of Spotfiy's API, Sentify tailors your playist based on your music taste, through seeds, at a given time range. The API then uses text input's polarity as a <a class="font-semibold">target valence</a> target valence to filter songs by.
    </p>
    <section class="mt-4 mb-2 mx-4">
        <h1> What is Valence? </h1>
        <p>Each song on Spotify can be analyzed by <a href="https://developer.spotify.com/documentation/web-api/reference/get-recommendations" target="_blank" rel="noopener noreferrer" class="font-semibold hover:underline underline-offset-2">13 features</a>, one of them being valence. Valence is a value from 0 to 1 that determines the "emotion" of a song. Songs with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry), according to the Spotify API Developer Guide. </p>
    </section>
    <section class="mt-4 mb-2 mx-4">
        <h1> What is a Seed? </h1>
        <p>A seed is what Spotify's recommendation API endpoint will base your playlist recommendations on. Sentify gives you the option to base you playlist on either your top five tracks or artists. </p>
    </section>
    <section class="mt-4 mx-4">
        <h1 class="mb-1">Time Ranges</h1>
        <p><a class="underline underline-offset-4">Short Term:</a> Range of 4 weeks. (Personally, I've got the best playlists with this time range.) </p>
        <p><a class="underline underline-offset-4">Medium Term:</a> Range of 6 months. </p>
        <p><a class="underline underline-offset-4">Long Term:</a> Range of several years. </p>
    </section>
    <section class="container mx-auto max-w-6xl flex justify-center mt-4">
        <h1 class="mb-1">Created by</h1>
    </section>
    <footer class="container mx-auto max-w-6xl flex justify-center mt-[2px]">
        <h2>Favour Oshiokhale</h2>
    </footer>
    <footer class="container mx-auto max-w-6xl flex justify-center mt-[2px] text-sm">
        <div class="flex flex-row">
            <a href="mailto:afoshiokhale@gmail.com" target="_blank" rel="noopener noreferrer" class="font-semibold underline underline-offset-1">afoshiokhale@gmail.com</a>
            <div class="mx-2">|</div>
            <a href="https://www.linkedin.com/in/favour-oshio/" target="_blank" rel="noopener noreferrer" class="font-semibold underline underline-offset-1">LinkedIn</a>
            <div class="mx-2">|</div>
            <a href="https://github.com/afoshiok" target="_blank" rel="noopener noreferrer" class="font-semibold underline underline-offset-1">Github</a>
        </div>
    </footer>
</template>