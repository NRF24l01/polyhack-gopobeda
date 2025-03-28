<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 text-center">
    <transition name="slide-up" appear>
      <h1 class="text-4xl font-bold mb-4">Найдите свое ИТ-событие</h1>
    </transition>
    
    <transition name="slide-up" appear>
      <p class="text-gray-600 mb-8">
        Единая платформа для хакатонов, геймджемов, конкурсов и олимпиад в IT-сфере
      </p>
    </transition>
    
    <div class="flex justify-center space-x-4">
      <button 
        class="bg-purple-600 text-white px-6 py-3 rounded-md hover:bg-purple-700 transition-all duration-300 transform hover:scale-105"
        @click="$router.push('/events')"
      >
        Смотреть все события
      </button>
      <button 
        class="bg-white text-gray-700 px-6 py-3 rounded-md border border-gray-300 hover:bg-gray-50 transition-all duration-300 transform hover:scale-105 pulse"
        @click="$router.push('/events/create')"
      >
        Создать событие
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Hero'
}
</script> 