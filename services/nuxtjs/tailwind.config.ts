// tailwind.config.js или tailwind.config.ts
export default {
    darkMode: 'class', // важно!
    content: [
        './app/components/**/*.{vue,js,ts}',
        './app/layouts/**/*.vue',
        './app/pages/**/*.vue',
        './app/app.vue',
        './app/plugins/**/*.{js,ts}',
    ],
    theme: {
        extend: {
    },
    plugins: [],
}
