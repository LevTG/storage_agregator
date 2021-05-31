<template>
  <div class='adding-file'>
              <div class="file-drag-drop">
                    <form v-bind:ref="id">
                        <div class='file-load__area drop-files'>
                            <div class="file-listing" v-if=' file != ""'>
                                {{ file.name }}
                            </div>
                            <div class='file-load__area-background' v-else-if="dragAndDropCapable" >
                                <div class='area-background__image-top'>
                                    <inline-svg
                                        class="area-background__icon"
                                        :src="require('@/assets/icons/load-file.svg')"
                                        width="60"
                                        height="60"
                                    />
                                    <span class="area-background__text">Перетащите файл сюда</span>
                                </div>
                                <span class="area__text">или вы можете загузить файл вручную</span>
                            </div>
                            <div class='file-load__area-background' v-else>
                              <span class="area__text">Вы можете загузить файл вручную</span>
                            </div>
                            <div class="input__wrapper file-load__area-button">
                                <input name="file" v-bind:id="id" type="file" ref="file" class="input input__file" v-on:focus='handleFileClear()' v-on:change='handleFileUpload()' multiple>
                                <label v-bind:for="id" class="input__file-button">
                                    <span class="input__file-button-text">{{buttonName}}</span>
                                </label>
                            </div>
                        </div>
                    </form>
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
      file: '',
      errorTypeFile: false,
      event: 'load-file'
    }
  },
  computed: {
    buttonName () {
      return (this.file === '') ? 'Выбрать файл' : 'Изменить файл'
    }
  },
  watch: {
    isFileWasUploaded: function (val) {
      console.log(val)
      if (val === true) {
        this.file = ''
        this.$refs.file.value = ''
        console.log(this.$refs.file.value)
        this.$emit('isFileWasUploadedStatusChanged', false)
      }
    }
  },
  methods: {
    handleFileClear () {
      console.log('yes')
    },
    handleFileUpload () {
      if (/\.(xlsx)$/i.test(this.$refs.file.files[0].name)) {
        console.log('ok')
        this.file = this.$refs.file.files[0]
        this.$emit('load-file', this.file)
      } else {
        console.log('Расширение файла должно быть .xlsx')
        this.errorTypeFile = true
      }
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
  display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 10px 14px;
    font-size: 13px;
    line-height: 20px;
    letter-spacing: .005em;
    background: #30339B;
    border-radius: 8px;
    font-family: Roboto;
    font-style: normal;
    font-weight: 400;
    font-size: 18px;
    line-height: 25px;
    color: #fff;
    cursor: pointer;
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
    padding:69px 51px 34px 51px;
    margin-bottom: 28px;
    border: 1px dashed gray;
    border-radius:  6px;
}
</style>
