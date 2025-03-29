<template>
  <div
    class="bg-white rounded-lg shadow overflow-hidden cursor-pointer hover:shadow-lg transition-shadow flex flex-col"
    @click="handleCardClick"
  >
    <img :src="event.image" :alt="event.title" class="w-full h-48 object-cover" />
    <div class="p-4 flex flex-col flex-grow">
      <div class="flex justify-between items-start mb-2">
        <span class="inline-block px-2 py-1 text-sm text-purple-600 bg-purple-100 rounded-md">
          {{ event.type }}
        </span>
        <button
          @click.stop="handleToggleFavorite"
          class="transition-transform hover:scale-110"
          :class="{ 'text-red-500': favorite }"
        >
          <template v-if="favorite">
            <!-- Assuming you want to use the solid heart icon -->
            <SolidHeartIcon class="w-6 h-6 text-red-500" />
          </template>
          <template v-else>
            <!-- Outline heart icon -->
            <OutlineHeartIcon class="w-6 h-6 text-gray-400" />
          </template>
        </button>
      </div>
      <h3 class="text-xl font-semibold mb-2">{{ event.title }}</h3>
      <p class="text-gray-600 mb-4 line-clamp-2">{{ event.description }}</p>

      <div class="mt-auto">
        <div class="flex items-center text-sm text-gray-500 mb-2">
          <CalendarIcon class="w-5 h-5 mr-2" />
          {{ event.date }}
        </div>
        <div class="flex items-center text-sm text-gray-500 mb-2">
          <MapPinIcon class="w-5 h-5 mr-2" />
          {{ event.location }}
        </div>
        <div class="flex items-center text-sm text-gray-500">
          <UserIcon class="w-5 h-5 mr-2" />
          {{ event.organizer }}
        </div>
        <button
          class="w-full mt-4 bg-purple-600 text-white px-4 py-2 rounded-md hover:bg-purple-700"
          @click.stop="handleCardClick"
        >
          Подробнее
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';
import { HeartIcon as SolidHeartIcon } from "@heroicons/vue/24/solid";
import { HeartIcon as OutlineHeartIcon } from "@heroicons/vue/24/outline";
import { CalendarIcon, MapPinIcon, UserIcon } from "@heroicons/vue/24/solid";

const props = defineProps({
  event: {
    type: Object,
    required: true,
  },
  favorite: {
    type: Boolean,
    default: false,
  },
});

const emits = defineEmits(['card-click', 'toggle-favorite']);

function handleCardClick() {
  emits('card-click');
}

function handleToggleFavorite() {
  emits('toggle-favorite');
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
