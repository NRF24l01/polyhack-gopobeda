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
        :favorite="isFavorite(event.id)"
        @card-click="$router.push(`/events/${event.id}`)"
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
  mixins: [favoritesMixin],
  data() {
    return {
      searchQuery: "",
      selectedCategory: "",
      categories: [
        "Хакатоны",
        "Геймджемы",
        "Конкурсы",
        "Олимпиады",
        "Конференции",
      ],
      events: [
        {
          id: 1,
          type: "Хакатон",
          title: "Цифровой Прорыв 2023",
          description:
            "Всероссийский хакатон для IT-специалистов, дизайнеров и управленцев в цифровой сфере",
          date: "10-12 ноября 2023",
          location: "Москва",
          organizer: "Россия - страна возможностей",
          image:
            "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1740&q=80",
        },
        {
          id: 2,
          type: "Геймджем",
          title: "Ludum Dare 54",
          description:
            "Всемирный онлайн-геймджем, где участники создают игру с нуля за 48 или 72 часа",
          date: "15-18 октября 2023",
          location: "Онлайн",
          organizer: "Ludum Dare Community",
          image:
            "https://images.unsplash.com/photo-1552820728-8b83bb6b773f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1740&q=80",
        },
        {
          id: 3,
          type: "Олимпиада",
          title: "Всероссийская олимпиада по программированию",
          description:
            "Ежегодная олимпиада для школьников и студентов, проверяющая навыки в алгоритмическом программировании",
          date: "1-5 декабря 2023",
          location: "Санкт-Петербург",
          organizer: "Министерство образования РФ",
          image:
            "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1740&q=80",
        },
      ],
    };
  },
  computed: {
    filteredEvents() {
      return this.events.filter((event) => {
        const matchesSearch =
          event.title.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
          event.description
            .toLowerCase()
            .includes(this.searchQuery.toLowerCase());
        const matchesCategory =
          !this.selectedCategory || event.type === this.selectedCategory;
        return matchesSearch && matchesCategory;
      });
    },
  },
  methods: {
    selectCategory(category) {
      this.selectedCategory =
        this.selectedCategory === category ? "" : category;
    },
  },
};
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
