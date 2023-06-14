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
        <h4 class="text-uppercase fw-bold text-center">My Product</h4>
        <hr class="mx-auto" style="border:4px solid red" width="100px">

        <div id="rowproduct" class="row row-cols-md-3 row-cols-sm-1">
                <div class="col my-2">
                    <div class="card ms-2 bg-warning" style="width: 18rem;" data-aos="fade-up">
                        <img src="../assets/product/si_pariwisata.png" class="card-img-top" alt="...">
                        <div class="card-body text-light">
                            <h5 class="card-title">SI Pariwisata/Tourism</h5>
                            <hr>
                            <p class="card-text">Tourism System Information Website</p>
                            <a href="#" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#sipariwisataModal">Visit Product</a>
                        </div>
                    </div>
                </div>
        </div>
    </div>
    <!-- Modal SI Pariwsata-->
    <div class="modal fade" id="sipariwisataModal" tabindex="-1" aria-labelledby="sipariwisataModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="sipariwisataModalLabel">SI Pariwisata/Tourism</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <div class="row" >
                    <div class="col my-2">
                        <center>
                            <img class="project-img" src="../assets/php.png" alt="">
                        </center>
                    </div>
                    <div class="col-8 my-2">
                        <p class="mt-4"> 
                            Using PHP Native and Mysqli <i class="fa-solid fa-arrow-right mx-2"></i> 
                            <a href="https://github.com/WdangTehSeeker3245/php-mysqli-si-pariwisata">Link</a>
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

<style scoped>
    #rowproduct {
        margin-left: 50px;
    }
    .product-img{
        width: 80px;
        height: 80px;
        border-radius: 50%;
        background-color: black;
        padding: 5px;
    }
    @media (max-width:526px){
        #rowproduct {
            margin-left: 5px;
        }
    }
</style>