<script setup>
// Set layout for this page
definePageMeta({
    layout: 'test'
})
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
                <ButtonsGreen class="text-3xl border-4">Хочу в команду!</ButtonsGreen>
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

        <div class="flex justify-center">
            <LayoutText>
                <template #header-primary>
                    <LayoutTitle class="text-5xl font-bold underline">
                        Header Primary
                    </LayoutTitle>
                </template>
                <template #header-secondary>
                    <LayoutTitle class="text-2xl">
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Laborum ea dignissimos eveniet expedita
                        in officiis quisquam, blanditiis ipsum pariatur tempore. Odio dicta esse cum totam. Facere
                        accusamus quae placeat labore?
                    </LayoutTitle>
                </template>
            </LayoutText>
        </div>

        <div class="flex justify-center gap-5">
            <LayoutCard v-for="index in 3" :key="index">
                <template #title>
                    <LayoutTitle class="text-2xl">Title {{ index }}</LayoutTitle>
                </template>
                <template #description>
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam itaque fuga ratione? Nostrum,
                    suscipit natus reiciendis, delectus officiis minima consequatur illum optio consectetur blanditiis
                    saepe eius culpa officia at. Id.
                </template>
            </LayoutCard>
        </div>



        <div class="flex justify-center">
            <LayoutText>
                <template #header-primary>
                    <LayoutTitle class="text-5xl font-bold underline">
                        Header Primary
                    </LayoutTitle>
                </template>
                <template #header-secondary>
                    <LayoutTitle class="text-2xl">
                        Lorem ipsum dolor sit amet consectetur adipisicing elit
                    </LayoutTitle>
                </template>
            </LayoutText>
        </div>

        <div class="grid grid-cols-3 gap-5">
            <LayoutCard v-for="index in 6" :key="index">
                <template #title>
                    <LayoutTitle class="text-2xl">Title {{ index }}</LayoutTitle>
                    <!-- <TitlesRegularNormal></TitlesRegularNormal> -->
                </template>
                <template #description>
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusamus excepturi et nostrum. Eius non,
                    sit
                    excepturi dicta libero ratione voluptate facere quam cumque obcaecati exercitationem ullam rem
                    sapiente,
                    ad itaque.
                </template>
            </LayoutCard>
        </div>
    </div>

</template>