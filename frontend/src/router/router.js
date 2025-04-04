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
    meta: { noonAuth: true },
  },
  {
    path: "/auth/Organisation",
    component: authOrg,
    meta: { noonAuth: true },
  },
  {
    path: "/registration/Organisation",
    component: regOrg,
    meta: { noonAuth: true },
  },
  {
    path: "/registration/Client",
    component: regCli,
    meta: { noonAuth: true },
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
    return decodeJwt(token);
  }

  const token = localStorage.getItem("token");
  if (token && to.meta.noonAuth) {
    if (from.path && ["/auth/Client", "/auth/Organisation", "/registration/Client", "/registration/Organisation"].includes(from.path)) {
      next("/");
    } else {
      next(from.path || "/");
    }
    return;
  }

  if (!token && to.meta.requiresAuth && !to.meta.requireAdmin) {
    next("/auth/Client");
    return;
  }

  if (!token && to.meta.requireAdmin) {
    next("/auth/Organisation");
    return;
  }

  const data = getCustomClaims(token);
  if (data && to.meta.requiresAuth && data.access !== "organizer") {
    next("/auth/Client");
    return;
  }

  if (data && to.meta.requireAdmin && data.access !== "organizer") {
    next("/auth/Organisation");
    return;
  }

  next();
});

export default router;
