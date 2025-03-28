<template>
  <div class="max-w-4xl mx-auto px-4 py-8">
    <div v-if="event" class="bg-white rounded-lg shadow-lg overflow-hidden">
      <!-- Изображение события -->
      <div class="relative h-64 md:h-96">
        <img 
          :src="event.image" 
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
            {{ isFavorite(event.id) ? '❤️' : '🤍' }}
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
              <span>{{ event.date }}</span>
            </div>
            <div class="flex items-center text-gray-600">
              <span class="mr-2">📍</span>
              <span>{{ event.location }}</span>
            </div>
            <div class="flex items-center text-gray-600">
              <span class="mr-2">👤</span>
              <span>{{ event.organizer }}</span>
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
          <p class="text-gray-600 whitespace-pre-line">{{ event.description }}</p>
        </div>

        <!-- Кнопки действий -->
        <div class="flex flex-wrap gap-4">
          <button 
            class="px-6 py-2 bg-purple-600 text-white rounded-md hover:bg-purple-700 transition-colors"
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
      <div v-if="loading" class="text-gray-600">
        Загрузка...
      </div>
      <div v-else class="text-red-600">
        Событие не найдено
      </div>
    </div>
  </div>
</template>

<script>
import { favoritesMixin } from '@/mixins/favoritesMixin'

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
      loading: true
    }
  },
  created() {
    this.fetchEvent()
  },
  methods: {
    fetchEvent() {
      // Имитация загрузки данных
      setTimeout(() => {
        this.event = {
          id: this.id,
          type: "Хакатон",
          title: "Цифровой Прорыв 2023",
          description: `Всероссийский хакатон для IT-специалистов, дизайнеров и управленцев в цифровой сфере.

Вас ждут:
• Интересные задачи от ведущих компаний
• Призовой фонд
• Возможность найти команду
• Менторская поддержка
• Нетворкинг с профессионалами отрасли

Регистрация команд до 5 ноября 2023.`,
          date: "10-12 ноября 2023",
          location: "Москва",
          organizer: "Россия - страна возможностей",
          image: "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1740&q=80",
          website: "https://example.com"
        }
        this.loading = false
      }, 500)
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