import Vue from 'vue'
import Router from 'vue-router'
import Home from "../pages/Home.vue";
import ProductList from '../pages/ProductList.vue'
import ProductDetails from '../pages/ProductDetails.vue'
import ProductEdit from '../pages/ProductEdit.vue'
import productAdd from "../pages/productAdd.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/product',
      name: 'product_list',
      component: ProductList,
      meta: {
        pagesShow: true
      }
    },
    {
      path: '/product_details',
      name: 'product_details',
      component: ProductDetails,
    },
    {
      path: '/product_edit',
      name: 'product_edit',
      component: ProductEdit,
    },
    {
      path: '/product_add',
      name: 'product_add',
      component: productAdd,
    },
  ]
})
