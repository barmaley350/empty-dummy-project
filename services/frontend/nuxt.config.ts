// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devServer: {
    port: 5173,
    host: '0.0.0.0'  // Разрешить подключения из Docker
  },
  runtimeConfig: {
    baseURL: 'http://service.backend:8000/api/list/',
    public: {
    },
  },
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  modules: [
    '@nuxt/ui',
  ],
  css: [
    '~/assets/css/main.css',
  ],
})