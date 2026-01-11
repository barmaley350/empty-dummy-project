<script setup>
// Set layout for this page
definePageMeta({
    layout: 'test'
})

const how_its_work = {
    step1: {
        step: "1",
        url: "/",
        label: "Регистрация",
        text: "Создайте профиль и укажите свои навыки и технологии",
        icon: "",
    },
    step2: {
        step: "2",
        url: "/about",
        label: "Цели встречи",
        text: "Выберите ваши цели - менторство, обмен опытом или нетворкинг",
        icon: "i-lucide-book-open",
    },
    step3: {
        step: "3",
        url: "/about",
        label: "Подбор пары",
        text: "Алгоритм находит специалистов с совпадающими интересами",
        icon: "lucide:info",
    },
    step4: {
        step: "4",
        url: "/about",
        label: "Встреча",
        text: "Договоритесь о времени и месте для живого общения",
        icon: "lucide:info",
    },
}

const platforma = {
    step1: {
        step: "1",
        url: "/",
        label: "Проверенные специалисты",
        text: "Все участники проходят верификацию профиля",
        icon: "lucide-shield",
    },
    step2: {
        step: "2",
        url: "/about",
        label: "Быстрый подбор",
        text: "Находим подходящего собеседника за несколько минут",
        icon: "lucide-zap",
    },
    step3: {
        step: "3",
        url: "/about",
        label: "Встречи в вашем городе",
        text: "Подбираем специалистов поблизости для удобства",
        icon: "lucide-map-pin",
    },
    step4: {
        step: "4",
        url: "/about",
        label: "Обратная связь",
        text: "Оценивайте встречи и помогайте улучшать сервис",
        icon: "lucide-message-square",
    },
}
</script>


<template>
    <div class="flex flex-col gap-20">
        <div class="
            flex flex-col gap-10
            border 
            border-gray-100
            bg-gray-100 
            rounded-sm 
            p-10 
            dark:bg-gray-900
            dark:border-gray-600">
            <div class="flex justify-center text-center">
                <LayoutTitle class="text-7xl font-bold">
                    Находите IT специалистов<br>
                    для живых встреч
                </LayoutTitle>
            </div>


            <div class="flex justify-center text-center mt-5">
                <LayoutTitle class="text-2xl text-gray-500 dark:text-gray-300">
                    Укажите свои навыки и цели — мы подберём собеседника для встречи.<br>
                    Обменивайтесь опытом, находите
                    менторов, расширяйте профессиональную сеть.
                </LayoutTitle>
            </div>
            <div class="flex justify-center">
                <ButtonsGreen class="text-3xl font-bold py-3">Хочу в команду!</ButtonsGreen>
            </div>

            <div class="grid grid-cols-4 gap-5 text-center">
                <div class="border border-gray-300 p-3 rounded-sm">
                    <div class="text-3xl text-gray-600 dark:text-gray-300 font-bold">505</div>
                    <div class="text-2xl text-gray-500 dark:text-gray-300">специалистов online</div>
                </div>
                <div class="border border-gray-300 p-3 rounded-sm">
                    <div class="text-3xl text-gray-600 dark:text-gray-300 font-bold">1,247</div>
                    <div class="text-2xl text-gray-500 dark:text-gray-300">специалистов</div>
                </div>
                <div class="border border-gray-300 p-3 rounded-sm">
                    <div class="text-3xl text-gray-600 dark:text-gray-300 font-bold">3,892</div>
                    <div class="text-2xl text-gray-500 dark:text-gray-300">встреч проведено</div>
                </div>
                <div class="border border-gray-300 p-3 rounded-sm">
                    <div class="text-3xl text-gray-600 dark:text-gray-300 font-bold">105</div>
                    <div class="text-2xl text-gray-500 dark:text-gray-300">проходят сейчас</div>
                </div>
            </div>

        </div>

        <div class="flex flex-col gap-10">
            <div class="flex justify-center">
                <LayoutText>
                    <template #header_primary>
                        <LayoutTitle class="text-5xl font-bold underline">
                            Как это работает
                        </LayoutTitle>
                    </template>
                    <template #header_secondary>
                        <LayoutTitle class="text-2xl text-gray-500 dark:text-gray-300">
                            Всего несколько простых шагов и вы уже в команде
                        </LayoutTitle>
                    </template>
                </LayoutText>
            </div>

            <div class="grid grid-cols-2 gap-5">
                <div v-for="step in how_its_work" :key="step.step">
                    <div class="flex flex-row h-full gap-1">
                        <LayoutBadges
                            class="flex text-5xl px-10 bg-blue-600 text-white rounded-sm h-auto items-center font-bold">
                            {{ step.step }}
                        </LayoutBadges>
                        <LayoutCard class="h-full">
                            <template #title>
                                <LayoutTitle class="text-2xl font-bold">{{ step.label }}</LayoutTitle>
                            </template>
                            <template #description>
                                <div class="text-gray-500 dark:text-gray-300 text-xl">{{ step.text }}</div>
                            </template>
                        </LayoutCard>
                    </div>

                </div>

            </div>
        </div>


        <div class="flex flex-col gap-10">
            <div class="flex justify-center">
                <LayoutText>
                    <template #header_primary>
                        <LayoutTitle class="text-5xl font-bold underline">
                            Возможности платформы
                        </LayoutTitle>
                    </template>
                    <template #header_secondary>
                        <LayoutTitle class="text-2xl text-gray-500 dark:text-gray-300">
                            Мы создали простой и эффективный инструмент для профессионального нетворкинга
                        </LayoutTitle>
                    </template>
                </LayoutText>
            </div>

            <div class="grid grid-cols-2 gap-5">
                <div v-for="item in platforma" :key="item.step">
                    <div class="flex flex-row h-full gap-1">
                        <LayoutBadges
                            class="flex text-5xl px-8 bg-blue-600 text-white rounded-sm h-auto items-center font-bold">
                            <Icon :name=item.icon />
                        </LayoutBadges>
                        <LayoutCard class="h-full">
                            <template #title>
                                <LayoutTitle class="text-2xl font-bold">{{ item.label }}</LayoutTitle>
                            </template>
                            <template #description>
                                <div class="text-gray-500 dark:text-gray-300 text-xl">{{ item.text }}</div>
                            </template>
                        </LayoutCard>
                    </div>

                </div>

            </div>
        </div>

        <div class="flex flex-col gap-10">
            <div class="flex justify-center">
                <LayoutText>
                    <template #header_primary>
                        <LayoutTitle class="text-5xl font-bold underline">
                            Готовы начать?
                        </LayoutTitle>
                    </template>
                    <template #header_secondary>
                        <LayoutTitle class="text-2xl text-gray-500 dark:text-gray-300">
                            Присоединяйтесь к сообществу IT специалистов и находите нужные знакомства
                        </LayoutTitle>
                    </template>
                </LayoutText>
            </div>

            <div class="flex justify-center">
                <ButtonsGreen class="text-3xl font-bold py-3">Хочу в команду!</ButtonsGreen>
            </div>
        </div>
    </div>

</template>