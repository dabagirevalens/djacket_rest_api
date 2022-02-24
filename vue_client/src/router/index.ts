import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Category from '../components/Category.vue'
import SearchComponent from '../components/Search.vue'
import CartView from '../views/CartView.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/search',
    name: 'search',
    component: SearchComponent
  },
  {
    path: '/:category_slug/:product_slug',
    name: 'Product',
    component: () => import('../views/ProductDetails.vue')
  },

  {
    path: '/:category_slug',
    name: 'Category',
    component: Category
  },

  {
    path: '/cart',
    name: 'Cart',
    component: CartView
  },

  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },


  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  }


]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
