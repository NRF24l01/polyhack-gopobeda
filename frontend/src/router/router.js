import {createRouter, createWebHistory} from "vue-router";
import mainView from "@/pages/mainView.vue";
import authOrg from "@/pages/authOrg.vue";
import authCli from "@/pages/authCli.vue";
import regCli from "@/pages/regCli.vue";
import regOrg from "@/pages/regOrg.vue";





const routes = [
    {
        path: '/',
        component: mainView
    },
    {
        path: '/auth/Client',
        component: authCli
    },
    {
        path: '/auth/Organisation',
        component: authOrg
    },
    {
        path: '/registration/Organisation',
        component: regOrg
    },
    {
        path: '/registration/Client',
        component: regCli
    },

]

const router = createRouter({
    history: createWebHistory(),
    routes

})

export default router