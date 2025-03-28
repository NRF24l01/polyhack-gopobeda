<script setup>
import NewIvent from '../components/NewIvent.vue';
</script>

<template>
  <div class="min-h-screen bg-white">
    <Hero />
    <EventsList />
    <NewIvent />
  </div>
</template>

<script>

export default {
  name: 'HomePage',
  head() {
    return {
      title: 'TechEvents - Найдите свое ИТ-событие',
      meta: [
        {
          hid: 'description',
          name: 'description',
          content: 'Единая платформа для хакатонов, геймджемов, конкурсов и олимпиад в IT-сфере'
        }
      ]
    }
  }
}
</script> 