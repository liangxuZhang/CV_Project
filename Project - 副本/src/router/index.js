import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

import menus from '@/config/menu-config'
import Layout from '@/views/Layout'

Vue.use(Router)

let LayoutChildren = []
menus.forEach((item) => {
    LayoutChildren.push({
      path: item.name,
      name: item.name,
      meta: item.meta,
      component: () => import(`@/components/${item.name}`)
    })
})
export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component: ()=>import(`@/views/Login`)
    },
    {
      path: '/Home',
      name: 'Home',
      component: Layout,
      children: LayoutChildren
    }
  ]
})
