<template>
  <div>
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