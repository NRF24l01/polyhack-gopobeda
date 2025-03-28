<template>
  <div class="bg-white rounded-lg shadow overflow-hidden hover:shadow-md transition-shadow">
    <img :src="image" :alt="title" class="w-full h-48 object-cover" />
    <div class="p-4">
      <div class="mb-4">
        <span 
          class="inline-block px-2 py-1 text-sm rounded-md"
          :class="typeColors[type] || 'bg-purple-100 text-purple-600'"
        >
          {{ type }}
        </span>
      </div>
      
      <h3 class="text-xl font-semibold mb-2">{{ title }}</h3>
      <p class="text-gray-600 mb-4 line-clamp-2">{{ description }}</p>
      
      <div class="space-y-2 mb-4">
        <div class="flex items-center text-sm text-gray-500">
          <span class="mr-2">📅</span>
          {{ date }}
        </div>
        
        <div class="flex items-center text-sm text-gray-500">
          <span class="mr-2">📍</span>
          {{ location }}
        </div>
        
        <div class="flex items-center text-sm text-gray-500">
          <span class="mr-2">👤</span>
          {{ organizer }}
        </div>
      </div>

      <button 
        class="w-full bg-purple-600 text-white px-4 py-2 rounded-md hover:bg-purple-700 transition-colors"
        @click="$emit('click')"
      >
        Подробнее
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'EventCard',
  props: {
    type: {
      type: String,
      required: true
    },
    title: {
      type: String,
      required: true
    },
    description: {
      type: String,
      required: true
    },
    date: {
      type: String,
      required: true
    },
    location: {
      type: String,
      required: true
    },
    organizer: {
      type: String,
      required: true
    },
    image: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      typeColors: {
        'Хакатон': 'bg-purple-100 text-purple-600',
        'Геймджем': 'bg-pink-100 text-pink-600',
        'Конкурс': 'bg-orange-100 text-orange-600',
        'Олимпиада': 'bg-blue-100 text-blue-600',
        'Конференция': 'bg-green-100 text-green-600'
      }
    }
  }
}
</script> 