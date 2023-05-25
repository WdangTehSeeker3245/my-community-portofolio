<script>
import axios from 'axios';

export default {
  data() {
    return {
      formData: {
        subject: "",
        content: "",
      }
    }
  },
  methods: {
    // async submitForm() {
    //       axios({
    //         method: "POST",
    //         url: "http://localhost:5000/api/sendemail",
    //         data: {
    //           subject: this.formData.subject,
    //           content: this.formData.content,
    //         },
    //         headers: { "Content-Type": "multipart/form-data" },
    //       })
    //       .then(function (response) {
    //         console.log(response)
    //         alert(response.data.msg)
    //       })
    //       .catch(function (error) {
    //         console.log(error)
    //         alert(error)
    //       });
    // }
    async submitForm() {
      axios.defaults.headers.post['Content-Type'] = 'application/json';
      axios.post('https://formsubmit.co/ajax/faizalnf3245@gmail.com', {
          name: this.formData.subject,
          message: this.formData.content
      })
          .then(response => alert(response))
          .catch(error => alert(error));
          }
        },
    }
</script>
<template>
    <div class="bg-warning container-fluid">
     <br>
     <div class="mx-auto responsive-contact">
        <h4 class="text-center text-white text-uppercase fw-bold">Contact Me</h4>
        <hr style="border: 4px solid white ; width:100px" class="mx-auto">
        <br>
        <br>

        <!-- Using Formsubmit.co -->
        <!-- <form  class="px-4" action="https://formsubmit.co/faizalnf3245@gmail.com" method="POST">
            <div class="mb-4">
                <input id="subject" name="subject" class="form-control" type="text" placeholder="Subject" />
            </div>
            <div class="mb-4">
                <textarea id="content" name="content" class="form-control" rows="10" cols="50" placeholder="Content" ></textarea>
            </div>
            <center>
                <button type="submit" class="btn btn-primary mb-5"><i class="fa-solid fa-envelope me-2"></i>SEND</button>
            </center>
        </form> -->

        <!-- Using Axios -->
        <form @submit.prevent="submitForm" class="px-4">
            <div class="mb-4">
                <input id="subject" class="form-control" v-model="formData.subject" type="text" placeholder="Subject" />
            </div>
            <div class="mb-4">
                <textarea id="content" class="form-control" v-model="formData.content" rows="10" cols="50" placeholder="Content" ></textarea>
            </div>
            <center>
                <button type="submit" class="btn btn-primary mb-5"><i class="fa-solid fa-envelope me-2"></i>SEND</button>
            </center>
        </form>
     </div>
    </div>
     
</template>
<style>
.responsive-contact {
    width:380px;
}
.responsive-yt {
    width:480px;
    height: 280px;
}
.responsive-lets {
    width:480px;
    border:4px solid red;
}
@media (max-width: 526px) {
    .responsive-yt {
        width: 100%;
        height: 280px;
    }
    .responsive-lets {
        width:100%;
        border:4px solid red;
    }
    .responsive-contact {
        width:100%;
    }
}
</style>