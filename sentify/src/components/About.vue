<template>
    <header class="container mx-auto max-w-6xl flex justify-center">
        <h1 class="text-xl">About</h1>
    </header>
    <p class="mt-4 mx-4">
        Sentify is a playlist generator that utilizes <a href="https://aws.amazon.com/what-is/sentiment-analysis/#:~:text=Sentiment%20analysis%20is%20the%20process,social%20media%20comments%2C%20and%20reviews." class="font-semibold hover:underline underline-offset-2">sentiment analysis</a>.
        You can generate playlist of up to 100 songs based on the "polarity" of a text input. With the help of Spotfiy's API, Sentify tailors your playist based on your music taste at a given time range.  
    </p>
    <section class="mt-4 mb-2 mx-4">
        <h1> What is a Seed? </h1>
        <p>A seed is what Spotify's recommendation API endpoint will base your playlist recommendations on. Sentify gives you the option to base you playlist on either your top five tracks or artists. </p>
    </section>
    <section class="mt-4 mx-4">
        <h1 class="mb-1">Time Ranges</h1>
        <p>Short Term: Range of 4 weeks. </p>
        <p>Medium Term: Range of 6 months. </p>
        <p>Long Term: Range of several years. </p>
    </section>
</template>