import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Show = () => import('@/views/show/index.vue')
const Repertoire = () => import('@/views/repertoire/index.vue')
const Rehearsal = () => import('@/views/rehearsal/index.vue')
const Actor = () => import('@/views/actor/index.vue')
const Band = () => import('@/views/band/index.vue')
const Stage = () => import('@/views/stage/index.vue')
const Lighting = () => import('@/views/lighting/index.vue')
const Sound = () => import('@/views/sound/index.vue')
const Costume = () => import('@/views/costume/index.vue')
const Makeup = () => import('@/views/makeup/index.vue')
const Tour = () => import('@/views/tour/index.vue')
const Freight = () => import('@/views/freight/index.vue')
const Loadin = () => import('@/views/loadin/index.vue')
const Safety = () => import('@/views/safety/index.vue')
const Showlog = () => import('@/views/showlog/index.vue')
const Settle = () => import('@/views/settle/index.vue')
const Permit = () => import('@/views/permit/index.vue')
const Media = () => import('@/views/media/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/show', name: 'show', component: Show },
    { path: '/repertoire', name: 'repertoire', component: Repertoire },
    { path: '/rehearsal', name: 'rehearsal', component: Rehearsal },
    { path: '/actor', name: 'actor', component: Actor },
    { path: '/band', name: 'band', component: Band },
    { path: '/stage', name: 'stage', component: Stage },
    { path: '/lighting', name: 'lighting', component: Lighting },
    { path: '/sound', name: 'sound', component: Sound },
    { path: '/costume', name: 'costume', component: Costume },
    { path: '/makeup', name: 'makeup', component: Makeup },
    { path: '/tour', name: 'tour', component: Tour },
    { path: '/freight', name: 'freight', component: Freight },
    { path: '/loadin', name: 'loadin', component: Loadin },
    { path: '/safety', name: 'safety', component: Safety },
    { path: '/showlog', name: 'showlog', component: Showlog },
    { path: '/settle', name: 'settle', component: Settle },
    { path: '/permit', name: 'permit', component: Permit },
    { path: '/media', name: 'media', component: Media },
  ],
})

export default router
