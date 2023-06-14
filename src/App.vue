<script>
import Header from './components/Header.vue'
import About from './components/About.vue'
import TechStack from './components/TechStack.vue'
import Project from './components/Project.vue'
import Product from './components/Product.vue'
import ApiProduct from './components/ApiProduct.vue'
import Contact from './components/Contact.vue'
import Preloader from './components/Preloader.vue';

export default {
    components: {
      Preloader,About,TechStack,Header,Project,Product,ApiProduct,Contact
    },
    data() {
      return {
        loading: true,
      };
    },
    mounted() {
      setTimeout(() => {
        this.loading = false;
      }, 5000);
    },
};
</script>

<template>
  <Preloader v-if="loading" />
  <div v-if="!loading">
    <Header/>
    <About/>
    <TechStack/>
    <Project/>
    <Product/>
    <ApiProduct/>
    <Contact/>
  </div>
</template>

<style scoped>

</style>
