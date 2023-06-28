import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)

//import categoryComponent from './components/categoryComponent.vue'

const router = new VueRouter({
  mode:'history',
  base: process.env.BASE_URL,
  routes:[
    {
      // path:'/products/:categoryName',
      // name:'category',
      // component:categoryComponent
    }
  ]
})
//export default router;