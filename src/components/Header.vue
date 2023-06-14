<script>
import { gsap } from'gsap';

export default {
    methods:{
        toResume(){
            location.replace("https://drive.google.com/file/d/13wtVkP1cToeC-Pk08ySDeWR8h123_2du/view?usp=sharing");
        },
        toCertificate(){
            location.replace("https://drive.google.com/drive/folders/1WzlLIsbrWlQajnbMZLP3Xo8p0wCGwpGC?usp=sharing");
        }
    },
    mounted() {
        const pp = document.querySelector('.photo-profile');
        gsap.set(pp, { opacity: 0 });
        gsap.set('.mycontact', { opacity: 0 });
        gsap.fromTo(pp, { opacity: 0, x: -100, scale: 0.5 }, { opacity: 1, x: 0, scale: 1, duration: 1 });
        gsap.fromTo('.mycontact', { opacity: 0, x: -100, scale: 0.5 }, { opacity: 1, x: 0, scale: 1, duration: 1 });
    },
}

</script>
<template>
    <div>
        <nav class="navbar navbar-expand-lg bg-primary">
            <div class="container-fluid">
                <a class="navbar-brand text-light text-uppercase fw-bold" href="#">Faizal Portofolio</a>
            </div>
        </nav>
        <div class="container-fluid style-header">
            <center>
                <img class="photo-profile" src="../assets/faizal-nurul-firdaus.jpg" alt="">
                <h4 class="mt-5 fw-bold description">Hi Im Programmer Who do Code As Hobby for Long Life Learner</h4>
                <br>
                <a class="mx-2 " href="https://github.com/WdangTehSeeker3245"><i class="mycontact fa-brands fa-github fa-xl"></i></a>
                <a class="mx-2 " href="https://www.linkedin.com/in/faizal-nurul-firdaus-8448a0238"><i class="mycontact fa-brands fa-linkedin fa-xl"></i></a>
                <a class="mx-2 " href="mailto:faizaln77izaus@gmail.com"><i class="mycontact fa-solid fa-envelope fa-xl"></i></a>
                <a class="mx-2 " href="https://www.instagram.com/faizalnf8037"><i class="mycontact fa-brands fa-instagram fa-xl"></i></a>
                <a class="mx-2 " href="https://www.youtube.com/@faizalnurulfirdaus7847"><i class="mycontact fa-brands fa-youtube fa-xl"></i></a>
                <a class="mx-2 " href="https://www.facebook.com/profile.php?id=100088498143378"><i class="mycontact fa-brands fa-facebook fa-xl"></i></a>
                <a class="mx-2 " href="https://twitter.com/AsankaLigar1800"><i class="mycontact fa-brands fa-twitter fa-xl"></i></a>
                <br><br>
                <button class="btn btn-primary fw-bold mx-2" type="button" @click="toResume">Resume</button>
                <button class="btn btn-primary fw-bold mx-2" type="button" @click="toCertificate">Certification</button>
            </center>
        </div>
    </div>   
</template>

<style>
.photo-profile {
    width: 250px;
    height: 250px;
    margin-top: 100px;
    border-radius: 50%;
    border: 3px solid aqua
}
.description {
    margin-top: 80px;
    font-size: 20px;
    text-shadow: #FC0 1px 0 10px;
}
.style-header {
    background-image: url('../assets/background.jpg');
    background-repeat: no-repeat;
    background-size: cover;
    height: 700px;
}
</style>
