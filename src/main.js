import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import 'animate.css';
import 'bootstrap'
import 'bootswatch/dist/cosmo/bootstrap.css'
import '@fortawesome/fontawesome-free/css/all.css'

import { gsap } from "gsap";

import AOS from 'aos'
import 'aos/dist/aos.css'

const app = createApp(App);
app.use(gsap)
app.mount('#app')

AOS.init({
    offset: 200,
    duration: 600,
    easing: 'ease-in-sine',
    delay: 100,
})