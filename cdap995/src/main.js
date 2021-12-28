import Vue from 'vue'
import VueRouter from 'vue-router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import App from './App.vue'
import {routes} from "./routes"

Vue.use(VueRouter)
Vue.use(ElementUI)
Vue.config.productionTip = false

var router = new VueRouter({
  mode:'history',
  base:__dirname,
  routes
});

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
