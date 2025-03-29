<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <div class="flex justify-between items-center mb-8">
      <h2 class="text-2xl font-bold">Все события</h2>
    </div>

    <EventsList />
  </div>
</template>

<script setup>
import EventsList from "@/components/EventsList.vue"
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style> 