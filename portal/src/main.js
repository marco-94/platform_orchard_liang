// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Tabs from "./components/left-tab/tab";
import headers from "./components/top-headers/headers";
import pages from "./components/bottom-pages/pages";

Vue.prototype.$http = axios;
Vue.use(ElementUI, { size: 'small', zIndex: 3000 });
Vue.use(Tabs);
Vue.use(headers);
Vue.use(pages);

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
});
