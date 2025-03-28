<template>
  <div>
    <!-- Секция "Организуйте ИТ-событие" -->
    <div class="bg-purple-50 py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-2xl font-bold mb-4">Организуете ИТ-событие?</h2>
        <p class="text-gray-600 mb-8">
          Разместите информацию о вашем мероприятии на нашей платформе и привлеките больше участников
        </p>
        <button 
          @click="$router.push('/events/create')"
          class="bg-purple-600 text-white px-6 py-2 rounded-md hover:bg-purple-700 transition-colors"
        >
          Создать событие
        </button>
      </div>
    </div>

    <!-- Копирайт -->
    <div class="border-t border-gray-200 py-4">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center text-gray-500 text-sm">
        © {{ currentYear }} TechEvents. Все права защищены.
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Footer',
  computed: {
    currentYear() {
      return new Date().getFullYear()
    }
  }
}
</script> 