<template>
  <div class="min-h-screen bg-white">
    <Header />
    <Hero />
    <EventsList />
  </div>
  <Footer />
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