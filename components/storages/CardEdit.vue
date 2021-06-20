<template>
  <div class="card">
    <div class="top-line">
      <inline-svg style="margin-left: auto; width: 100%"
        :src="require('@/assets/icons/x.svg')"
      />
    </div>
    <div class="main">
      <div class="img">
        <img  class="logo":src="info.album.images[0].image" alt="logo" width="400">
      </div>
      <div class="rigth-part">
      <div class="middle-line">
        {{info.address}}
      </div>
        <div class="info">
          <div class="line">
            <span>Тип: </span> <span class="rigth-text">{{info.type}} </span>
          </div>
          <div class="line">
            <span>Свободного места: </span> <span class="rigth-text"> {{info.square}} кв. м </span>
          </div>
          <div class="line">
            <span>Владелец: </span> <span class="rigth-text">{{info.type}} </span>
          </div>
          <div class="line">
            <span>Услуги: </span> <span class="rigth-text">{{info.type}} </span>
          </div>
          <div class="line">
            <span>Цена от: </span> <span class="rigth-text">{{info.price}} р </span>
          </div>
        </div>
      </div>
    </div>
    <div class="footer">
      <default-button @click="showPopup()" style="margin-left: auto">Редактировать</default-button>
    </div>
  </div>
</template>
<script>
  import InlineSvg from 'vue-inline-svg'
  import DefaultButton from '@/components/shared/DefaultButton'
  export default{
    components: {
      DefaultButton,
      InlineSvg
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
.card{
  display: flex;
  position: relative;
  flex-direction: column;
  padding: 28px;
  width: 800px;
  padding-bottom: 40px;
  background: #FFFFFF;
  box-shadow: 6px 4px 16px rgba(0, 0, 0, 0.25);
  border-radius: 8px;
}

.main{
  display: flex;
  flex-direction: row;
}

.rigth-part{
  display: flex;
  flex-direction: column;
  margin-left: 25px;
  width: 100%;
}

.middle-line{
  font-family: Roboto;
  font-style: normal;
  font-weight: 500;
  font-size: 29px;
  line-height: 140.62%;
  color: #000000;
  margin-bottom: 25px;
}

.line{
  display: flex;
  flex-direction: row;
  margin-bottom: 25px;
  font-family: Roboto;
font-style: normal;
font-weight: normal;
font-size: 18px;
line-height: 140.62%;
/* or 25px */


/* Текст на светлом фоне */

color: #000000;
}

.logo{
  height: 300px;
  width: 300px;
  object-fit: cover;
  border-radius: 8px;
}


.top-line{
  position: absolute;
  left: 800px;
}

.rigth-text{
  display: flex;
  margin-left: auto;
}

.footer{

}

.img{
  border-radius: 8px;
  background: grey;
  width: 300px;
  height: 300px;
}

.middle-line{
  width: 100%;
  display: flex;
}

</style>
