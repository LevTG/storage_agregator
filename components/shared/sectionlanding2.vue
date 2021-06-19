<template>
  <section class="wow">
    <div class="container">
       <div class="container-in">
           <img src="@/assets/picture/image7.svg" class="pic">
            <div class="container-in_text">
              <p class="container-in_zag">Облачное хранилище</p>
              <p class="container-in_roseText">{{subtitle}}</p>
              <p class="container-in_bigtext">
                Тип хранения для b2b сегмента. Склады различных размеров в
                черте города, разного наполнения и внутренним условиям содержания.
                <br>
                <br>
                Как правило подходит для долгосрочных
                контрактов в индустрии продуктового и продовольственного ритейла.
              </p>
          </div>
       </div>
    </div>
    <div class="container" :class="backPro">
       <div class="container-in" :class="reverPro" >
           <img src="@/assets/picture/image8.svg" class="pic">
            <div class="container-in_text">
              <p class="container-in_zag">Индивидуальное хранение</p>
              <p class="container-in_roseText">
                {{subtitle}}
              </p>
              <p class="container-in_bigtext">
                Тип хранения при котором склад представляет собой небольшое помещение,
                специально выделенное в ЖК. Клиент получает доступ к ней 24/7.
                <br>
                <br>
                 Как правило подходит для хранения вещей по типу:
                 велосипед, книги, лодка, шины автомобиля.
              </p>
          </div>
       </div>
    </div>
       <div class="container">
       <div class="container-in">
           <img src="@/assets/picture/image6.svg" class="pic">
            <div class="container-in_text">
              <p class="container-in_zag">Ответсвенное хранение</p>
              <p class="container-in_roseText">
                {{subtitle}}
              </p>
              <p class="container-in_bigtext">
                Тип хранения вещей, при котором специально обученные муверы приезжают
                к вам, упаковывают ваши вещи, после чего отвозят их на безопасный склад.
                <br>
                <br>
                В данном типе хранения предусмотрено создание виртуального каталога с фотографиями
                каждой вещи.Вы можете выбрать любую необходимую вам и ее доставят на следующий день.
              </p>
          </div>
       </div>
    </div>
    <div class="container" :class="backPro">
       <div class="container-in" :class="reverPro">
           <img src="@/assets/picture/image9.svg" class="pic" >
            <div class="container-in_text">
              <p class="container-in_zag">Частные кладовки</p>
              <p class="container-in_roseText">
                {{subtitle}}
              </p>
              <p class="container-in_bigtext">
                Тип хранения вещей, при котором каждому клиенту предоставляется безопасный бокс с умным замком
                и необходимых размеров.
                <br>
                <br>
                 Как правило, такие боксы распространяются внутри небольших складских помещений, кторые находятся в черте города.
                 Преимуществом данного типа является доступ для клиента 24/7.
              </p>
          </div>
       </div>
    </div>
  </section>
</template>

<script>
import InlineSvg from 'vue-inline-svg';

// Your component
export default {
    components: {
        InlineSvg,

    },
    data(){
      return{
         reverPro:{
            rever:true,
         },
         backPro:{
            back:true
         },
         subtitle:'3765 складов',
      }
    },
}
</script>

<style scoped>
.wow{
  display: flex;
  flex-direction: column;
}

.container{
     width: 100%;
     height: 414px;
     background: #F8F9FB;
     display: flex;
     align-items: center;
     justify-content: center;
}
.container-in{
     width: 1200px;
     display:flex;
     flex-direction: row;
     align-items: center;
     justify-content: space-between;
}
.container-in_zag{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  color: #000000;
  font-size: 18px;
}
.container-in_roseText{
  color: #FB4A71;
  font-size: 18px;
  margin-bottom: 40px;
}
.container-in_text{
     display: flex;
     flex-direction: column;
     justify-content: space-between;
     height: 280px;
}
.container-in_bigtext{
  width: 535px;
  color: #000000;
  font-size: 18px;
}
.back{
  background-color: white;
}
.rever{
  flex-direction: row-reverse;
}
.pic{
  background-color: slategrey;
}
</style>
