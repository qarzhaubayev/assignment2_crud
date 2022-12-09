
const routes = [
    {path:"/", component:main},
    {path:"/diseasetype", component:diseasetype},
    {path:"/country", component:country},
    {path:"/disease", component:disease},
    {path:"/discover", component:discover},
    {path:"/users", component:users},
    {path:"/publicservant", component:publicservant},
    {path:"/doctor", component:doctor},
    {path:"/specialize", component:specialize},
    {path:"/record", component:record}
]


// import router from './router'
const router = VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    routes
  })
  const app = Vue.createApp({})
  app.use(router)
  app.mount('#app')
