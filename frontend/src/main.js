import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import 'bootstrap'
import 'bootswatch/dist/cosmo/bootstrap.css'
import 'fontawesome-free/css/all.css'
import { Vue3Mq } from "vue3-mq";
const app = createApp(App);

app.use(Vue3Mq, {
    preset: 'bootstrap5'
})
    .mount('#app')
