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
            <label class="block text-sm font-medium text-gray-700 mb-1">Название события*</label>
            <input 
              v-model="form.title"
              type="text"
              required
              placeholder="Введите название события"
              class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-transparent"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Описание*</label>
            <textarea
              v-model="form.description"
              required
              rows="4"
              placeholder="Опишите ваше мероприятие подробно..."
              class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-transparent"
            ></textarea>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Дата начала*</label>
              <input 
                v-model="form.start_date"
                type="datetime-local"
                required
                class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-transparent"
              />
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Дата окончания*</label>
              <input 
                v-model="form.end_date"
                type="datetime-local"
                required
                class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-transparent"
              />
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Тип события*</label>
              <select 
                v-model="form.type"
                required
                class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-transparent"
              >
                <option value="hackathon">Хакатон</option>
                <option value="meetup">Митап</option>
                <option value="conference">Конференция</option>
                <option value="workshop">Воркшоп</option>
              </select>
            </div>

            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Формат проведения*</label>
              <select 
                v-model="form.format"
                required
                class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-transparent"
              >
                <option value="online">Онлайн</option>
                <option value="offline">Офлайн</option>
                <option value="hybrid">Гибридный</option>
              </select>
            </div>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Ссылка на регистрацию*</label>
            <input 
              v-model="form.registration_url"
              type="url"
              required
              placeholder="https://..."
              class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-transparent"
            />
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Изображение события*</label>
            <input 
              type="file"
              @change="handleImageUpload"
              accept="image/*"
              required
              class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-transparent"
            />
            <p class="text-sm text-gray-500 mt-1">Рекомендуемый размер: 1200x630px</p>
          </div>

          <div v-if="error" class="bg-red-50 border border-red-200 text-red-600 px-4 py-3 rounded-md">
            {{ error }}
          </div>

          <div class="flex justify-end space-x-4 pt-4">
            <button 
              type="button"
              class="px-6 py-2 border border-gray-300 rounded-md hover:bg-gray-50"
              @click="$router.push('/events')"
            >
              Отмена
            </button>
            <button 
              type="submit"
              :disabled="loading"
              class="px-6 py-2 bg-purple-600 text-white rounded-md hover:bg-purple-700 disabled:opacity-50"
            >
              <span v-if="loading">Создание...</span>
              <span v-else>Создать событие</span>
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
        start_date: '',
        end_date: '',
        type: 'hackathon',
        format: 'online',
        registration_url: '',
        image: null
      },
      loading: false,
      error: null
    }
  },
  methods: {
    handleImageUpload(event) {
      const file = event.target.files[0]
      if (file) {
        this.form.image = file
      }
    },
    dateToTimestamp(dateString) {
      return Math.floor(new Date(dateString).getTime() / 1000)
    },
    async createEvent() {
      this.loading = true
      this.error = null

      try {
        // Создаем объект с данными
        const eventData = {
          title: this.form.title,
          description: this.form.description,
          start_date: this.dateToTimestamp(this.form.start_date),
          end_date: this.dateToTimestamp(this.form.end_date),
          type: this.form.type,
          format: this.form.format,
          image: this.form.image,
          registration_url: this.form.registration_url
        }
        console.log(eventData)

        const response = await fetch(`${import.meta.env.VITE_BASE_URL}/events`, {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(eventData)
        })

        if (!response.ok) {
          const errorData = await response.json()
          throw new Error(errorData.message || 'Ошибка при создании мероприятия')
        }

        const data = await response.json()
        
        // Если нужно отправить изображение отдельно
        if (this.form.image) {
          const imageFormData = new FormData()
          imageFormData.append('image', this.form.image)
          
          await fetch(`http://127.0.0.1:8080/events/${data.event_id}/image`, {
            method: 'POST',
            headers: {
              'Authorization': `Bearer ${localStorage.getItem('token')}`
            },
            body: imageFormData
          })
        }

        // Перенаправляем на страницу созданного мероприятия
        this.$router.push(`/events/${data.event_id}`)
      } catch (error) {
        this.error = error.message
        console.error('Ошибка:', error)
      } finally {
        this.loading = false
      }
    }
  }
}
</script> 