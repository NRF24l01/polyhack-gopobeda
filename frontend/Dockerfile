# === Сборка Vue.js ===
FROM node:20 AS builder

ARG VITE_BASE_URL
ENV VITE_BASE_URL=${VITE_BASE_URL}
COPY .env.production /app/.env.production

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .
RUN npm run build

# === Финальный образ на основе Nginx ===
FROM nginx:alpine

RUN rm -rf /etc/nginx/conf.d/*
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/sites-enabled.conf

COPY --from=builder /app/dist /usr/share/nginx/html