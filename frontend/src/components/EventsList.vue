<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
    <div class="flex justify-between items-center mb-8">
      <h2 class="text-2xl font-bold">Популярные события</h2>
      <router-link to="/events" class="text-purple-600 hover:text-purple-700">
        Смотреть все
      </router-link>
    </div>

    <div class="mb-8">
      <input
        v-model="searchQuery"
        type="text"
        placeholder="Поиск событий..."
        class="w-full px-4 py-2 border border-gray-300 rounded-md"
      />
    </div>

    <div class="flex space-x-4 mb-8 overflow-x-auto">
      <button
        v-for="category in categories"
        :key="category"
        :class="[
          'px-4 py-2 rounded-md whitespace-nowrap',
          selectedCategory === category
            ? 'bg-purple-600 text-white'
            : 'bg-gray-100 hover:bg-gray-200',
        ]"
        @click="selectCategory(category)"
      >
        {{ category }}
      </button>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <EventCard
        v-for="event in filteredEvents"
        :key="event.id"
        :event="event"
        :favorite="isFavorite(event.event_id)"
        @card-click="$router.push(`/events/${event.event_id}`)"
        @toggle-favorite="toggleFavorite(event)"
      />
    </div>
  </div>
</template>

<script>
import EventCard from "@/components/EventCard.vue";
import { favoritesMixin } from "@/mixins/favoritesMixin";

export default {
  name: "EventsList",
  components: {
    EventCard,
  },
  watch: {
    searchQuery() {
      this.fetchEvents();
    },
    selectedCategory() {
      this.fetchEvents();
    }
  },
  mixins: [favoritesMixin],
  data() {
    return {
      searchQuery: '',
      selectedCategory: '',
      categories: ['Хакатон', 'Геймджем', 'Конкурс', 'Олимпиад', 'Конференция'],
      events: [],
      filteredEvents: [],
      loading: false,
      error: null
    }
  },
  methods: {
    selectCategory(category) {
      this.selectedCategory = this.selectedCategory === category ? '' : category
    },
    formatDate(timestamp) {
      return new Date(timestamp * 1000).toLocaleDateString('ru-RU', {
        day: 'numeric',
        month: 'long',
        year: 'numeric'
      })
    },
    async fetchEvents() {
      this.loading = true
      this.error = null

      try {
        const response = await fetch(`${import.meta.env.VITE_BASE_URL}/events`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json'
          }
        })

        if (!response.ok) {
          throw new Error('Ошибка при загрузке событий')
        }

        const data = await response.json()
        this.events = data
        console.log(data)
        this.filteredEvents = this.events.filter((event) => {
          const matchesSearch =
            event.title.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
            event.description
              .toLowerCase()
              .includes(this.searchQuery.toLowerCase());
          const matchesCategory =
            !this.selectedCategory || event.type === this.selectedCategory;
          return matchesSearch && matchesCategory;
        });
      } catch (error) {
        this.error = error.message
        console.error('Ошибка:', error)
      } finally {
        this.loading = false
      }
    }
  },
  created() {
    this.fetchEvents()
  }
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style> 