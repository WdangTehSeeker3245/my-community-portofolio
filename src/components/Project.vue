<script>
export default {
    mounted() {
        this.$nextTick(() => {
            AOS.refresh()
        })
    },
    methods: {
        // MyLapak
        mylapakAdmin(){
            window.location.href = 'https://github.com/WdangTehSeeker3245/admin-mylapak'
        },
        mylapakBackend(){
            window.location.href = 'https://github.com/WdangTehSeeker3245/backend-ci4-mylapak'
        },
        mylapakFrontend(){
            window.location.href = 'https://github.com/WdangTehSeeker3245/frontend-mylapak'
        },
        // Webnote
        webnoteFlask() {
            window.location.href = 'https://github.com/WdangTehSeeker3245/flask-note-webapp';
        },
        webnotePHP() {
            window.location.href = 'https://github.com/WdangTehSeeker3245/webnote';
        }
    }
}
</script>

<template>
    <div class="container-fluid pb-5">
        <br /><br />
        <h4 class="text-uppercase fw-bold text-center">My Project</h4>
        <hr class="mx-auto" style="border: 4px solid red" width="100px" />

        <div id="rowproject" class="row row-cols-md-3 row-cols-sm-1 card-row">
            <div class="col my-2">
                <div class="card ms-2 bg-warning" style="width: 18rem" data-aos="fade-up">
                    <img src="../assets/project/wdangtehseeker-website.png" class="card-img-top" alt="..." />
                    <div class="card-body text-light">
                        <h5 class="card-title">N77 Universal Website</h5>
                        <hr />
                        <p class="card-text">
                            My Personal Project Website Created With Tailwind CSS and React
                        </p>
                        <a href="https://github.com/WdangTehSeeker3245/n77-universal-website-frontend"
                            class="btn btn-primary">Visit Project</a>
                    </div>
                </div>
            </div>
            <div class="col my-2">
                <div class="card ms-2 bg-warning" style="width: 18rem" data-aos="fade-up">
                    <img src="../assets/project/izaus-linux.png" class="card-img-top" alt="..." />
                    <div class="card-body text-light">
                        <h5 class="card-title">Izaus Linux</h5>
                        <hr />
                        <p class="card-text">
                            Linux theming and app project focused around ubuntu and archlinux
                            user.
                        </p>
                        <a href="https://bitbucket.org/faizalnurulfirdaus_code/izaus-linux-dev/src/master/"
                            class="btn btn-primary">Visit Project</a>
                    </div>
                </div>
            </div>
            <div class="col my-2">
                <div class="card ms-2 bg-warning" style="width: 18rem" data-aos="fade-up">
                    <img src="../assets/project/my-lapak.png" class="card-img-top" alt="..." />
                    <div class="card-body text-light">
                        <h5 class="card-title">My Lapak</h5>
                        <hr />
                        <p class="card-text">
                            Website to sell used item,service,and pawning
                        </p>
                        <a href="#" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#mylapakModal">Visit
                            Project</a>
                    </div>
                </div>
            </div>
            <div class="col my-2">
                <div class="card ms-2 bg-warning" style="width: 18rem" data-aos="fade-up">
                    <img src="../assets/project/flaskwebnote.png" class="card-img-top" alt="..." />
                    <div class="card-body text-light">
                        <h5 class="card-title">Webnote</h5>
                        <hr />
                        <p class="card-text">
                            Website note taking app for saving draft my story on localhost.
                        </p>
                        <a href="#" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#webnoteModal">Visit
                            Project</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- Modal My Lapak-->
    <div class="modal fade" id="mylapakModal" tabindex="-1" aria-labelledby="mylapakModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="mylapakModalLabel">My Lapak</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="project-detail-con pt-4 pb-2 mb-2" @click="mylapakAdmin">
                        <center>
                            <img class="project-img" src="../assets/sbadmin.png" />
                            <img class="project-img" src="../assets/jquery.png" />
                        </center>
                        <p class="text-center text-white fw-bold">Admin Using SBadmin Ver 1 and Jquery</p>
                    </div>
                    <div class="project-detail-con pt-4 pb-2 mb-2" @click="mylapakBackend">
                        <center>
                            <img class="project-img" src="../assets/ci.png" />
                        </center>
                        <p class="text-center text-white fw-bold">Backend Api Using Codeigniter 4</p>
                    </div>
                    <div class="project-detail-con pt-4 pb-2 mb-2" @click="mylapakFrontend">
                        <center>
                            <img class="project-img" src="../assets/bootstrap.png" />
                            <img class="project-img" src="../assets/jquery.png" />
                        </center>
                        <p class="text-center text-white fw-bold">Frontend Using Bootstrap and Jquery</p>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                        Close
                    </button>
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
                    <div class="project-detail-con pt-4 pb-2 mb-2" @click="webnoteFlask">
                        <center>
                            <img class="project-img" src="../assets/flask.png" />
                        </center>
                        <p class="text-center text-white fw-bold">Made Using Flask</p>
                    </div>
                    <div class="project-detail-con pt-4 pb-2 mb-2" @click="webnotePHP">
                        <center>
                            <img class="project-img" src="../assets/php.png" />
                        </center>
                        <p class="text-center text-white fw-bold">Made Using PHP Native</p>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                        Close
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
#rowproject {
    margin-left: 50px;
}

.project-detail-con {
    background-color: darkorange;
}

.project-detail-con:hover {
    background-color: orange;
    cursor: pointer;
}

.project-img {
    width: 80px;
    height: 80px;
}

@media (max-width: 526px) {
    #rowproject {
        margin-left: 5px;
    }
}
</style>
