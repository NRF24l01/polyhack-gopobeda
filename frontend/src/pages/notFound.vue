<!-- src/views/NotFound.vue -->
<template>
  <div class="flex items-center justify-center min-h-screen">
    <div class="max-w-7xl px-4 sm:px-6 lg:px-8 text-center">
      <transition name="slide-up" appear>
        <h1 class="text-4xl font-bold mb-4">404</h1>
      </transition>

      <transition name="slide-up" appear>
        <div class="text-gray-600 mb-8">
          <p>Страница не найдена.</p>
          <router-link to="/" class="text-blue-500 hover:underline"
            >На главную</router-link
          >
        </div>
      </transition>
    </div>
  </div>
</template>
