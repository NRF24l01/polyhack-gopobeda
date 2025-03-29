<template>
  <header class="border-b border-gray-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <div class="flex items-center">
          <router-link to="/" class="text-xl font-bold">
            <span class="text-purple-600">Tech</span>
            <span>Events</span>
          </router-link>
        </div>
        
        <nav class="hidden md:flex space-x-8">
          <router-link v-for="(link, index) in navLinks" :key="index" :to="link.path" class="text-gray-700 hover:text-gray-900"active-class="text-purple-600" v-html="link.title" />
        </nav>
        <button 
          class="bg-purple-600 text-white px-4 py-2 rounded-md hover:bg-purple-700"
          @click="$router.push('/events/create')"
        >
          + Создать событие
        </button>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {
      navLinks: [
        { title: 'Главная', path: '/' },
        { title: '<span class="mr-1">❤️</span>Избранное', path: '/favorite' },
        { title: 'События', path: '/events' },
        { title: 'О нас', path: '/about' }
      ]
    }
  }
}
</script> 