<template>
  <Header />
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <h1 class="text-3xl font-bold mb-8">Избранные мероприятия</h1>
    
    <div v-if="favoriteEvents.length" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div 
        v-for="event in favoriteEvents" 
        :key="event.id"
        class="bg-white rounded-lg shadow overflow-hidden"
      >
        <img :src="event.image" :alt="event.title" class="w-full h-48 object-cover" />
        <div class="p-4">
          <div class="flex justify-between items-start mb-2">
            <span class="inline-block px-2 py-1 text-sm text-purple-600 bg-purple-100 rounded-md">
              {{ event.type }}
            </span>
            <button 
              @click="removeFromFavorites(event)"
              class="text-red-500 hover:text-red-600"
            >
              ❤️
            </button>
          </div>
          
          <h3 class="text-xl font-semibold mb-2">{{ event.title }}</h3>
          <p class="text-gray-600 mb-4 line-clamp-2">{{ event.description }}</p>
          
          <div class="flex items-center text-sm text-gray-500 mb-2">
            <span class="mr-2">📅</span>
            {{ event.date }}
          </div>
          
          <div class="flex items-center text-sm text-gray-500 mb-2">
            <span class="mr-2">📍</span>
            {{ event.location }}
          </div>
          
          <div class="flex items-center text-sm text-gray-500">
            <span class="mr-2">👤</span>
            {{ event.organizer }}
          </div>

          <button 
            class="w-full mt-4 bg-purple-600 text-white px-4 py-2 rounded-md hover:bg-purple-700"
            @click="$router.push(`/events/${event.id}`)"
          >
            Подробнее
          </button>
        </div>
      </div>
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