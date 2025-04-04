<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-r from-blue-400 to-purple-500">
    <div class="w-full max-w-md p-8 bg-white rounded-2xl shadow-2xl">
      <h2 class="text-2xl font-bold text-center mb-6 text-gray-700">Регистрация</h2>

      <div class="mb-4">
        <label class="block text-gray-500 text-sm mb-1">Email</label>
        <input v-model="regOrg.email" type="email" :class="{'border-red-500': emailError}" class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400" placeholder="Введите ваш email" />
        <p v-if="emailError" class="text-red-500 text-sm mt-1">{{ emailError }}</p>
      </div>

      <div class="mb-4">
        <label class="block text-gray-500 text-sm mb-1">Login</label>
        <input v-model="regOrg.username" type="text" :class="{'border-red-500': loginError}" class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400" placeholder="Введите ваш логин" />
        <p v-if="loginError" class="text-red-500 text-sm mt-1">{{ loginError }}</p>
      </div>

      <div class="mb-4">
        <label class="block text-gray-500 text-sm mb-1">Password</label>
        <input v-model="regOrg.password" type="password" :class="{'border-red-500': passwordError}" class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400" placeholder="Введите ваш пароль" />
        <p v-if="passwordError" class="text-red-500 text-sm mt-1">{{ passwordError }}</p>
      </div>

      <button @click="register" class="w-full bg-blue-500 text-white p-3 rounded-lg hover:bg-blue-600 transition">Зарегистрироваться</button>
      
      <div class="mb-4" v-if="serverError">
        <p class="text-red-500 text-center mt-3">{{ serverError }}</p>
      </div>

      <p class="text-center text-gray-600 mt-4">Есть аккаунт? <span @click="$router.push('/auth/Organisation')" class="text-blue-500 hover:text-blue-600 cursor-pointer">Войти</span></p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      regOrg: {
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
      const usernamePattern = /^.{1,50}$/;
      const passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,60}$/;
      
      this.emailError = this.regOrg.email.length >= 8 && this.regOrg.email.length <= 120 && emailPattern.test(this.regOrg.email) 
        ? '' 
        : 'Введите корректный email (от 8 до 120 символов)';
      this.passwordError = passwordPattern.test(this.regOrg.password) 
        ? '' 
        : 'Пароль должен содержать от 8 до 60 символов, включая хотя бы одну заглавную букву, одну строчную и одну цифру';
      this.usernameError = usernamePattern.test(this.regOrg.username) ? '' : 'Имя пользователя должно содержать от 1 до 50 символов';

      return !this.emailError && !this.loginError && !this.passwordError;
    },
    async register() {
      if (!this.validateForm()) return;

      try {
        const response = await fetch(`${import.meta.env.VITE_BASE_URL}/auth/register/organizer`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.regOrg)
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
        this.$router.push('/');
      } catch (error) {
        console.error('Error during registration:', error);
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