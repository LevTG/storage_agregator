<template>
  <div class="container">
    <h1> Тут лендинг </h1>
    <SearchResultItem :info="info" @showPopup="showModal"/>
    <DropDownFilter />
    <modal
      :show='showPopup'
      header-text='Введите контактные данные, чтобы владелец склада мог связаться с Вами'
      :on-close='onRowClose'
    >
      <template #body>
        <default-input style="max-width: 300px; margin-bottom: 12px" placeholder="Имя" />
        <default-input style="max-width: 300px; margin-bottom: 12px" placeholder="Почта" />
        <default-input style="max-width: 300px; margin-bottom: 12px" placeholder="Телефон" />
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
import 'vue-hotel-datepicker/dist/vueHotelDatepicker.css';

export default {
  components: {
    SearchResultItem,
    DropDownFilter,
    Modal,
    HotelDatePicker,
    DefaultInput,
    DefaultButton
  },
  data() {
    return {
      info: {
        address: 'Улица Пупкина',
        type: 'Теплый склад',
        price: 500,
        available: 32
      },
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
