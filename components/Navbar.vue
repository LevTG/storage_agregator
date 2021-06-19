<template>
  <nav>
    <div class="place_to_logo">
      <title-medium style="color: #000"> StÖrage </title-medium>
    </div>
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
      <li>
        <default-button @click="showModal" v-if="!isAuth"> Войти</default-button>
        <Account @isAuth="logout()" v-if="isAuth"
          :username="username"
        />
      </li>
    </ul>
    <modal
      :show='showPopup'
      header-text='Вход'
      :on-close='onRowClose'
    >
      <template #body>
        <default-input @input="setLogin($event)" style="width: 300px; margin-bottom: 12px" placeholder="Логин" />
        <default-input @input="setPassword($event)" style="width: 300px; margin-bottom: 50px" placeholder="Пароль" />
        <default-button @click="login()" style="height 40px; width: 300px; margin-bottom: 50px">Войти</default-button>
      </template>
    </modal>
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
import TitleMedium from '@/components/shared/TitleMedium'
import Account from '@/components/shared/Account'
import { VuePicker, VuePickerOption } from '@/components/shared/picker/'
import 'vue-hotel-datepicker/dist/vueHotelDatepicker.css';
import axios from 'axios'
import {URL} from '@/const/url'
import Api from '@/api'

export default {
  components: {
    SearchResultItem,
    DropDownFilter,
    Modal,
    HotelDatePicker,
    DefaultInput,
    DefaultButton,
    DefaultArea,
    TitleMedium,
    VuePicker,
    VuePickerOption,
    Account
  },
  data() {
    return {
      showPopup: false,
      enterinfo: {

      },
      isAuth: false,
      username: '',
      router: {

      }
    }
  },
  mounted () {
    console.log('Авторизирован ли юзер?')
    console.log(localStorage.access)
    //localStorage.removeItem('access')
    let self = this
    if(localStorage.access != null){
      console.log(localStorage.access)
      this.isAuth = true
      const api = new Api
      api.getUser().then(
        response => {
          console.log('Вызвать говно')
          self.username = response.data.first_name + ' ' + response.data.last_name
          console.log(response)
        }
      )
    }else{
      this.isAuth = false
    }
    console.log(this.isAuth)
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
    login() {
      let self = this
      const api = new Api
      api.login(this.enterinfo.login , this.enterinfo.password).then(
        response => {
          if(response.access != null){
            self.isAuth = true
            self.onRowClose()
            api.getUser().then(
              response => {
                console.log('Вызвать говно')
                self.username = response.data.first_name + ' ' + response.data.last_name
                console.log(response)
              }
            )
          }
          console.log('Вызвать говно')
          console.log(response)
        }
      )
    },
    logout () {
      this.isAuth = false
    },
    toLk(){
      this.$router.push('/partners/lk')
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

.place_to_logo{
  display: flex;
  width: 100%;
  align-items: center;
}

.toLk{
  display: flex;
  min-width: 150px;
}
nav{
  z-index: 1;
  height: 70px;
  width: 80%;
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
  flex-direction: row;
  list-style-type: disc;
  margin-left: auto;
  margin-block-start: 0em;
  margin-block-end: 0em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  padding-inline-start: 0px;
  align-items: center;
  padding: 0px;
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
