import {createRouter, createWebHistory} from "vue-router";
import mainView from "@/pages/mainView.vue";
import authOrg from "@/pages/authOrg.vue";
import authCli from "@/pages/authCli.vue";
import regCli from "@/pages/regCli.vue";
import regOrg from "@/pages/regOrg.vue";
import createEvent from "@/pages/createEvent.vue";
import eventDetails from "@/pages/eventDetails.vue";
import favoriteEvents from "@/pages/favoriteEvents.vue";

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
        path: '/events/:id',
        component: eventDetails,
        props: true
    },
    {
        path: '/favorites',
        component: favoriteEvents
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
    scrollBehavior(to, from, savedPosition) {
        if (savedPosition) {
            return savedPosition
        } else {
            return { top: 0 }
        }
    }
})

export default router