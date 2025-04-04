<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-r from-blue-400 to-purple-500">
    <div class="w-full max-w-md p-8 bg-white rounded-2xl shadow-2xl">
      <h2 class="text-2xl font-bold text-center mb-6 text-gray-700">Вход</h2>

      <div class="mb-4">
        <label class="block text-gray-500 text-sm mb-1">Email</label>
        <input v-model="authOrg.email" type="email" 
               :class="{'border-red-500': emailError}" 
               class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400" 
               placeholder="Введите ваш email" />
        <p v-if="emailError" class="text-red-500 text-sm mt-1">{{ emailError }}</p>
      </div>

      <div class="mb-4">
        <label class="block text-gray-500 text-sm mb-1">Password</label>
        <input v-model="authOrg.password" type="password" 
               :class="{'border-red-500': passwordError}" 
               class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400" 
               placeholder="Введите ваш пароль" />
        <p v-if="passwordError" class="text-red-500 text-sm mt-1">{{ passwordError }}</p>
      </div>

      <button @click="register" class="mt-4 w-full bg-blue-500 text-white p-3 rounded-lg hover:bg-blue-600 transition">Войти</button>
      
      <div class="mb-4" v-if="serverError">
        <p class="text-red-500 text-center mt-3">{{ serverError }}</p>
      </div>

      <p class="text-center text-gray-600 mt-4">Нет аккаунта? <span @click="$router.push('/registration/Organisation')" class="text-blue-500 hover:text-blue-600 cursor-pointer">Зарегистрироваться</span></p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      authOrg: {
        email: '',
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
      const passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,60}$/;

      this.emailError = this.authOrg.email.length >= 8 && this.authOrg.email.length <= 120 && emailPattern.test(this.authOrg.email) 
        ? '' 
        : 'Введите корректный email (от 8 до 120 символов)';
      this.passwordError = passwordPattern.test(this.authOrg.password) 
        ? '' 
        : 'Пароль должен содержать от 8 до 60 символов, включая хотя бы одну заглавную букву, одну строчную и одну цифру';

      return !this.emailError && !this.passwordError;
    },
    async register() {
      if (!this.validateForm()) return;

      try {
        const response = await fetch(`${import.meta.env.VITE_BASE_URL}/auth/login`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.authOrg)
        });
        const data = await response.json();

        if (!response.ok) {
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

        localStorage.setItem('token', data.jwt);
        console.log('Registration successful:', data);
        console.log(localStorage.getItem("token"));
        console.log('AUTH successful:', data);
        this.$router.push('/');
      } catch (error) {
        console.error('Error during authorithation:', error);
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