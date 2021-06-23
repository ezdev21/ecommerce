import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter);
export default new VueRouter({
  mode:'history',
  routes:[
    {
      path:'/products/:category',
      name:'category',
      component:()=>require('./components/categoryComponent')
    }
  ]
})
