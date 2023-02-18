import { createRouter, createWebHistory } from "vue-router";

const routes = [
    {
        path: '/',
        component: () => import('../views/init.vue'),
        meta: {
            name: '打开文件'
        }
    }, {
        path: '/mark',
        component: () => import('../views/home.vue'),
        meta: {
            name: '标注系统'
        }
    },
]

const router = createRouter({
    // history: createWebHistory(),
    history: createWebHistory("/mark/"),
    routes,
})

export default router