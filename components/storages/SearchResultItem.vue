<template>
  <div class="search-result-item">
    <div class="search-result-item__place-to-img">
      <div class="place-to-price">
        {{info.price + ' руб/день'}}
      </div>
    </div>
    <div class="search-result-item__place-to-info">
      <div class="search-result-item__place-to-info__top">
        <div class="adress">{{info.address}}</div>
        <div class="type">{{info.type}}</div>
        <div class="available">Доступно: {{info.available}} м2</div>
      </div>
      <div class="search-result-item__place-to-info__bottom">
        <default-button @click="showPopup()">Забронировать</default-button>
      </div>
    </div>
  </div>
</template>
<script>

  import DefaultButton from '@/components/shared/DefaultButton'
  export default{
    components: {
      DefaultButton
    },
    props: {
      info: {
        type: Object,
        default: null
      }
    },
    methods: {
      showPopup(){
        this.$emit('showPopup', true)
      }
    }
  }
</script>

<style scoped>
.search-result-item{
  border-top: 1px solid gray;
  width: 600px;
  display: flex;
  height: 200px;
  flex-direction: row;
  padding: 20px;
}

.search-result-item__place-to-img{
  width: 60%;
  height: 100%;
  border-radius: 8px;
  background-color: gray;
  display: flex;
}

.search-result-item__place-to-info{
  width: 40%;
  height: 100%;
  display: flex;
  flex-direction: column;
  padding-left: 20px;
}

.search-result-item__place-to-info__bottom{
  margin-top: auto;
}

.place-to-price{
  margin-top: auto;
  font-family: Roboto;
  font-style: normal;
  font-weight: 500;
  font-size: 18px;
  padding-left: 12px;
  padding-bottom: 12px;
}

.adress{
  font-family: Roboto;
font-style: normal;
font-weight: normal;
font-size: 29px;
margin-bottom: 12px;
}

.type{
  font-family: Roboto;
font-style: normal;
font-weight: normal;
font-size: 18px;
line-height: 25px;
/* or 25px */
margin-bottom: 12px;


color: #626262;
}
.available{
  font-family: Roboto;
font-style: normal;
font-weight: normal;
font-size: 18px;
line-height: 25px;
/* or 25px */


color: #000;
}

</style>
