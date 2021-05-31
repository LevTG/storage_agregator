<template>
  <nav>
    <ul>
      <li>
        <nuxt-link exact active-class="active" class="nav-link" to="/">
          Домой
        </nuxt-link>
      </li>
      <li>
        <nuxt-link no-prefetch active-class="active" class="nav-link" to="/partners">
          Партнерам
        </nuxt-link>
      </li>
      <li>
        <nuxt-link no-prefetch active-class="active" class="nav-link" to="/storage">
          Склад
        </nuxt-link>
      </li>
      <default-button @click="showModal"> Войти</default-button>
      <modal
        :show='showPopup'
        header-text='Вход'
        :on-close='onRowClose'
      >
        <template #body>
          <default-input @input="setLogin($event)" style="width: 300px; margin-bottom: 12px" placeholder="Логин" />
          <default-input @input="setPassword($event)" style="width: 300px; margin-bottom: 12px" placeholder="Пароль" />
          <default-button @click="LoginGet()" style="width: 300px; margin-bottom: 50px">Войти</default-button>
        </template>
      </modal>
    </ul>
  </nav>
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
import axios from 'axios'
import {URL} from '@/const/url'

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
      showPopup: false,
      enterinfo: {

      }
    }
  },
  methods: {
    onRowClose () {
      this.showPopup = false
    },
    showModal (value) {
      this.showPopup = !this.showPopup
    },
    setLogin(event) {
      this.enterinfo.login = event
    },
    setPassword(event) {
      this.enterinfo.password = event
    },
    LoginGet () {
      const formData = new FormData()
      formData.append('username', this.enterinfo.login)
      formData.append('password', this.enterinfo.password)
      let self  = this
      console.log(URL)
      this.$axios.$post(URL + 'authentication/token',
        formData,
          {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
          }
      ).then( function(json) {
        console.log(json)
        //self.$router.push('/partners/createadd')

      }).catch(function (error) {
            console.error('UPLOAD FAILURE!', error)
      })

    },
    Pop () {
      console.log(this.enterinfo)
    }
  }
}
</script>

<style scoped>
nav{
  height: 50px;
  width: 100%;
  padding-left: 10%;
  padding-right: 10%;
  background: #dfdfdf;
  display: flex;
  position: fixed;
  top: 0px;
}
ul{
  display: flex;
  height: 100%;
  margin-left: auto;
  flex-direction: row;
  list-style-type: disc;
  margin-block-start: 0em;
  margin-block-end: 0em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  padding-inline-start: 0px;
  align-items: center;
}
li{
  display: flex;
  margin-left: 25px;
}
li a{
  color: #777;
  text-decoration: none;
}
.active{
  color: #333;
}
</style>
