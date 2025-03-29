<template>
  <div class="max-w-4xl mx-auto px-4 py-8">
    <div v-if="event" class="bg-white rounded-lg shadow-lg overflow-hidden">
      <!-- Изображение события -->
      <div class="relative h-64 md:h-96">
        <img
          :src="event.image_url"
          :alt="event.title"
          class="w-full h-full object-cover"
        />
        <div class="absolute top-4 right-4 flex items-center space-x-4">
          <span class="px-3 py-1 bg-purple-600 text-white rounded-full text-sm">
            {{ event.type }}
          </span>
          <button
            @click="toggleFavorite(event)"
            class="p-2 bg-white rounded-full shadow-lg transition-transform hover:scale-110"
            :class="{ 'text-red-500': isFavorite(event.id) }"
          >
            {{ isFavorite(event.id) ? "❤️" : "🤍" }}
          </button>
        </div>
      </div>

      <!-- Информация о событии -->
      <div class="p-6">
        <h1 class="text-3xl font-bold mb-4">{{ event.title }}</h1>

        <!-- Основная информация -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
          <div class="space-y-4">
            <div class="flex items-center text-gray-600">
              <span class="mr-2">📅</span>
              <span>{{ convertUnixTimestamp(parseInt(event.start_date)) }} - {{ convertUnixTimestamp(event.end_date) }}</span>
            </div>
            <div class="flex items-center text-gray-600">
              <span class="mr-2">📍</span>
              <span v-if="event.format != 'online'">{{ event.location }}</span>
              <span v-else>Онлайн</span>
            </div>
            <div class="flex items-center text-gray-600">
              <span class="mr-2">👤</span>
              <span>{{ event.organizer.username }}</span>
            </div>
          </div>

          <div class="space-y-4">
            <a
              v-if="event.website"
              :href="event.website"
              target="_blank"
              class="inline-flex items-center text-purple-600 hover:text-purple-700"
            >
              <span class="mr-2">🌐</span>
              Официальный сайт
            </a>
          </div>
        </div>

        <!-- Описание -->
        <div class="mb-8">
          <h2 class="text-xl font-semibold mb-4">Описание</h2>
          <p class="text-gray-600 whitespace-pre-line">
            {{ event.description }}
          </p>
        </div>

        <!-- Кнопки действий -->
        <div class="flex flex-wrap gap-4">
          <button
            class="px-6 py-2 bg-purple-600 text-white rounded-md hover:bg-purple-700 transition-colors"
            @click="window.location.href = '{{ event.registration_url }}'"
          >
            Принять участие
          </button>
          <button
            class="px-6 py-2 border border-purple-600 text-purple-600 rounded-md hover:bg-purple-50 transition-colors"
            @click="shareEvent"
          >
            Поделиться
          </button>
          <button
            class="px-6 py-2 border border-gray-300 text-gray-700 rounded-md hover:bg-gray-50 transition-colors"
            @click="$router.push('/')"
          >
            Назад
          </button>
        </div>
      </div>
    </div>

    <!-- Загрузка или ошибка -->
    <div v-else class="text-center py-12">
      <div v-if="loading" class="text-gray-600">Загрузка...</div>
      <div v-else class="text-red-600">Событие не найдено</div>
    </div>
  </div>
</template>

<script>
import { favoritesMixin } from '@/mixins/favoritesMixin'
import { useRoute } from 'vue-router'

export default {
  name: 'EventDetails',
  mixins: [favoritesMixin],
  props: {
    id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      event: null,
      loading: true,
    }
  },
  created() {
    this.fetchEvent()
  },
  methods: {
    
    convertUnixTimestamp(timestamp) {
        return new Date(timestamp * 1000).toLocaleString("en-GB", {
            timeZone: "Etc/GMT-3",
            hour12: false
        });
    },
    async fetchEvent() {
      const rid = useRoute().params.id
      this.loading = true
      this.error = null

      try {
        const response = await fetch(`${import.meta.env.VITE_BASE_URL}/events/${rid}`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json'
          }
        });

        if (!response.ok) {
          console.log(response);
          throw new Error('Ошибка при загрузке событий');
        }

        const data = await response.json(); // Добавляем await
        this.event = data;
        console.log(data);
      } catch (error) {
        this.error = error.message;
        console.error('Ошибка:', error);
      } finally {
        this.loading = false;
      }

    },
    shareEvent() {
      if (navigator.share) {
        navigator.share({
          title: this.event.title,
          text: this.event.description,
          url: window.location.href
        })
      } else {
        navigator.clipboard.writeText(window.location.href)
          .then(() => alert('Ссылка скопирована в буфер обмена'))
      }
    }
  }
}
</script>
