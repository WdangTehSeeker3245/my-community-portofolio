<script>

export default {
    methods:{
        tolinkedin(){
            location.replace("https://www.linkedin.com/in/faizal-nurul-firdaus-8448a0238/");
        }
    }
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
                <img class="photo-profile" src="../assets/faizal_ozeroki_virus.jpg" alt="">
                <h4 class="mt-5 fw-bold description">"Hi Im Programmer Who do Code As Hobby for Long Life Learner"</h4>
                <br>
                <a class="mx-2" href="https://github.com/WdangTehSeeker3245"><i class="fa-brands fa-github fa-xl"></i></a>
                <a class="mx-2" href="mailto:faizaln77izaus@gmail.com"><i class="fa-solid fa-envelope fa-xl"></i></a>
                <a class="mx-2" href="https://www.instagram.com/faizalnf8037"><i class="fa-brands fa-instagram fa-xl"></i></a>
                <a class="mx-2" href="https://www.youtube.com/@faizalnurulfirdaus7847"><i class="fa-brands fa-youtube fa-xl"></i></a>
                <a class="mx-2" href="https://www.facebook.com/profile.php?id=100088498143378"><i class="fa-brands fa-facebook fa-xl"></i></a>
                <a class="mx-2" href="https://twitter.com/AsankaLigar1800"><i class="fa-brands fa-twitter fa-xl"></i></a>
                <br><br>
                <button class="btn btn-primary fw-bold" type="button" data-bs-toggle="modal" data-bs-target="#exampleModal"> Check My Specialization In Progress</button>
            </center>
        </div>
    </div>
    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Specialization Rank</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <div class="row" >
                    <div class="col my-2">
                        <center>
                            <img class="specialization-img" src="../assets/flask.png" alt="">
                        </center>
                    </div>
                    <div class="col-8 my-2">
                        <p>Beginner To Intermediate</p>
                        <div class="skill-con">
                            <div class="flask text-light">35%</div>
                        </div>
                    </div>
                </div>
                <div class="row" >
                    <div class="col my-2">
                        <center>
                            <img class="specialization-img" src="../assets/vue.svg" alt="">
                        </center>
                    </div>
                    <div class="col-8 my-2" >
                        <p>Beginner</p>
                        <div class="skill-con">
                            <div class="vue text-light">15%</div>
                        </div>
                    </div>
                </div>
                <div class="row" >
                    <div class="col my-2" >
                        <center>
                            <img class="specialization-img" src="../assets/reactjs.png" alt="">
                        </center>
                    </div>
                    <div class="col-8 my-2" >
                        <p>Newbie Beginner</p>
                        <div class="skill-con">
                            <div class="react text-light">5%</div>
                        </div>
                    </div>
                </div>
                <div class="row" >
                    <div class="col" >
                        <center>
                            <img class="specialization-img" src="../assets/java.png" alt="">
                        </center>
                    </div>
                    <div class="col-8">
                        <p>Intermadiate but Long not Touch</p>
                        <div class="skill-con">
                            <div class="java text-light"> 35%</div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" @click="tolinkedin">View Resume</button>
            </div>
            </div>
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

.specialization-img{
    width: 80px;
    height: 80px;
    border-radius: 50%;
    background-color: black;
    padding: 5px;
}

.skill-con {
    width:100%;
    background-color: #ddd;
}

.flask {width: 35%; background-color: #f44336;}
.vue {width: 15%; background-color: #f44336;}
.react {width: 5%; background-color: #f44336;}
.java {width: 35%; background-color: #f44336;}
</style>
