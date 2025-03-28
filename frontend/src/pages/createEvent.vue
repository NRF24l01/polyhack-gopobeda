<template>
  <div class="max-w-3xl mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold mb-2">Создать новое событие</h1>
    <p class="text-gray-600 mb-8">Заполните информацию о вашем мероприятии для публикации на платформе</p>

    <div class="bg-white rounded-lg shadow p-6">
      <h2 class="text-xl font-semibold mb-2">Данные о событии</h2>
      <p class="text-gray-600 mb-6">Заполните все необходимые поля для создания события</p>

      <form @submit.prevent="createEvent">
        <div class="space-y-6">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Название события</label>
            <input 
              v-model="form.title"
              type="text"
              placeholder="Введите название события"
              class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-transparent"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Описание</label>
            <textarea
              v-model="form.description"
              rows="4"
              placeholder="Опишите ваше мероприятие подробно..."
              class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-transparent"
            ></textarea>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Дата проведения</label>
              <input 
                v-model="form.date"
                type="text"
                placeholder="Например: 10-12 ноября 2023"
                class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-transparent"
              />
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Место проведения</label>
              <input 
                v-model="form.location"
                type="text"
                placeholder="Город или Онлайн"
                class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-transparent"
              />
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Организатор</label>
              <input 
                v-model="form.organizer"
                type="text"
                placeholder="Кто организует событие"
                class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-transparent"
              />
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Тип события</label>
              <select 
                v-model="form.type"
                class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-transparent"
              >
                <option value="Хакатон">Хакатон</option>
                <option value="Геймджем">Геймджем</option>
                <option value="Конкурс">Конкурс</option>
                <option value="Олимпиада">Олимпиада</option>
                <option value="Конференция">Конференция</option>
              </select>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">URL изображения (опционально)</label>
              <input 
                v-model="form.imageUrl"
                type="text"
                placeholder="URL изображения"
                class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-transparent"
              />
              <p class="text-sm text-gray-500 mt-1">Ссылка на изображение для события</p>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Официальный сайт (опционально)</label>
              <input 
                v-model="form.website"
                type="text"
                placeholder="https://..."
                class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-transparent"
              />
              <p class="text-sm text-gray-500 mt-1">Ссылка на официальный сайт события</p>
            </div>
          </div>

          <div class="flex justify-end space-x-4 pt-4">
            <button 
              type="button"
              class="px-6 py-2 border border-gray-300 rounded-md hover:bg-gray-50"
              @click="$router.push('/')"
            >
              Отмена
            </button>
            <button 
              type="submit"
              class="px-6 py-2 bg-purple-600 text-white rounded-md hover:bg-purple-700"
            >
              Создать событие
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CreateEvent',
  data() {
    return {
      form: {
        title: '',
        description: '',
        date: '',
        location: '',
        organizer: '',
        type: 'Хакатон',
        imageUrl: '',
        website: ''
      }
    }
  },
  methods: {
    createEvent() {
      // Здесь будет логика создания события
      console.log('Создание события:', this.form)
      this.$router.push('/')
    }
  }
}
</script> 