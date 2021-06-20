<template>
  <div>
    <section>
      <div class="col-hf">
        <title-big style="margin-top: 100px">
          Создание нового объявления
        </title-big>
        <div class="form" style="margin-top: 50px">
          <default-input @input="setAddress($event)" style="width: 520px; margin-bottom: 12px" placeholder="Адрес склада" />
          <default-input @input="setMetroStation($event)" style="width: 520px; margin-bottom: 12px" placeholder="Метро (пока не работает как надо)" />
          <type-storage-filter @set="setStorageType($event)" style="margin-bottom: 12px" />
          <default-input @input="setSquare($event)" style="width: 300px; margin-bottom: 12px" placeholder="Размер склада кв.м" />
          <type-save @set="setWarehouseType($event)" style="margin-bottom: 12px" />
          <default-area  @input="setDescription($event)" style="width: 520px; margin-bottom: 12px" placeholder="Описание" />
          <default-input @input="setPrice($event)" style="width: 300px; margin-bottom: 50px" placeholder="Цена" />
          <title-small style="margin-bottom: 20px">
            Выберите дополнительные услуги
          </title-small>
          <div class="uslugi">
            <div class="column-ch">
              <checkbox style="margin-bottom: 12px; width: 200px; width: 200px" @CheckboxChange="CheckboxChange"
                name = "access_24h"
                title = "Доступ 24/7"
              />
              <checkbox style=" margin-bottom: 12px; width: 200px" @CheckboxChange="CheckboxChange"
                name = "video_surveillance"
                title = "Видеонаблюдение"
              />
              <checkbox style="margin-bottom: 50px; width: 200px" @CheckboxChange="CheckboxChange"
                name = "inventoty"
                title = "Инвентарь для погрузки-разгрузки"
              />
            </div>
            <div class="column-ch">
              <checkbox style="margin-bottom: 12px; width: 200px" @CheckboxChange="CheckboxChange"
                name = "shipping"
                title = "Доставка, упаковка вещей"
              />
              <checkbox style=" margin-bottom: 12px; width: 200px" @CheckboxChange="CheckboxChange"
                name = "any_rental_period"
                title = "Любой срок аренды"
              />
              <checkbox style="margin-bottom: 50px; width: 200px" @CheckboxChange="CheckboxChange"
                name = "mobile_app"
                title = "Управление через мобильное приложение"
              />
            </div>
            <div class="column-ch">
              <checkbox style="margin-bottom: 12px; width: 200px" @CheckboxChange="CheckboxChange"
                name = "clever_lock"
                title = "Умный замок"
              />
              <checkbox style=" margin-bottom: 12px; width: 200px" @CheckboxChange="CheckboxChange"
                name = "straight_way"
                title = "Прямой подъезд к складу"
              />
              <checkbox style="margin-bottom: 50px; width: 200px" @CheckboxChange="CheckboxChange"
                name = "ventilation"
                title = "Вентиляция"
              />
            </div>
            <div class="column-ch">
              <checkbox style="margin-bottom: 12px; width: 200px" @CheckboxChange="CheckboxChange"
                name = "online_contract"
                title = "Онлайн договор"
              />
              <checkbox style=" margin-bottom: 12px; width: 200px" @CheckboxChange="CheckboxChange"
                name = "inshurance"
                title = "Страховка имущества"
              />
              <checkbox style="margin-bottom: 50px; width: 200px" @CheckboxChange="CheckboxChange"
                name = "cleaning"
                title = "Регулярная уборка"
              />
            </div>
          </div>
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
import TypeSave from '@/components/shared/TypeSave'
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
    TypeStorageFilter,
    TypeSave
  },
  data () {
    return{
      storageinfo: {

      },
      selVal3: null,
      isFileWasUploaded: false,
      checkboxControler: {}
    }
  },
  methods: {
    setAddress (event) {
      this.storageinfo.address = event
    },
    setMetroStation (event) {
      this.storageinfo.metro_station = event
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
    setStorageType(event){
      this.storageinfo.storage_type = event
    },
    setWarehouseType(event){
      this.storageinfo.WarehouseType = event
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
    CheckboxChange(value) {
      console.log(value)
      this.checkboxControler[value.name] = value.value
      this.storageinfo.addUslugi = this.checkboxControler
      console.log(this.checkboxControler)
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

.uslugi{
  display: flex;
  flex-direction: row;
}

.column-ch{
  display: flex;
  flex-direction: column;
  margin-right: 50px;
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
