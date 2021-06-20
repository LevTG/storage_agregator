<template>
  <div>
    <div class="account" v-if="companyIsReadyData">
        <img  class="logo":src="'http://storage.pythonanywhere.com' + company.logo.image" alt="logo" width="400">
        <div class="company-info-top-line">
          <title-medium> {{company.name}} </title-medium>
          <div class="city"> {{company.city}} </div>
        </div>
    </div>
    <div class="">
      <div class="NullAdd" v-if="isAddIsNull">
        <section style="flex-direction: row">
          <div class="col-hf">
            <div class="content-container">
              <div class="center-el">
                <title-big style="margin-bottom: 25px">
                  У вас еще нет
                  <span style="color:#24287D">объявлений</span>
                </title-big>
                <title-small style="font-weight: 400; margin-bottom: 50px">
                  Создайте свое первое объявление прямо сейчас и начните получать больше клиентов
                </title-small>
                  <nuxt-link no-prefetch class="nav-link" to="/partners/createadd">
                    <default-Button red style="width: 230px">
                      + Создать объявление
                    </default-button>
                  </nuxt-link>
              </div>
            </div>
          </div>
          <div class="col-hf-r">
            <img src="@/assets/icons/img/secondframe.svg" alt="альтернативный текст">
          </div>
        </section>
      </div>
      <div v-if="!isAddIsNull">
        <div class="tab">
          <div class="col-hf" >
            <div class="left-tab" @click="showMyAd()" :class="{'active-tab': isShowMyAd}">
              Мои объявления
            </div>
          </div>
          <div class="col-hf" >
            <div class="rigth-tab" @click="showMyFeedback()" :class="{'active-tab': isShowMyFeedback}">
              Отклики
            </div>
          </div>
        </div>
        <section v-if="isShowMyAd">
          <div class="row">
            <nuxt-link no-prefetch class="nav-link" to="/partners/createadd">
              <default-Button style="width: 230px; margin-bottom: 28px">
                + Создать объявление
              </default-button>
            </nuxt-link>
          </div>
          <div class="row">
            <div v-for="item in myAdd" :key="item.id">
              <card-edit  style="margin-bottom: 28px" :info="item"/>
            </div>

          </div>
        </section>
        <section v-if="isShowMyFeedback">
          <div class="col-hf">
            Отклики
          </div>
          <div class="col-hf">
          </div>
        </section>
      </div>
    </div>
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
import CardEdit from '@/components/storages/CardEdit'
import DefaultInput from '@/components/shared/DefaultInput'
import Api from '@/api'

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
    CardEdit
  },
  data() {
    return {
      info: {
        address: 'Улица Пупкина',
        type: 'Теплый склад',
        price: 500,
        available: 32
      },
      isShowMyAd: true,
      isShowMyFeedback: false,
      isAddIsNull: true,
      myAdd: [],
      company_id: null,
      company: {

      },
      companyIsReadyData: false
    }
  },
  mounted () {
    console.log('Авторизирован ли юзер?')
    console.log(localStorage.access)
    console.log(localStorage.refresh)
    let self = this
    if(localStorage.access != null){
      this.isAuth = true
      const api = new Api
      api.getUser().then(
        response => {
          self.company_id = response.data.companies[0].id
          api.getAllStorages().then( response => {
              if(response.length > 0){
                console.log('Данные пользователя')
                self.myAdd = response
                self.isAddIsNull = false
              }
            }
          )
          if(response.data.myadd != null){
            self.isAddIsNull = true
          }
          self.username = response.data.first_name + ' ' + response.data.last_name
          console.log(response)
        }
      ).then( () => {
        api.getCompany(self.company_id).then( response =>
        {
          console.log('Data company')
          console.log(response)
          self.companyIsReadyData = true
          self.company = response.data
          console.log(self.company)
          //self.company.logo.image = "http://storage.pythonanywhere.com" + self.company.logo.image
          //api.getImg(self.company.logo.image)
        })
      })

    }else{
      this.isAuth = false
    }
    console.log(this.isAuth)
  },
  methods: {
    showMyAd() {
      this.isShowMyAd = true
      this.isShowMyFeedback = false
    },
    showMyFeedback() {
      this.isShowMyFeedback = true
      this.isShowMyAd = false
    }
  }
}
</script>

<style scoped>

section{
  display: flex;
  flex-direction: column;
  padding-left: 10%;
  padding-right: 10%;
}

.account{
  display: flex;
  flex-direction: column;
  background: #F8F9FB;
  padding-left: 10%;
  padding-right: 10%;
  padding-top: 45px;
  padding-bottom: 45px;
  justify-content: center;
  align-items: center;
}

.city{
  color: gray;
}

.company-info-top-line{
  margin-top: 25px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}


.logo{
  height: 200px;
  width: 200px;
  object-fit: cover;
  border-radius: 8px;
}

.left-tab{
  display: flex;
  margin-left: auto;
}

.rigth-tab{
  display: flex;
  margin-right: auto;
}

.active-tab{
  border-bottom: 1px solid #FB4A71;
  margin-bottom: -1px;
}

.rigth-tab:hover{
  border-bottom: 1px solid #FB4A71;
  cursor: pointer;
  margin-bottom: -1px;

}

.left-tab:hover{
  border-bottom: 1px solid #FB4A71;
  cursor: pointer;
  margin-bottom: -1px;

}

.tab{
  display: flex;
  padding-left: 10%;
  padding-right: 10%;
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  line-height: 140.62%;
  /* identical to box height, or 25px */


  /* Обычный текст */

  color: #000000;
  margin-bottom: 70px;
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
  padding: 30px;
  width: calc(50% - 30px);
}
.col-hf-r{
  display: flex;
  width: calc(50% - 30px);
}

.row{
  display: flex;
  flex-direction: column;
}

.column{
  display: flex;
  flex-direction: column;
}

a{
  text-decoration: none;
  color: white;
}



</style>
