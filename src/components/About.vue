<script>
export default {
  mounted() {
    this.$nextTick(() => {
      AOS.refresh()
    })
  }
}
</script>

<template>
    <div class="container-fluid pb-5">
        <br><br>
        <h4 class="text-uppercase fw-bold text-center">About</h4>
        <hr class="mx-auto" style="border:4px solid red" width="100px">
        <div class="about-box mx-auto mt-5 px-4 py-4" data-aos="fade-up">
            <p class="text-light">"Greetings, I am someone who studies problem-solving so that one day I can become a software engineer. I like processing in backend technology therefore my frontend is less attractive. I'm trying to get used using Python, PHP and Js for more web development mastery.learn various backend language for preparing to work as a backend web programmer."</p>
        </div>
    </div>
</template>

<style>
.about-box {
    width: 80%;
    font-size: 20px;
    text-align: center;
    background-color: orangered;
}
</style>