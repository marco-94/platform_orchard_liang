import pages  from "./pages.vue";
import Vue from 'vue'
const   Pages = {
  install: function() {
      Vue.component('Pages', pages)
  }
};

export default Pages;
