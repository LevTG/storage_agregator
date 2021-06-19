<template>
  <div>
    <section>
      <div class="col-hf">
        <title-big style="margin-top: 100px">
          Создание нового объявления
        </title-big>
        <div class="form" style="margin-top: 50px">
          <default-input @input="setAddress($event)" style="width: 520px; margin-bottom: 12px" placeholder="Адрес склада" />
          <type-storage-filter style="margin-bottom: 12px" />
          <default-input @input="setSquare($event)" style="width: 300px; margin-bottom: 12px" placeholder="Размер склада кв.м" />
          <VuePicker class="demo__picker" style="width: 300px; margin-bottom: 12px" v-model="selVal3" placeholder="Тип владельца">
                  <VuePickerOption value="val-0">Любой</VuePickerOption>
          </VuePicker>
          <default-input style="width: 520px; margin-bottom: 12px" placeholder="Наименование владельца" />
          <default-area  style="width: 300px; margin-bottom: 12px" placeholder="Описание" />
          <default-input @input="setPrice($event)" style="width: 300px; margin-bottom: 50px" placeholder="Цена" />
          <title-small style="margin-bottom: 20px">
            Выберите дополнительные услуги
          </title-small>
          <checkbox style="margin-bottom: 12px" @CheckboxChange="CheckboxChange"
            name = "type"
            title = "Круглосуточно"
          />
          <checkbox style=" margin-bottom: 12px" @CheckboxChange="CheckboxChange"
            name = "type"
            title = "Бесплатный вывоз вещей"
          />
          <checkbox style="margin-bottom: 50px" @CheckboxChange="CheckboxChange"
            name = "type"
            title = "Доступ 24/7"
          />
          <adding-file id="aggregatoin"
            :isFileWasUploaded="isFileWasUploaded"
            @load-file="loadFileAggregation"
            @isFileWasUploadedStatusChanged="isFileWasUploadedStatusChanged()"></adding-file>
          <default-button @click="toPublic()" style="width: 220px">Опубликовать</default-button>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Checkbox from '@/components/shared/Checkbox'
import { VuePicker, VuePickerOption } from '@/components/shared/picker/'
import TitleSmall from '@/components/shared/TitleSmall'
import TitleMedium from '@/components/shared/TitleMedium'
import TitleBig from '@/components/shared/TitleBig'
import DefaultButton from '@/components/shared/DefaultButton'
import HowItWork from '@/components/partners/HowItWork'
import DefaultInput from '@/components/shared/DefaultInput'
import DefaultArea from '@/components/shared/DefaultArea'
import AddingFile from '@/components/shared/AddingFile'
import TypeStorageFilter from '@/components/shared/TypeStorageFilter'
import Api from '@/api'

export default {
  components: {
    TitleMedium,
    TitleSmall,
    TitleBig,
    DefaultButton,
    HowItWork,
    DefaultInput,
    DefaultArea,
    VuePicker,
    VuePickerOption,
    Checkbox,
    AddingFile,
    TypeStorageFilter
  },
  data () {
    return{
      storageinfo: {

      },
      selVal3: null,
      isFileWasUploaded: false
    }
  },
  methods: {
    setAddress (event) {
      this.storageinfo.address = event
    },
    setSquare (event) {
      this.storageinfo.square = event
    },
    setPrice (event) {
      this.storageinfo.price = event
    },
    setDescription (event) {
      this.storageinfo.description = event
    },
    loadFileAggregation (value) {
      this.storageinfo.images = value
      // this.submitFiles()
    },
    toPublic () {
      console.log(this.storageinfo)
      const api = new Api
      api.postStorage(this.storageinfo).then(
        response => {
          console.log('Создать склад')
          //self.username = response.data.first_name + ' ' + response.data.last_name
          console.log(response)
        }
      )
    },
    CheckboxChange(){

    },
    isFileWasUploadedStatusChanged (value) {
      this.isFileWasUploaded = false
    }
  }
}
</script>

<style lang="css" scoped>

section{
  display: flex;
  padding-left: 10%;
  padding-right: 10%;
}

.form{
  display: flex;
  flex-direction: column;
  width: 520px;
  padding-bottom: 125px;
}

.content-container{
  display: flex;
  height: 100%;
  align-items: center;
}

.center-el{
  display: flex;
  flex-direction: column;
}

.col-hf{
  display: flex;
  flex-direction: column;
  width: calc(50% - 30px);
}
.col-hf-r{
  display: flex;
  width: calc(50% - 30px);
}

.row{
  display: flex;
  flex-direction: row;
}

.column{
  display: flex;
  flex-direction: column;
}


</style>
