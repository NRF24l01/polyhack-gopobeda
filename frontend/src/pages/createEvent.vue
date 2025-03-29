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
              pattern="https?://.*"
              placeholder="https://..."
              class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-transparent"
            />
            <p class="text-sm text-gray-500 mt-1">Введите полный URL, начиная с http:// или https://</p>
          </div>

          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1">Изображение события*</label>
            <input 
              type="file"
              @change="handleImageUpload"
              accept="image/jpeg,image/png,image/gif"
              required
              class="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-transparent"
            />
            <p class="text-sm text-gray-500 mt-1">
              Поддерживаемые форматы: JPG, PNG, GIF. Максимальный размер: 5MB
            </p>
            <div v-if="imagePreview" class="mt-2">
              <img 
                :src="imagePreview" 
                alt="Preview" 
                class="h-32 object-cover rounded-md"
              />
            </div>
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
      imagePreview: null,
      loading: false,
      error: null
    }
  },
  methods: {
    // Возвращаем полный base64 без изменений
    async fileToBase64(file) {
      return new Promise((resolve, reject) => {
        const reader = new FileReader()
        reader.readAsDataURL(file)
        reader.onload = () => {
          resolve(reader.result)  // Возвращаем полный результат без изменений
        }
        reader.onerror = error => reject(error)
      })
    },

    handleImageUpload(event) {
      const file = event.target.files[0]
      if (file) {
        // Проверяем размер файла (например, максимум 5MB)
        const maxSize = 5 * 1024 * 1024 // 5MB в байтах
        if (file.size > maxSize) {
          this.error = 'Размер файла не должен превышать 5MB'
          event.target.value = '' // Очищаем input
          this.imagePreview = null
          return
        }

        // Проверяем тип файла
        const allowedTypes = ['image/jpeg', 'image/png', 'image/gif']
        if (!allowedTypes.includes(file.type)) {
          this.error = 'Пожалуйста, загрузите изображение в формате JPG, PNG или GIF'
          event.target.value = ''
          this.imagePreview = null
          return
        }

        // Создаем URL для предпросмотра
        this.imagePreview = window.URL.createObjectURL(file)
        this.form.image = file
        this.error = null
      }
    },

    dateToTimestamp(dateString) {
      return Math.floor(new Date(dateString).getTime() / 1000).toString()
    },

    // Добавляем метод валидации URL
    isValidUrl(string) {
      try {
        new URL(string)
        return true
      } catch (_) {
        return false
      }
    },

    async createEvent() {
      this.loading = true
      this.error = null

      try {
        // Конвертируем изображение в base64
        let imageBase64 = null
        if (this.form.image) {
          imageBase64 = await this.fileToBase64(this.form.image)
        }

        // Создаем объект с данными
        const eventData = {
          title: this.form.title,
          description: this.form.description,
          start_date: this.dateToTimestamp(this.form.start_date),
          end_date: this.dateToTimestamp(this.form.end_date),
          type: this.form.type,
          format: this.form.format,
          registration_url: this.form.registration_url,
          image: imageBase64, // Отправляем полный base64 с префиксом
          place: this.form.format === 'online' ? null : this.form.location
        }
        console.log(eventData)

        const response = await fetch('http://127.0.0.1:8080/events', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('token')}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(eventData)
        })

        const responseText = await response.text()
        console.log('Ответ сервера:', responseText)

        if (!response.ok) {
          let errorMessage
          try {
            const errorData = JSON.parse(responseText)
            errorMessage = errorData.message || 'Неизвестная ошибка'
          } catch (e) {
            errorMessage = responseText || 'Ошибка при создании мероприятия'
          }
          throw new Error(`Ошибка ${response.status}: ${errorMessage}`)
        }

        const data = JSON.parse(responseText)
        this.$router.push(`/events/${data.event_id}`)
      } catch (error) {
        this.error = error.message
        console.error('Подробности ошибки:', error)
      } finally {
        this.loading = false
      }
    }
  },
  // Очищаем URL при уничтожении компонента
  beforeUnmount() {
    if (this.imagePreview) {
      window.URL.revokeObjectURL(this.imagePreview)
    }
  }
}
</script> 