// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import App from './App';
import router from './router';
import {
  NavbarPlugin,
  NavPlugin,
} from 'bootstrap-vue';

Vue.config.productionTip = false;


Vue.use(NavbarPlugin);
Vue.use(NavPlugin);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
