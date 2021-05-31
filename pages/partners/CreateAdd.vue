<template>
  <div>
    <section>
      <div class="col-hf">
        <title-big style="margin-top: 100px">
          Создание нового объявления
        </title-big>
        <div class="form" style="margin-top: 50px">
          <default-input style="width: 520px; margin-bottom: 12px" placeholder="Адрес склада" />
          <VuePicker class="demo__picker" style="width: 300px; margin-bottom: 12px" v-model="selVal3" placeholder="Тип склада">
                  <VuePickerOption value="val-0">Любой</VuePickerOption>
          </VuePicker>
          <default-input style="width: 300px; margin-bottom: 12px" placeholder="Размер склада" />
          <VuePicker class="demo__picker" style="width: 300px; margin-bottom: 12px" v-model="selVal3" placeholder="Тип владельца">
                  <VuePickerOption value="val-0">Любой</VuePickerOption>
          </VuePicker>
          <default-input style="width: 520px; margin-bottom: 12px" placeholder="Наименование владельца" />
          <default-input style="width: 300px; margin-bottom: 50px" placeholder="Цена" />
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
          <default-button style="width: 220px">Опубликовать</default-button>
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
import AddingFile from '@/components/shared/AddingFile'
export default {
  components: {
    TitleMedium,
    TitleSmall,
    TitleBig,
    DefaultButton,
    HowItWork,
    DefaultInput,
    VuePicker,
    VuePickerOption,
    Checkbox,
    AddingFile
  },
  data () {
    return{
      selVal3: null,
      isFileWasUploaded: false
    }
  },
  methods: {
    CheckboxChange(){

    },
    isFileWasUploadedStatusChanged (value) {
      this.isFileWasUploaded = false
    },
    loadFileAggregation (value) {
      this.file = value
      // this.submitFiles()
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
