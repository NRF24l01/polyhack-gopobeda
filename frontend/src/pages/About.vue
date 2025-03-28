<template>
  <div class="max-w-3xl mx-auto px-4 py-8">
    <h1 class="text-3xl font-bold mb-2">О платформе</h1>
    <p class="text-gray-600 mb-8">Единое место для всех IT-событий и соревнований</p>

    <div class="bg-white rounded-lg shadow p-6 mb-6">
      <h2 class="text-xl font-semibold mb-4">Наша миссия</h2>
      <p class="text-gray-600">
        Мы создали TechEvents, чтобы собрать на одной площадке информацию обо всех ключевых IT-мероприятиях: 
        хакатонах, геймджемах, олимпиадах, конкурсах и конференциях. Наша цель – помочь участникам легко 
        находить интересные события, а организаторам – привлекать больше заинтересованных участников.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
      <div class="bg-white rounded-lg shadow p-6">
        <h2 class="text-xl font-semibold mb-4">Для участников</h2>
        <ul class="space-y-3">
          <li class="flex items-center">
            <span class="mr-2">✓</span>
            Находите мероприятия по интересам
          </li>
          <li class="flex items-center">
            <span class="mr-2">✓</span>
            Отслеживайте даты проведения
          </li>
          <li class="flex items-center">
            <span class="mr-2">✓</span>
            Получайте всю необходимую информацию
          </li>
          <li class="flex items-center">
            <span class="mr-2">✓</span>
            Участвуйте в интересных событиях
          </li>
        </ul>
      </div>

      <div class="bg-white rounded-lg shadow p-6">
        <h2 class="text-xl font-semibold mb-4">Для организаторов</h2>
        <ul class="space-y-3">
          <li class="flex items-center">
            <span class="mr-2">✓</span>
            Размещайте информацию о событиях
          </li>
          <li class="flex items-center">
            <span class="mr-2">✓</span>
            Привлекайте целевую аудиторию
          </li>
          <li class="flex items-center">
            <span class="mr-2">✓</span>
            Получайте больше видимости
          </li>
          <li class="flex items-center">
            <span class="mr-2">✓</span>
            Проводите успешные мероприятия
          </li>
        </ul>
      </div>
    </div>

    <div class="bg-white rounded-lg shadow p-6">
      <h2 class="text-xl font-semibold mb-4">Свяжитесь с нами</h2>
      <p class="text-gray-600 mb-4">
        Если у вас есть вопросы, предложения или вы хотите сотрудничать, свяжитесь с нами:
      </p>
      <a 
        href="mailto:support@techevents.ru" 
        class="text-purple-600 hover:text-purple-700"
      >
        support@techevents.ru
      </a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'About'
}
</script> 