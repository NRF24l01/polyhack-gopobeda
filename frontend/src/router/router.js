import {createRouter, createWebHistory} from "vue-router";
import mainView from "@/pages/mainView.vue";
import authOrg from "@/pages/authOrg.vue";
import authCli from "@/pages/authCli.vue";
import regCli from "@/pages/regCli.vue";
import regOrg from "@/pages/regOrg.vue";
import createEvent from "@/pages/createEvent.vue";
import about from "@/pages/about.vue";
import events from "@/pages/events.vue";

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
    {
        path: '/events/create',
        component: createEvent
    },
    {
        path: '/about',
        component: about
    },
    {
        path: '/events',
        component: events
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router