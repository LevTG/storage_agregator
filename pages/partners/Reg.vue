<template>
  <div>
    <section>
      <title-big style="margin-top: 100px">
        Заполните форму для регистрации
      </title-big>
      <div class="form" style="margin-top: 50px">
        <div class="row">
          <default-input @input="setFirstName($event)" style="width: 250px; margin-bottom: 12px" placeholder="Имя" />
          <default-input @input="setLastName($event)" style="width: 250px; margin-bottom: 12px; margin-left: 25px" placeholder="Фамилия" />
        </div>
        <default-input @input="setLogin($event)" style="width: 520px; margin-bottom: 12px" placeholder="Логин" />
        <default-input @input="setMail($event)" style="width: 520px; margin-bottom: 12px" placeholder="Почта" />
        <default-input @input="setPhone($event)" style="width: 520px; margin-bottom: 12px" placeholder="Телефон" />
        <default-input @input="setCompanyName($event)" style="width: 520px; margin-bottom: 12px" placeholder="Компания" />
        <default-input @input="setCompanyUrl($event)" style="width: 520px; margin-bottom: 12px" placeholder="Ссылка на сайт компании" />
        <default-input @input="setCity($event)" style="width: 520px; margin-bottom: 12px" placeholder="Город*" />
        <adding-file id="aggregatoin"
          :isFileWasUploaded="isFileWasUploaded"
          @load-file="loadFileAggregation"
          @isFileWasUploadedStatusChanged="isFileWasUploadedStatusChanged()"></adding-file>
        <default-input @input="setPassword($event)" style="width: 520px; margin-bottom: 12px" placeholder="Пароль*" />
        <default-input @input="setPassword($event)" style="width: 520px; margin-bottom: 50px" placeholder="Подтверждение пароля*" />
        <default-button @click="reg()"style="width: 220px">Зарегистрироваться</default-button>
      </div>
    </section>
  </div>
</template>

<script>
import TitleSmall from '@/components/shared/TitleSmall'
import TitleMedium from '@/components/shared/TitleMedium'
import TitleBig from '@/components/shared/TitleBig'
import DefaultButton from '@/components/shared/DefaultButton'
import HowItWork from '@/components/partners/HowItWork'
import DefaultInput from '@/components/shared/DefaultInput'
import AddingFile from '@/components/shared/AddingFile'
import Api from '@/api/'
import axios from 'axios'
import {URL} from '@/const/url'
export default {
  components: {
    TitleMedium,
    TitleSmall,
    TitleBig,
    DefaultButton,
    HowItWork,
    DefaultInput,
    AddingFile
  },
  data() {
    return {
      reginfo: {
        company: {

        }
      },
      user: {

      },
      isFileWasUploaded: false
    }
  },
  mounted () {
    this.test()
  },
  methods:{
    setMail (event) {
      this.reginfo.mail = event;
    },
    setFirstName (event){
      this.reginfo.firstname = event;
    },
    setLastName (event){
      this.reginfo.lastname = event;
    },
    setCity (event){
      this.reginfo.company.city = event;
    },
    setPhone (event){
      this.reginfo.phone = event;
    },
    setCompanyName (event){
      this.reginfo.company.name= event;
    },
    setLogin (event){
      this.reginfo.login = event;
    },
    setCompanyDescription(event){
      this.reginfo.company.description = event;
    },
    setCompanyUrl (event){
      this.reginfo.companyurl = event;
    },
    setPassword (event){
      this.reginfo.password = event;
    },
    put (){
      console.log(this)
      this.$router.push('/partners/createadd')
    },
    reg() {
      console.log(this.reginfo)
      const api = new Api
      api.registration(this.reginfo)
    },
    isFileWasUploadedStatusChanged (value) {
      this.isFileWasUploaded = false
    },
    loadFileAggregation (value) {
      this.reginfo.logo = value
      // this.submitFiles()
    },
    test () {
      this.reginfo.firstname = 'Den6'
      this.reginfo.lastname = 'Fedorov6'
      this.reginfo.mail = 'fedorovdgap2341@gmail.com',
      this.reginfo.phone = '723418596470',
      this.reginfo.login = 'fedorovdgap2341',
      this.reginfo.password = '12345'
      this.reginfo.company = {
        name: 'FedorovInc2341',
        city: 'Ростов-на-Дону',
        description : 'Мы лучший склад в мире'
      }
      //this.reginfo.company = null
    },
    regPost () {
      const formData = new FormData()
      formData.append('first_name', this.reginfo.firstname)
      formData.append('last_name', this.reginfo.lastname)
      formData.append('email', this.reginfo.mail)
      formData.append('phone_number', this.reginfo.phone)
      formData.append('company_name', this.reginfo.companyname)
      formData.append('city', this.reginfo.city)
      formData.append('username', this.reginfo.login)
      formData.append('password', this.reginfo.password)
      console.log(URL)
      let self  = this
      this.$axios.$post(URL + 'authentication/registration',
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
    async getSuck() {
        this.users = await this.$axios.$get('https://jsonplaceholder.typicode.com/users')
      console.log(this.users)
    }
  }
}
</script>

<style lang="css" scoped>

section{
  display: flex;
  justify-content: center;
  flex-direction: column;
  padding-left: 10%;
  padding-right: 10%;
  align-items: center;
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
