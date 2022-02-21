/* eslint-disable @typescript-eslint/no-explicit-any */
import { createStore } from 'vuex'

export default createStore({
  state: {
    cart: {
      items: <any>[]
    },
    isAuthenticated: false,
    isLoading: false,
    token: ''
  },
  getters: {
  },
  mutations: {

    initializeStore(state) {
      if (localStorage.getItem('cart')) {
        state.cart = JSON.parse(localStorage.getItem('cart') || '{}')
      } else {
        localStorage.setItem('cart', JSON.stringify(state.cart))
      }
    },

    addToCart(state, item) {
      const exists = state.cart.items.filter((i: { product: { id: any } }) => i.product.id === item.product.id)

      if (exists.length) {
        exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
      }else{
        state.cart.items.push(item)
      }
      
      localStorage.setItem('cart', JSON.stringify(state.cart))
    },

    setIsLoading(state, status){
      state.isLoading = status
    }
  },
  actions: {
  },
  modules: {
  }
})
