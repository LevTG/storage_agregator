<template>
  <div class='adding-file'>
              <div class="file-drag-drop">
                    <form v-bind:ref="id">
                        <div class='file-load__area drop-files'>
                            <div class="input__wrapper file-load__area-button">
                                <input name="file" v-bind:id="id" type="file" ref="file" class="input input__file" v-on:focus='handleFileClear()' v-on:change='handleFileUpload()' multiple>
                                <label v-bind:for="id" class="input__file-button">
                                    <span class="input__file-button-text">{{buttonName}}</span>
                                </label>
                            </div>
                        </div>
                    </form>
                </div>
                <div class="place-to-file-chosen">
                  <div v-for="item in files" :key="item.name">
                    <div class="load__img">
                      <img  class="load__img_scr"  :id="item.name"> </img>
                      <div class="delete" @click="FileRemove(item.name)">
                        <inline-svg
                            class="area-background__icon"
                            :src="require('@/assets/icons/trash.svg')"
                            width="24"
                            height="24"
                        />
                      </div>
                    </div>
                  </div>
                </div>
  </div>
</template>
<script>
import InlineSvg from 'vue-inline-svg'
import DefaultButton from '@/components/shared/DefaultButton'
export default {
  name: 'AddingFile',
  components: {
    InlineSvg,
    DefaultButton
  },
  props: { id: String, isFileWasUploaded: Boolean },
  data () {
    return {
      dragAndDropCapable: false,
      files: [],
      errorTypeFile: false,
      event: 'load-file'
    }
  },
  computed: {
    buttonName () {
      return (this.file === '') ? '+ Добавить файл' : '+ Добавить файл'
    }
  },
  watch: {
    isFileWasUploaded: function (val) {
      console.log(val)
      if (val === true) {
        this.files = ''
        this.$refs.file.value = ''
        console.log(this.$refs.file.value)
        this.$emit('isFileWasUploadedStatusChanged', false)
      }
    }
  },
  methods: {
    FileRemove(file_name){
      console.log(file_name)
      let self_file = this.files
      let index = function(){
        //console.log(self_file)
        let index = 0;
        self_file.forEach((item, i) => {
          if(item.name == file_name){
              console.log(i)
              index = i
            }
        })
        return index
      }
      console.log(index())
      this.files.splice(index(), 1)
      console.log(this.files)
    },
    addPreViewFile() {
      console.log('Добавить пикчу')
      console.log(this.files)
      this.files.forEach((item, i) => {
        console.log(item)
        if (FileReader && item) {
          console.log('Добавляем пикчу')
          var fr = new FileReader();
          fr.onload = function () {
              document.getElementById(item.name).src = fr.result;
          }
          fr.readAsDataURL(item);
        }
      });
    },
    handleFileClear () {
      console.log('yes')
    },
    handleFileUpload () {
      this.$refs.file.files.forEach((item, i) => {
        console.log(item)
        if (/\.(jpeg)$/i.test(item.name)) {
          console.log('ok')
          if(this.files.length <= 5){
            this.files.push(item)
            this.addPreViewFile()
          } else {
            this.isFull = true
            console.log('Слишком много файлов')
          }
        } else if(/\.(png)$/i.test(item.name)) {
          console.log('ok')
          if(this.files.length <= 5){
            this.files.push(item)
            this.addPreViewFile()
          } else {
            this.isFull = true
            console.log('Слишком много файлов')
          }
        } else {
          console.log('Расширение файла должно быть .xlsx')
          this.errorTypeFile = true
        }
      })
      this.$emit('load-file', this.files)
      console.log(this.files)
    },
    determineDragAndDropCapable () {
      const div = document.createElement('div')
      return (('draggable' in div) || ('ondragstart' in div && 'ondrop' in div)) && 'FormData' in window && 'FileReader' in window
    }
  },
  mounted () {
    this.dragAndDropCapable = this.determineDragAndDropCapable()
    if (this.dragAndDropCapable) {
      ['drag', 'dragstart', 'dragend', 'dragover', 'dragenter', 'dragleave', 'drop'].forEach(function (evt) {
        this.$refs[this.id].addEventListener(evt, function (e) {
          e.preventDefault()
          e.stopPropagation()
        })
      }.bind(this))
      this.$refs[this.id].addEventListener('drop', function (e) {
        if (/\.(xlsx)$/i.test(e.dataTransfer.files[0].name)) {
          console.log('ok')
          this.file = e.dataTransfer.files[0]
          this.$emit('load-file', this.file)
        } else {
          console.log('Расширение файла должно быть .xlsx')
          this.errorTypeFile = true
        }
      }.bind(this))
    }
  }
}
</script>
<style lang="scss" scoped>

.delete{
  position: absolute;
  top: 12px;
  right: 12px;
}

.delete:hover{
  cursor: pointer;
}

.place-to-file-chosen{
  display: flex;
  flex-direction: row;
  flex-wrap:  wrap;
  width: calc(100% + 40px);
}

.load__img_scr{
  height: 250px;
  width: 250px;
  object-fit: cover;
  border-radius: 8px;
  filter: brightness(50%);
}

.load__img_scr:hover{
  //filter: brightness(100%);
}


.load__img{
  position: relative;
  display: flex;
  margin-right: 20px;
  margin-bottom: 20px;
}



.place-to-file-chosen{

}
.input__wrapper {
  width: 100%;
  position: relative;
  text-align: center;
}
.input__file {
  opacity: 0;
  visibility: hidden;
  position: absolute;
}
.input__file-button-text {
  line-height: 1;
  margin-top: 1px;
}
.input__file-button {
  display: flex;
    width: 520px;
    height: 200px;
    cursor: pointer;
    justify-content: center;
    align-items: center;
}
div.file-listing{
    display: block;
    width: 215px;
    text-align: center;
    padding-bottom: 15px;
    word-break: break-all;
}
.area-background__text{
    max-width: 80px;
    text-align: center;
}
.area-background__image-top{
    padding-bottom: 10px;
    display: flex;
    align-items: center;
    justify-content: space-around;
}
.file-load__area-background{
    display: block;
    max-width: 215px;
    text-align: center;
    padding-bottom: 20px;
}
.file-load__area{
    display: flex;
    flex-direction: column;
    box-sizing: border-box;
    margin-bottom: 28px;
    border: 1px dashed gray;
    border-radius:  6px;
}
</style>
