<template>
  <header class="border-b border-gray-200 bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between items-center h-16">
        <div class="flex items-center">
          <router-link to="/" class="text-xl font-bold">
            <span class="text-purple-600">Tech</span>
            <span>Events</span>
          </router-link>
        </div>

        <div class="hidden md:flex space-x-8">
          <router-link
            v-for="(link, index) in navLinks"
            :key="index"
            :to="link.path"
            class="text-gray-700 hover:text-gray-900"
            active-class="text-purple-600"
            v-html="link.title"
          />
        </div>

        <button
          class="hidden md:block bg-purple-600 text-white px-4 py-2 rounded-md hover:bg-purple-700"
          @click="$router.push('/auth/Client')"
        >
          Войти
        </button>

        <!-- Мобильное меню -->
        <button
          @click="toggleMenu"
          class="md:hidden text-gray-700 border border-gray-300 rounded-md p-2"
        >
          <svg
            class="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h16m-7 6h7"
            ></path>
          </svg>
        </button>
      </div>
    </div>

    <transition name="slide">
      <div
        v-if="isMenuOpen"
        class="md:hidden bg-white border-t border-gray-200 p-4 fixed top-16 left-0 w-full z-10"
      >
        <nav class="flex flex-col space-y-4">
          <router-link
            v-for="(link, index) in navLinks"
            :key="index"
            :to="link.path"
            class="text-gray-700 hover:text-gray-900"
            active-class="text-purple-600"
            v-html="link.title"
            @click="toggleMenu"
          />
          <button
            class="bg-purple-600 text-white px-4 py-2 rounded-md hover:bg-purple-700"
            @click="
              $router.push('/events/create');
              toggleMenu();
            "
          >
            + Создать событие
          </button>
        </nav>
      </div>
    </transition>
  </header>

  <main
    :class="{ 'mt-40': isMenuOpen, 'mt-16 md:mt-0': !isMenuOpen }"
    class="transition-all duration-300"
  >
    <slot></slot>
  </main>
</template>

<script>
export default {
  name: "Header",
  data() {
    return {
      isMenuOpen: false,
      navLinks: [
        { title: "Главная", path: "/" },
        { title: "Избранное", path: "/favorites" },
        { title: "События", path: "/events" },
        { title: "О нас", path: "/about" },
      ],
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuOpen = !this.isMenuOpen;
    },
  },
};
</script>

<style scoped>
.slide-enter-active,
.slide-leave-active {
  transition: transform 0.3s ease-out, opacity 0.3s ease-out;
}
.slide-enter-from,
.slide-leave-to {
  transform: translateY(-10px);
  opacity: 0;
}
</style>
