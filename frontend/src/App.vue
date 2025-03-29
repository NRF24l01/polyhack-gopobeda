<script setup>
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
</script>

<template>
  <div class="min-h-screen flex flex-col">
    <Header />
    <main class="flex-grow">
      <transition name="fade" mode="out-in">
         <router-view :key="$route.fullPath" />
       </transition>
    </main>
    <Footer />
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
/* Fade transition */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.2s ease; /* Reduced to 0.5s */
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

/* Slide transition */
.slide-enter-active, .slide-leave-active {
  transition: transform 0.2s ease; /* Reduced to 0.5s */
}
.slide-enter, .slide-leave-to {
  transform: translateX(100%);
}
</style>
