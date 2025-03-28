<template>
  <div class="min-h-screen flex flex-col">
    <!-- Ваш существующий header -->
    <main class="flex-grow">
      <router-view></router-view>
    </main>
  
  </div>
</template>

<script>

export default {
  name: 'App',

}
</script> 