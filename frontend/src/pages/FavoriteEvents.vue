<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <h1 class="text-3xl font-bold mb-8">Избранные мероприятия</h1>
    
    <div v-if="favoriteEvents.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <EventCard
        v-for="event in favoriteEvents"
        :key="event.id"
        :event="event"
        :favorite="true"
        @card-click="$router.push(`/events/${event.id}`)"
        @toggle-favorite="removeFromFavorites(event)"
      />
    </div>

    <div v-else class="text-center py-12">
      <p class="text-gray-600 mb-4">У вас пока нет избранных мероприятий</p>
      <router-link 
        to="/" 
        class="inline-block bg-purple-600 text-white px-6 py-2 rounded-md hover:bg-purple-700"
      >
        Найти мероприятия
      </router-link>
    </div>
  </div>
</template>

<script setup>
import EventCard from "@/components/EventCard.vue";
</script> 

<script>
export default {
  name: 'FavoriteEvents',
  data() {
    return {
      favoriteEvents: []
    }
  },
  created() {
    // Загружаем избранные мероприятия из localStorage
    const favorites = localStorage.getItem('favoriteEvents')
    if (favorites) {
      this.favoriteEvents = JSON.parse(favorites)
    }
  },
  methods: {
    removeFromFavorites(event) {
      this.favoriteEvents = this.favoriteEvents.filter(e => e.id !== event.id)
      localStorage.setItem('favoriteEvents', JSON.stringify(this.favoriteEvents))
    }
  }
}
</script> 