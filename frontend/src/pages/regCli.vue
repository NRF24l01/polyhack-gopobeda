<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-r from-blue-400 to-purple-500">
    <div class="w-full max-w-md p-8 bg-white rounded-2xl shadow-2xl">
      <h2 class="text-2xl font-bold text-center mb-6 text-gray-700">Регистрация</h2>

      <div class="mb-4">
        <label class="block text-gray-500 text-sm mb-1">Email</label>
        <input v-model="regCli.email" type="email" :class="{'border-red-500': emailError}" class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400" placeholder="Введите ваш email" />
        <p v-if="emailError" class="text-red-500 text-sm mt-1">{{ emailError }}</p>
      </div>

      <div class="mb-4">
        <label class="block text-gray-500 text-sm mb-1">Login</label>
        <input v-model="regCli.username" type="text" :class="{'border-red-500': loginError}" class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400" placeholder="Введите ваш логин" />
        <p v-if="loginError" class="text-red-500 text-sm mt-1">{{ loginError }}</p>
      </div>

      <div class="mb-4">
        <label class="block text-gray-500 text-sm mb-1">Password</label>
        <input v-model="regCli.password" type="password" :class="{'border-red-500': passwordError}" class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400" placeholder="Введите ваш пароль" />
        <p v-if="passwordError" class="text-red-500 text-sm mt-1">{{ passwordError }}</p>
      </div>

      <button @click="register" class="w-full bg-blue-500 text-white p-3 rounded-lg hover:bg-blue-600 transition">Зарегистрироваться</button>

      <p class="text-center text-gray-600 mt-4">Есть аккаунт? <span @click="$router.push('/auth/client')" class="text-blue-500 hover:text-blue-600 cursor-pointer">Войти</span></p>
    </div>
  </div>
</template>

<script>
import { jwtDecode } from "jwt-decode"; // Correct import for ES module

export function decodeJwt(token) {
  try {
    return jwtDecode(token);
  } catch (error) {
    console.error("Invalid JWT", error);
    return null;
  }
}

export function getCustomClaims(token) {
  const decoded = decodeJwt(token);
  return decoded;
}

const token = localStorage.getItem("token")
console.log(token)
console.log(getCustomClaims(token))

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
      passwordError: ''
    };
  },
  methods: {
    validateForm() {
      this.emailError = this.regCli.email.includes('@') ? '' : 'Введите корректный email';
      this.loginError = this.regCli.username.trim() ? '' : 'Логин не может быть пустым';
      this.passwordError = this.regCli.password.length >= 6 ? '' : 'Пароль должен содержать минимум 6 символов';

      return !this.emailError && !this.loginError && !this.passwordError;
    },
    async register() {
      if (!this.validateForm()) return;

      try {
        const response = await fetch(`${import.meta.env.VITE_BASE_URL}/auth/register/user`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.regCli)
        });
        const data = await response.json();
        console.log('Registration successful:', data);
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