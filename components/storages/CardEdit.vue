<template>
  <div class="card">
    <div class="top-line">
      <inline-svg
        :src="require('@/assets/icons/x.svg')"
      />
    </div>
    <div class="main">
      <div class="img">
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
            <span>Свободного места: </span> <span class="rigth-text">{{info.available}} </span>
          </div>
          <div class="line">
            <span>Владелец: </span> <span class="rigth-text">{{info.type}} </span>
          </div>
          <div class="line">
            <span>Услуги: </span> <span class="rigth-text">{{info.type}} </span>
          </div>
          <div class="line">
            <span>Цена: </span> <span class="rigth-text">{{info.price}} </span>
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
  flex-direction: column;
  padding: 28px;
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
}

.middle-line{
  font-family: Roboto;
  font-style: normal;
  font-weight: 500;
  font-size: 29px;
  line-height: 140.62%;
  color: #000000;
  margin-top: 25px;
  margin-bottom: 50px;
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


.top-line{
  position: absolute;
}

.rigth-text{
  display: flex;
  margin-left: auto;
}

.footer{
  display: flex;
}

.img{
  border-radius: 8px;
  background: grey;
  width: 45%;
  min-height: 300px;
}

.middle-line{
  width: 100%;
  display: flex;
  justify-content: center;
}

</style>
