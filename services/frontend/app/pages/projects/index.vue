<script setup>
const runtimeConfig = useRuntimeConfig()
const paginationPageNumber = ref(1)
let url = "baseURL" in runtimeConfig ? runtimeConfig.baseURL + 'project/' : window.location.origin + '/api/project/'

const { data, status, error, pending } = await useFetch(url, {
    query: {
        page: paginationPageNumber,
        // sort_price_order: sortPriceOrder,
    },
    // lazy: true,
})
console.log(data)
const countFlats = computed(() => {
    if (status.value == "success") {
        // globalCounter1.value = data.value["count"]
        return data.value["count"]
    }
})

</script>
<template>
    <div class="flex flex-col gap-3">
        <div class="block my-3">
            <UPagination v-model:page="paginationPageNumber" :total="countFlats" />
        </div>
        <div class="grid grid-cols-12 gap-3">
            <div class="col-span-9">
                <div class="flex flex-col gap-3" v-if="data">
                    <LayoutCard v-for="item in data.results" :key="item.id">
                        <template #title>
                            <LayoutTitle class="text-xl">
                                {{ item.title }}
                            </LayoutTitle>
                        </template>
                        <template #description>
                            {{ item.description }}
                        </template>
                    </LayoutCard>
                </div>

            </div>
            <div class="col-span-3">
                <LayoutSidebarRight>
                    <LayoutCard>
                        <template #title>
                            <LayoutTitle class="text-2xl">Title 1</LayoutTitle>
                        </template>
                        <template #description>
                            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nesciunt adipisci necessitatibus
                            nostrum, maiores aliquid soluta laudantium at, minima molestiae commodi praesentium est
                            officia eius quae reprehenderit quibusdam rem distinctio accusantium.
                        </template>
                    </LayoutCard>
                </LayoutSidebarRight>
            </div>
        </div>
    </div>
</template>