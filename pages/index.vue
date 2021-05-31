<template>
  <div class="container">
    <h1> Тут лендинг </h1>
    <VuePicker class="demo__picker" style="width: 300px" v-model="selVal3" placeholder="Выберите размер">
            <VuePickerOption value="val-0">Любой</VuePickerOption>
            <VuePickerOption value="val-1">XL</VuePickerOption>
            <VuePickerOption value="val-1">XXL</VuePickerOption>
            <VuePickerOption value="val-1">XXXL</VuePickerOption>
            <VuePickerOption value="val-2">XXXXL</VuePickerOption>
            <VuePickerOption value="val-3">LLLL</VuePickerOption>
    </VuePicker>
    <SearchResultItem :info="info" @showPopup="showModal"/>
    <DropDownFilter />
    <modal
      :show='showPopup'
      header-text='Введите контактные данные, чтобы владелец склада мог связаться с Вами'
      :on-close='onRowClose'
    >
      <template #body>
        <default-input style="width: 300px; margin-bottom: 12px" placeholder="Имя" />
        <default-input style="width: 300px; margin-bottom: 12px" placeholder="Почта" />
        <default-input style="width: 300px; margin-bottom: 12px" placeholder="Телефон" />
        <default-area style="width: 300px; margin-bottom: 12px" placeholder="Сообщение" />
        <default-button>Забронировать</default-button>
      </template>
    </modal>
    <HotelDatePicker
      format="DD/MM/YYYY"
      :i18n="ptBr">
    </HotelDatePicker>
  </div>
</template>

<script>
import SearchResultItem from '@/components/storages/SearchResultItem'
import DropDownFilter from '@/components/shared/DropDownFilter'
import Modal from '@/components/shared/Modal'
import DefaultInput from '@/components/shared/DefaultInput'
import HotelDatePicker from 'vue-hotel-datepicker'
import DefaultButton from '@/components/shared/DefaultButton'
import DefaultArea from '@/components/shared/DefaultArea'
import { VuePicker, VuePickerOption } from '@/components/shared/picker/'
import 'vue-hotel-datepicker/dist/vueHotelDatepicker.css';


export default {
  components: {
    SearchResultItem,
    DropDownFilter,
    Modal,
    HotelDatePicker,
    DefaultInput,
    DefaultButton,
    DefaultArea,
    VuePicker,
    VuePickerOption
  },
  data() {
    return {
      info: {
        address: 'Улица Пупкина',
        type: 'Теплый склад',
        price: 500,
        available: 32
      },
      selVal3: null,
      showPopup: false,
      ptBr: {
        'day-names': ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
        'month-names': ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
      }
    }
  },
  methods: {
    onRowClose () {
      this.showPopup = false
    },
    showModal (value) {
      this.showPopup = value
    }
  }
}
</script>
<style>

</style>
