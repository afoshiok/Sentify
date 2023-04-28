<template>
  <body class="container mx-auto max-w-6xl">
    <header class="flex my-6 mx-4">
      <h1 class="flex-auto text-4xl text-bold" id="Title">Sentify</h1>
      <div class="flex flex-row">
        <a href="https://github.com/afoshiok/Perfect-Spotify-Playlist">
          <svg fill="currentColor" stroke-width="0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" height="2.5em" width="2.5em" style="overflow: visible;"><path fill="currentColor" d="M8 .198a8 8 0 00-2.529 15.591c.4.074.547-.174.547-.385 0-.191-.008-.821-.011-1.489-2.226.484-2.695-.944-2.695-.944-.364-.925-.888-1.171-.888-1.171-.726-.497.055-.486.055-.486.803.056 1.226.824 1.226.824.714 1.223 1.872.869 2.328.665.072-.517.279-.87.508-1.07-1.777-.202-3.645-.888-3.645-3.954 0-.873.313-1.587.824-2.147-.083-.202-.357-1.015.077-2.117 0 0 .672-.215 2.201.82A7.672 7.672 0 018 4.066c.68.003 1.365.092 2.004.269 1.527-1.035 2.198-.82 2.198-.82.435 1.102.162 1.916.079 2.117.513.56.823 1.274.823 2.147 0 3.073-1.872 3.749-3.653 3.947.287.248.543.735.543 1.481 0 1.07-.009 1.932-.009 2.195 0 .213.144.462.55.384A8 8 0 008.001.196z"></path></svg>
        </a>
        <router-link to="/about" class="flex justify-center"><a class="py-2 px-8 text-lg hover:underline decoration-2 underline-offset-4">About</a></router-link> 
      </div> 
    </header>
    <main>
      <router-view></router-view>
    </main>
  </body>
</template>


