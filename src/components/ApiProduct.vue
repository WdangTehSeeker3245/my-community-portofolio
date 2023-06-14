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
        <h4 class="text-uppercase fw-bold text-center">My Api Product</h4>
        <hr class="mx-auto" style="border:4px solid red" width="100px">
        
        <div class="con" data-aos="fade-up">
            <div class="con-api bg-warning">
                <div class="row">
                    <div class="col-2">
                        <img class="img-api" src="../assets/api-product/notes.png">
                    </div>
                    <div class="col-10">
                        <h4 class="text-light fw-bold mt-2">Flask Note API</h4>
                        <hr class="hr-api">
                        <div class="mt-3">
                            <span class="tag bg-success py-2 px-2 me-2 mt-2 text-light rounded">Flask</span>
                            <span class="tag bg-success py-2 px-2 me-2 mt-2 text-light rounded">SqlAlchemy</span>
                            <span class="tag bg-success py-2 px-2 me-2 mt-2 text-light rounded">REST</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="con-option text-light">
                <center>
                    <a href="#" class="btn btn-primary me-2 mt-4" data-bs-toggle="modal" data-bs-target="#flasknoteapiModal" >Endpoint</a>
                    <a href="https://github.com/WdangTehSeeker3245/flasknote-api" class="btn btn-primary mt-4">Visit Api Product</a>
                </center>
            </div>
        </div>
        
    </div>
    <!-- Modal Flask Note-->
    <div class="modal fade" id="flasknoteapiModal" tabindex="-1" aria-labelledby="flasknoteapiModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="flasknoteapiModalLabel">Flask Note API</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <table class="table table-bordered">
                    <thead class="table-head">
                        <tr> 
                            <th class="table-head">Method</th>
                            <th class="table-head">Endpoint</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>GET</td>
                            <td>
                                api/notes<br>
                                api/search?title_note=[query]
                            </td>
                        </tr>
                        <tr>
                            <td>GET</td>
                            <td>api/note/:id</td>
                        </tr>
                        <tr>
                            <td>POST</td>
                            <td>api/notes</td>
                        </tr>
                        <tr>
                            <td>PUT</td>
                            <td>api/note/:id</td>
                        </tr>
                        <tr>
                            <td>DELETE</td>
                            <td>api/note/:id</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <a href="https://github.com/WdangTehSeeker3245/flasknote-api" class="btn btn-primary">Visit Api Product</a>
            </div>
            </div>
        </div>
    </div> 
</template>

<style scoped>
.con-api {
    padding:30px;
}

.con-option {
    background-color: brown;
    height: 80px;
}

.img-api {
    height: 100px;
    width: 100px;
    margin-left: 50px;
    margin-top: 5px;
}

.hr-api {
    width:100%;
    border:2px solid white
}

.tag {
    display: inline-block;
}

.table-head {
    background-color: orange; /* Replace with your desired color */
    color: white; /* Replace with your desired text color */
}

@media (max-width:526px){
    .img-api {
        height: 50px;
        width: 50px;
        margin-left: 0px;
        margin-top: 5px;
        padding-right: 5px;
    }
}
</style>