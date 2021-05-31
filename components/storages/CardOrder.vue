<template>
  <div class="ordercard">
    <div class="row" style="margin-bottom: 25px">
      <div class="left-col">
        <TitleSmall style="margin-bottom: 12px">
          Адрес
        </TitleSmall>
        <tag style="width: calc(100% - 48px)">
          Улица Ленина д. 25
        </tag>
      </div>
      <div class="rigth-col">
        <TitleSmall>
          Период хранения
        </TitleSmall>
      </div>
    </div>
    <div class="row-down">
      <TitleSmall style="margin-bottom: 12px">
        Размер
      </TitleSmall>
      <VuePicker class="demo__picker" style="width: 100%; margin-bottom: 12px" v-model="selVal3" placeholder="Выберите размер">
              <VuePickerOption value="val-0">Любой</VuePickerOption>
              <VuePickerOption value="val-1">XL</VuePickerOption>
              <VuePickerOption value="val-1">XXL</VuePickerOption>
              <VuePickerOption value="val-1">XXXL</VuePickerOption>
              <VuePickerOption value="val-2">XXXXL</VuePickerOption>
              <VuePickerOption value="val-3">LLLL</VuePickerOption>
      </VuePicker>
      <default-button @click="showPopup()" style="margin-bottom: 50px">Забронировать</default-button>
      <div class="total">
        <span class="total-price-left"> 400р х 10 дней </span> <span class="total-price"> 4000 р.</span>
      </div>
    </div>
    <div class="footer">
      <span class="footer-left"> Итого </span> <span class="footer-total-price"> 4000 р.</span>
    </div>
  </div>
</template>
<script>

  import DefaultButton from '@/components/shared/DefaultButton'
  import Tag from '@/components/shared/Tag'
  import TitleSmall from '@/components/shared/TitleSmall'
  import { VuePicker, VuePickerOption } from '@/components/shared/picker/'
  export default{
    components: {
      DefaultButton,
      TitleSmall,
      VuePicker,
      VuePickerOption,
      Tag
    },
    props: {
      info: {
        type: Object,
        default: null
      },
      selVal3: null
    },
    methods: {
      showPopup(){
        this.$emit('showPopup', true)
      }
    }
  }
</script>

<style scoped>
.ordercard{
  display: flex;
  flex-direction: column;
  background: #E7E7E7;
  padding: 24px;
  height: fit-content;
  border-radius: 8px;
  margin-left: 25px;
  width: calc(100% - 25px);
}
.row{
  display: flex;
  flex-direction: row;
}
.row-down{
  display: flex;
  flex-direction: column;
}
.left-col{
  width: 50%;
}
.rigth-col{
  width: 50%;
}
.footer{
  display: flex;
  flex-direction: row;
  border-top: 1px solid #000;
  padding-top: 25px;
  font-family: Roboto;
  font-style: normal;
  font-weight: 500;
  font-size: 18px;
  line-height: 140.62%;
  /* or 25px */


  color: #000000;
}

.footer-left{

}

.footer-total-price{
  margin-left: auto;
}

.total{
  display: flex;
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  line-height: 25px;
  color: #000000;
  margin-bottom: 24px;

}
.total-price-left{

}

.total-price{
  margin-left: auto;
}
</style>
