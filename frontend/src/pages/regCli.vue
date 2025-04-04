<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-r from-blue-400 to-purple-500">
    <div class="w-full max-w-md p-8 bg-white rounded-2xl shadow-2xl">
      <h2 class="text-2xl font-bold text-center mb-6 text-gray-700">Регистрация</h2>

      <div class="mb-4">
        <label class="block text-gray-500 text-sm mb-1">Email</label>
        <input v-model="regCli.email" type="email" 
               :class="{'border-red-500': emailError}" 
               class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400" 
               placeholder="Введите ваш email" />
        <p v-if="emailError" class="text-red-500 text-sm mt-1">{{ emailError }}</p>
      </div>

      <div class="mb-4">
        <label class="block text-gray-500 text-sm mb-1">Login</label>
        <input v-model="regCli.username" type="text" 
               :class="{'border-red-500': loginError}" 
               class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400" 
               placeholder="Введите ваш логин" />
        <p v-if="loginError" class="text-red-500 text-sm mt-1">{{ loginError }}</p>
      </div>

      <div class="mb-4">
        <label class="block text-gray-500 text-sm mb-1">Password</label>
        <input v-model="regCli.password" type="password" 
               :class="{'border-red-500': passwordError}" 
               class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400" 
               placeholder="Введите ваш пароль" />
        <p v-if="passwordError" class="text-red-500 text-sm mt-1">{{ passwordError }}</p>
      </div>

      <button @click="register" 
              :disabled="loading" 
              class="w-full bg-blue-500 text-white p-3 rounded-lg hover:bg-blue-600 transition disabled:opacity-50">
        {{ loading ? 'Регистрация...' : 'Зарегистрироваться' }}
      </button>

      <p v-if="serverError" class="text-red-500 text-center mt-3">{{ serverError }}</p>

      <p class="text-center text-gray-600 mt-4">
        Есть аккаунт? 
        <span @click="$router.push('/auth/client')" class="text-blue-500 hover:text-blue-600 cursor-pointer">
          Войти
        </span>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      regCli: {
        email: '',
        username: '',
        password: '',
      },
      emailError: '',
      loginError: '',
      passwordError: '',
      serverError: '',
      loading: false
    };
  },
  methods: {
    validateForm() {
      const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      const usernamePattern = /^.{2,50}$/;
      const passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$/;

      this.emailError = this.regCli.email.length >= 8 && this.regCli.email.length <= 120 && emailPattern.test(this.regCli.email) 
        ? '' 
        : 'Введите корректный email (от 8 до 120 символов)';
      this.passwordError = passwordPattern.test(this.regCli.password) 
        ? '' 
        : 'Пароль должен содержать от 8 до 60 символов, включая хотя бы одну заглавную букву, одну строчную и одну цифру';
      this.usernameError = usernamePattern.test(this.regCli.username) ? '' : 'Имя пользователя должно содержать от 1 до 50 символов';

      return !this.emailError && !this.loginError && !this.passwordError;
    },
    
    async register() {
      if (!this.validateForm()) return;

      this.serverError = '';
      this.loading = true;

      try {
        const response = await fetch(`${import.meta.env.VITE_BASE_URL}/auth/register/user`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(this.regCli)
        });

        const data = await response.json();
        
        if (!response.ok) {
          // Обрабатываем формат ответа с бэка
          if (data.details) {
            this.serverError = data.details;
          } else if (data.reason) {
            this.serverError = data.reason;
          } else if (data.error) {
            this.serverError = data.error;
          } else {
            this.serverError = "Неизвестная ошибка";
          }
          return;
        }

        console.log('Registration successful:', data);
      } catch (error) {
        console.error('Error during registration:', error);
        this.serverError = 'Ошибка сервера, попробуйте позже.';
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>


<style scoped>
input {
  border: 1px solid #ccc;
}
.border-red-500 {
  border-color: #f56565;
}
</style>
