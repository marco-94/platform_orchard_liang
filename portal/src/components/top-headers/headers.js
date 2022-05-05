import headers  from "./headers.vue";
import Vue from 'vue'
const   Headers = {
  install: function() {
      Vue.component('Headers', headers)
  }
};

export default Headers;
