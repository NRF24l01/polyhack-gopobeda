import { createRouter, createWebHistory } from "vue-router";
import mainView from "@/pages/mainView.vue";
import authOrg from "@/pages/authOrg.vue";
import authCli from "@/pages/authCli.vue";
import regCli from "@/pages/regCli.vue";
import regOrg from "@/pages/regOrg.vue";
import createEvent from "@/pages/createEvent.vue";
import EventDetails from "@/pages/EventDetails.vue";
import FavoriteEvents from "@/pages/FavoriteEvents.vue";
import notFound from "@/pages/notFound.vue";
import about from "@/pages/about.vue";
import events from "../pages/events.vue";

const routes = [
  {
    path: "/",
    component: mainView,
  },
  {
    path: "/auth/Client",
    component: authCli,
  },
  {
    path: "/auth/Organisation",
    component: authOrg,
  },
  {
    path: "/registration/Organisation",
    component: regOrg,
  },
  {
    path: "/registration/Client",
    component: regCli,
  },
  {
    path: "/events",
    component: events,
  },
  {
    path: "/events/create",
    component: createEvent,
    meta: { requiresAuth: true, requireAdmin: true },
  },
  {
    path: "/events/:id",
    component: EventDetails,
  },
  {
    path: "/favorites",
    component: FavoriteEvents,
    meta: { requiresAuth: true },
  },
  {
    path: "/about",
    component: about,
  },
  {
    path: "/:pathMatch(.*)*",
    component: notFound,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else {
      return { top: 0 };
    }
  },
});

import { jwtDecode } from "jwt-decode";

router.beforeEach((to, from, next) => {
  function decodeJwt(token) {
    try {
      return jwtDecode(token);
    } catch (error) {
      console.error("Invalid JWT", error);
      return null;
    }
  }

  function getCustomClaims(token) {
    const decoded = decodeJwt(token);
    return decoded;
  }

    const token = localStorage.getItem("token");
    if (!to.meta.requiresAuth) {
      console.log('NO AUTH')
    next();
  }
  if (!token && !to.meta.requiresAuth) {
    next("/auth/client");
  } else if (!token && to.meta.requireAdmin) {
    next("/auth/Organisation");
  }
  const data = getCustomClaims(token);

  console.log(data);
  console.log(data.access);

  if (!data.access && to.meta.requiresAuth && data.access == "organizer") {
    next("/auth/client");
  } else if (data.access != "organizer" && to.meta.requireAdmin) {
    next("/auth/organisation");
  } else {
    next();
  }
});

export default router;
