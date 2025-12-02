<script setup>
definePageMeta({
    layout: 'empty',
})
</script>
<template>
    <div class="flex items-center justify-center h-screen">
        <div class="flex flex-col w-1/3">
            <LayoutCard>
                <template #title>
                    <div class="flex justify-center">
                        <LayoutTitle class="text-2xl">Добро пожаловать!</LayoutTitle>
                    </div>

                </template>
                <template #description>
                    <div class="text-center">
                        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Earum excepturi recusandae officiis
                        est culpa hic, laboriosam aspernatur voluptatibus
                    </div>
                </template>
                <template #fields>
                    <div class="flex flex-col gap-3">
                        <div class="flex flex-col gap-3">
                            <label for="user_name" class="block">
                                <TitlesSimple>Имя пользователя</TitlesSimple>
                            </label>
                            <input type="text" id="user_name"
                                class="border border-gray-300 text-sm rounded-sm w-full px-3 py-2.5 shadow-xs placeholder:text-body"
                                placeholder="name@example.com" required />
                        </div>
                        <div class="flex flex-col gap-3">
                            <label for="user_password" class="block">
                                <TitlesSimple>Пароль</TitlesSimple>
                            </label>
                            <input type="password" id="user_password"
                                class="border border-gray-300 text-sm rounded-sm w-full px-3 py-2.5 shadow-xs placeholder:text-body"
                                required />
                        </div>
                    </div>

                </template>
                <template #button>
                    <div class="flex justify-center">
                        <ButtonsEnter class="text-2xl font-bold">Вход</ButtonsEnter>
                    </div>
                </template>
                <template #footer>
                    <div class="flex justify-between">
                        <NuxtLink class="navbar-brand" to="/">На главную</NuxtLink> /
                        <NuxtLink class="navbar-brand" to="/">Забыли пароль?</NuxtLink> /
                        <NuxtLink class="navbar-brand" to="/">Регистрация</NuxtLink>
                    </div>
                </template>
            </LayoutCard>
        </div>
    </div>
</template>