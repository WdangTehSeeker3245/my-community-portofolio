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
        <h4 class="text-uppercase fw-bold text-center">My Project</h4>
        <hr class="mx-auto" style="border:4px solid red" width="100px">

        <div id="rowproject" class="row row-cols-md-3 row-cols-sm-1 card-row">
                <div class="col my-2">
                    <div class="card ms-2 bg-warning" style="width: 18rem;" data-aos="fade-up">
                        <img src="../assets/project/wdangtehseeker-website.png" class="card-img-top" alt="...">
                        <div class="card-body text-light">
                            <h5 class="card-title">N77 Universal Website</h5>
                            <hr>
                            <p class="card-text">My Personal Project Website Created With Tailwind CSS and React</p>
                            <a href="https://github.com/WdangTehSeeker3245/n77-universal-website-frontend" class="btn btn-primary">Visit Project</a>
                        </div>
                    </div>
                </div>
                <div class="col my-2">
                    <div class="card ms-2 bg-warning" style="width: 18rem;" data-aos="fade-up">
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
                    <div class="card ms-2 bg-warning" style="width: 18rem;" data-aos="fade-up">
                        <img src="../assets/project/my-lapak.png" class="card-img-top" alt="...">
                        <div class="card-body text-light">
                            <h5 class="card-title">My Lapak App</h5>
                            <hr>
                            <p class="card-text">Static site website connected with admin dashboard API that all of it basically collection of stuff i want to pawned.</p>
                            <a href="https://github.com/WdangTehSeeker3245/mylapak-fullstack" class="btn btn-primary">Visit Project</a>
                        </div>
                    </div>
                </div>
                <div class="col my-2">
                    <div class="card ms-2 bg-warning" style="width: 18rem;" data-aos="fade-up">
                        <img src="../assets/project/flaskwebnote.png" class="card-img-top" alt="...">
                        <div class="card-body text-light">
                            <h5 class="card-title">Webnote</h5>
                            <hr>
                            <p class="card-text">Website note taking app for saving draft my story on localhost.</p>
                            <a href="#" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#webnoteModal">Visit Project</a>
                        </div>
                    </div>
                </div>
        </div>
    </div>
    <!-- Modal Webnote-->
    <div class="modal fade" id="webnoteModal" tabindex="-1" aria-labelledby="webnoteModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="webnoteModalLabel">Webnote</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <div class="row" >
                    <div class="col my-2">
                        <center>
                            <img class="project-img" src="../assets/flask.png" alt="">
                        </center>
                    </div>
                    <div class="col-8 my-2">
                        <p class="mt-4"> 
                            Using Flask <i class="fa-solid fa-arrow-right mx-2"></i> 
                            <a href="https://github.com/WdangTehSeeker3245/flask-note-webapp">Link</a>
                        </p>
                    </div>
                </div>
                <div class="row" >
                    <div class="col my-2">
                        <center>
                            <img class="project-img" src="../assets/php.png" alt="">
                        </center>
                    </div>
                    <div class="col-8 my-2">
                        <p class="mt-4"> 
                            Using PHP Native <i class="fa-solid fa-arrow-right mx-2"></i> 
                            <a href="https://github.com/WdangTehSeeker3245/webnote">Link</a>
                        </p>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            </div>
            </div>
        </div>
    </div> 
</template>

<style>
    #rowproject {
        margin-left: 50px;
    }
    .project-img{
        width: 80px;
        height: 80px;
        border-radius: 50%;
        background-color: black;
        padding: 5px;
    }
    @media (max-width:526px){
        #rowproject {
            margin-left: 5px;
        }
    }
    .card-row {
        transition: transform 0.5s ease;
    }

    .card-row.animate {
        transform: translateY(0);
    }
</style>
