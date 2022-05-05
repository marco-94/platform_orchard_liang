import tab  from "./tab.vue";
import Vue from 'vue'
const   Tabs = {
  install: function() {
      Vue.component('Tabs', tab)
  }
};

export default Tabs;
