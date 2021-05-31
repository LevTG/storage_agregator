<template>
  <div>
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
      <div class="col-hf">
        <card-edit :info="info"/>
      </div>
      <div class="col-hf">
        <default-button style="width: 260px">+ Добавить объявление</default-button>
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
      isShowMyFeedback: false
    }
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

<style>

section{
  display: flex;
  padding-left: 10%;
  padding-right: 10%;
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
  flex-direction: row;
}

.column{
  display: flex;
  flex-direction: column;
}


</style>
