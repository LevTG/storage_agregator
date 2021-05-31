import Vue from 'vue'
import Router from 'vue-router'
import { normalizeURL, decode } from 'ufo'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _46b75784 = () => interopDefault(import('../pages/Partners.vue' /* webpackChunkName: "pages/Partners" */))
const _4a7a51b8 = () => interopDefault(import('../pages/Storage.vue' /* webpackChunkName: "pages/Storage" */))
const _6a72e834 = () => interopDefault(import('../pages/partners/CreateAdd.vue' /* webpackChunkName: "pages/partners/CreateAdd" */))
const _7f2b3260 = () => interopDefault(import('../pages/partners/Lk.vue' /* webpackChunkName: "pages/partners/Lk" */))
const _c7341efa = () => interopDefault(import('../pages/partners/Reg.vue' /* webpackChunkName: "pages/partners/Reg" */))
const _0a9b4c22 = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

const emptyFn = () => {}

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: '/',
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/Partners",
    component: _46b75784,
    name: "Partners"
  }, {
    path: "/Storage",
    component: _4a7a51b8,
    name: "Storage"
  }, {
    path: "/partners/CreateAdd",
    component: _6a72e834,
    name: "partners-CreateAdd"
  }, {
    path: "/partners/Lk",
    component: _7f2b3260,
    name: "partners-Lk"
  }, {
    path: "/partners/Reg",
    component: _c7341efa,
    name: "partners-Reg"
  }, {
    path: "/",
    component: _0a9b4c22,
    name: "index"
  }],

  fallback: false
}

export function createRouter (ssrContext, config) {
  const base = (config._app && config._app.basePath) || routerOptions.base
  const router = new Router({ ...routerOptions, base  })

  // TODO: remove in Nuxt 3
  const originalPush = router.push
  router.push = function push (location, onComplete = emptyFn, onAbort) {
    return originalPush.call(this, location, onComplete, onAbort)
  }

  const resolve = router.resolve.bind(router)
  router.resolve = (to, current, append) => {
    if (typeof to === 'string') {
      to = normalizeURL(to)
    }
    return resolve(to, current, append)
  }

  return router
}
