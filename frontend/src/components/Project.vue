<template>
    <div class="container-fluid bg-success pb-5">
        <br><br>
        <h4 class="text-uppercase fw-bold text-center">My Project</h4>
        <hr class="mx-auto" style="border:4px solid red" width="100px">

        <div id="rowproject" class="row row-cols-md-3 row-cols-sm-1">
                <div class="col my-2">
                    <div class="card ms-2 bg-warning" style="width: 18rem;">
                        <img src="../assets/project/wdangtehseeker-website.png" class="card-img-top" alt="...">
                        <div class="card-body text-light">
                            <h5 class="card-title">N77 Universal Website</h5>
                            <hr>
                            <p class="card-text">Tailwind based SPA with API JSON Project Using React and Vite. This website created For repairer team,join artwork, and stories writer.</p>
                            <a href="https://github.com/WdangTehSeeker3245/n77-universal-website-frontend" class="btn btn-primary">Visit Project</a>
                        </div>
                    </div>
                </div>
                <div class="col my-2">
                    <div class="card ms-2 bg-warning" style="width: 18rem;">
                        <img src="../assets/project/izaus-linux.png" class="card-img-top" alt="...">
                        <div class="card-body text-light">
                            <h5 class="card-title">Izaus Linux</h5>
                            <hr>
                            <p class="card-text">Linux theming and app project focused around ubuntu and archlinux user.</p>
                            <a href="https://bitbucket.org/faizalnurulfirdaus_code/izaus-linux-dev/src/master/" class="btn btn-primary">Visit Project</a>
                        </div>
                    </div>
                </div>
                <div class="col my-2">
                    <div class="card ms-2 bg-warning" style="width: 18rem;">
                        <img src="../assets/project/my-lapak.png" class="card-img-top" alt="...">
                        <div class="card-body text-light">
                            <h5 class="card-title">My Lapak App</h5>
                            <hr>
                            <p class="card-text">Static site website connected with admin dashboard API that all of it basically collection of stuff i want to pawned.</p>
                            <a href="#" class="btn btn-primary">Visit Project</a>
                        </div>
                    </div>
                </div>
                <div class="col my-2">
                    <div class="card ms-2 bg-warning" style="width: 18rem;">
                        <img src="../assets/project/flaskwebnote.png" class="card-img-top" alt="...">
                        <div class="card-body text-light">
                            <h5 class="card-title">Webnote</h5>
                            <hr>
                            <p class="card-text">Website note taking app for saving draft my story on localhost, Build Using Flask or PHP pure. now working on api to syncronize with local app.</p>
                            <a href="https://github.com/WdangTehSeeker3245/flasknote-api" class="btn btn-primary">Visit Project</a>
                        </div>
                    </div>
                </div>
        </div>
    </div>
</template>

<style>
    #rowproject {
        margin-left: 50px;
    }
    @media (max-width:526px){
        #rowproject {
            margin-left: 10px;
        }
    }
</style>