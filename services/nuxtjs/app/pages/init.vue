<script setup>
definePageMeta({
    layout: 'empty',
})
useHead({
    title: 'Ура! У вас все получилось!',
    meta: [
        { name: 'description', content: 'Стратовая страница' }
    ]
})
const colorMode = useColorMode()

const isDark = computed(() => colorMode.value === 'dark')

function toggleDarkMode() {
    colorMode.preference = isDark.value ? 'light' : 'dark'
}

</script>
<template>

    <div class="flex items-center justify-center h-screen">
        <div class="flex flex-col w:3/3 md:w-2/3 lg:w-1/3">
            <div class="justify-items-center">
            </div>
            <div class="flex flex-col rounded-sm border border-gray-200 ">
                <div class="flex justify-between bg-gray-500 p-3 rounded-t-sm items-center">
                    <div class="text-xl text-center text-white">
                        Добро пожаловать!
                    </div>
                    <button @click="toggleDarkMode" class="px-2 py-1 flex items-center text-white">
                        <span v-if="!isDark">
                            <Icon name="i-lucide:moon" />
                        </span>
                        <span v-else>
                            <Icon name="i-lucide:sun" />
                        </span>
                    </button>
                </div>

                <div class="p-5 space-y-5 text-center">
                    Если вы видите эту страницу, значит, у вас всё получилось и вы всё сделали правильно
                </div>
                <div
                    class="p-3 text-center rounded-b-sm border-t border-gray-200 gap-3">
                    Есть вопросы или предложения?<br>
                    Пишите — всегда открыт к диалогу <span class="
                    bg-gray-300 
                    px-2 py-1 
                    rounded-sm
                    dark:text-gray-700">@tg_nick</span>
                </div>
                <div class="flex p-3 
            rounded-b-sm border-t border-gray-200 justify-center 
            items-center gap-3 bg-gray-100 dark:bg-gray-300 dark:text-gray-600">
                    <a href="/admin/">Django Admin</a>
                </div>
            </div>

        </div>
    </div>
</template>