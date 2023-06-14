<template>
    <div class="preloader">
      <div class="spinner"></div>
    </div>
</template>
  
<style scoped>
    .preloader {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background-color: lightblue;
      z-index: 9999;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    .spinner {
      width: 50px;
      height: 50px;
      border-radius: 50%;
      border: 5px solid #ccc;
      border-top-color: #888;
      animation: spinner 0.6s linear infinite;
    }
    @keyframes spinner {
      to {
        transform: rotate(360deg);
      }
    }
</style>
  