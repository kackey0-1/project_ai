<template>
  <v-container fluid style="width: 600px">
    <div class="mb-5">
      <h1>数値判別AI</h1>
      <h2>{{answer}}</h2>
    </div>

    <div class="mb-5" justify="center">
      <v-file-input
        show-size
        label="Select Image"
        accept="image/*"
        @change="selectImage"
      ></v-file-input>
      <v-btn color="success" dark @click="upload">Upload<v-icon right dark>mdi-cloud-upload</v-icon></v-btn>
      <div v-if="progress">
        <div>
          <v-progress-linear
            v-model="progress"
            color="light-blue"
            height="25"
            reactive
          >
            <strong>{{ progress }} %</strong>
          </v-progress-linear>
        </div>
      </div>

      <div v-if="previewImage">
        <v-img
          :src="previewImage"
        ></v-img>
      </div>
    </div>
  </v-container>
</template>
<script>
import axios from 'axios'
export default {
  name: "upload-image",
  data() {
    return {
      currentImage: undefined,
      previewImage: undefined,
      progress: 0,
      message: "",
      imageInfos: [],
      answer: "数値画像を識別します。",
    };
  },
  methods: {
    upload() {
      let formData = new FormData();

      formData.append("file", this.currentImage)
      axios.post(`${process.env.VUE_APP_API_URL}/api/v1/upload/`, formData, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      }).then(res => {
        console.log(res.data)
        this.answer = `これは、${res.data.answer} です。`
      });
    },
    selectImage(image) {
      this.currentImage = image;
      this.previewImage = URL.createObjectURL(this.currentImage);
      this.progress = 0;
      this.message = "";
    },

  }
}
</script>
