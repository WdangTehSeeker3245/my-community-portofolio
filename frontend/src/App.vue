<script>
import Header from './components/Header.vue'
import Project from './components/Project.vue'
import Contact from './components/Contact.vue'
import Preloader from './components/Preloader.vue';

export default {
    components: {
      Preloader,Header,Project,Contact
    },
    data() {
      return {
        loading: true,
      };
    },
    mounted() {
      setTimeout(() => {
        this.loading = false;
      }, 10000);
    },
};
</script>

<template>
  <Preloader v-if="loading" />
  <div v-if="!loading">
    <Header/>
    <Project/>
    <Contact/>
  </div>
</template>

<style scoped>

</style>
