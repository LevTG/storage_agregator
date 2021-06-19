<template>
  <div>
    <section class="sec-row">
      <title-big style="margin-bottom: 25px">
      Быстрый поиск помещений для
        <span style="color:#FB4A71">хранения вещей</span>
      </title-big>
      <div class="text">
        Мгновенное бронируйте и храниет вещи в любой точке города
      </div>
    </section>
    <section>
      <div class="col-hf">
        <div class="content-container">
          <div class="center-el">
            <title-big style="margin-bottom: 25px">
            Быстрый поиск помещений для
              <span style="color:#FB4A71">хранения вещей</span>
            </title-big>
            <title-small style="font-weight: 400; margin-bottom: 50px">
              Мы поможем Вашему бизнесу заработать больше, не тратя денег на рекламу
            </title-small>
              <nuxt-link no-prefetch class="nav-link" to="/partners/reg">
                <default-Button red style="width: 160px">
                  Подать заявку
                </default-button>
              </nuxt-link>
          </div>
        </div>
      </div>
      <div class="col-hf-r">
        <img src="@/assets/icons/img/firstframe.png" alt="альтернативный текст">
      </div>
    </section>
    <section>
      <div class="column">
        <div class="row" style="margin-bottom: 50px">
          <title-medium>
            Как это работает
          </title-medium>
        </div>
        <div class="row">
          <how-it-work-var
            title='Поиск пунктов хранения'
            img='pwr1.svg'>
              Введите наиболее удобный для Вас адрес
            </how-it-work-var>
          <how-it-work-var
            title='Онлайн бронирование'
            img='pwr2.svg'>
              Нажмите кнопку “Забронировать” у понравившегося Вам склада
          </how-it-work-var>
          <how-it-work-var
            title='Уточнение деталей'
            img='pwr3.svg'>
              Свяжитесь с менеджером склада для решения Ваших вопросов
          </how-it-work-var>
        </div>
      </div>
    </section>

    <section class="bg" style="margin-top: 200px">
      <div class="col-hf-c" style="color: #fff">
        <title-medium>
          О нас
        </title-medium>
        <div class="text" style="color: #fff">
          “Сервис” помогает искать не только удобное расположение склада, но и предоставляет возможность отслеживать оставленные на хранение вещи
        </div>
        <img src="@/assets/icons/img/wq.png" alt="альтернативный текст">
      </div>
      <div class="col-hf-c" style="color: #fff">
        <div class="place-to-tab">
          <div class="tab" @click="showInfoForClient()" :class="{'active-tab': isShowInfoClient}">
            Клиентам
          </div>
          <div class="tab" @click="showInfoForPartner()" :class="{'active-tab': isShowInfoPartner}">
            Партнерам
          </div>
        </div>
        <div class="tab-info" v-if="isShowInfoClient">
          — Близкое расположение <br>
          <br>
          Мы сотрудничаем с пунктами хранения по всей стране
          <br>
          <br>
          — Помощь с определением необходимого размера ячейки
          <br>
          <br>
          Если Вы не знаете, сколько места займут Ваши вещи, то пришлите фото в Службу поддержки. Наши специалисты подскажут Вам, какого размера помещение выбрать.
          <br>
          <br>
          — Наблюдение за вещами
          <br>
          <br>
          Вы можете воспользоваться нашей услугой и запросить фотографию оставленных вещей в Личном кабинете, чтобы убедиться в их сохранности.
          <br>
          <br>
          <br>
          <br>
          <default-button red> Найти </default-button>
        </div>
        <div class="tab-info" v-if="isShowInfoPartner">
          qw
        </div>
      </div>
    </section>
    <section style="background: #F8F9FB; max-height: 300px; margin-top: 200px; margin-bottom: 200px">
      <div class="col-hf">
        <div class="content-container">
          <div class="center-el">
            <title-medium style="margin-bottom: 25px">
              Больше клиентов — больше прибыли
            </title-medium>
            <title-small style="font-weight: 400; margin-bottom: 50px">
              Откройте для своего бизнеса новый канал привлечения аудитории
            </title-small>
            <nuxt-link no-prefetch class="nav-link" to="/partners/reg">
              <default-Button style="width: 160px">
                Подать заявку
              </default-button>
            </nuxt-link>
          </div>
        </div>
      </div>
      <div class="col-hf-r">
        <img src="@/assets/icons/img/secondframe.svg" alt="альтернативный текст" style="transform: scale(2); margin-left: auto">
      </div>
    </section>
    <sectionlanding2 />
  </div>
</template>

<script>
import TitleSmall from '@/components/shared/TitleSmall'
import TitleMedium from '@/components/shared/TitleMedium'
import TitleBig from '@/components/shared/TitleBig'
import DefaultButton from '@/components/shared/DefaultButton'
import HowItWorkVar from '@/components/partners/HowItWorkVar'
import sectionlanding2 from '@/components/shared/sectionlanding2'
export default {
  components: {
    TitleMedium,
    TitleSmall,
    TitleBig,
    DefaultButton,
    HowItWorkVar,
    sectionlanding2
  },
  data () {
    return {
      isShowInfoClient: true,
      isShowInfoPartner: false
    }
  },
  methods: {
    showInfoForClient(){
      this.isShowInfoClient = true
      this.isShowInfoPartner = false
    },
    showInfoForPartner(){
      this.isShowInfoClient = false
      this.isShowInfoPartner = true
    }
  }
}
</script>

<style lang="css" scoped>

section{
  display: flex;
  flex-direction: row;
  padding-left: 10%;
  padding-right: 10%;
}
.sec-row{
  padding-top: 150px;
  display: flex;
  flex-direction: column;
}

.bg{
  background: #24287D;
  padding-bottom: 40px;
}

.tab-info{
  margin-top: 30px;
}

.active-tab{
  border-bottom: 1px solid #FB4A71;
  margin-bottom: -1px;
}

.place-to-tab{
  display: flex;
  flex-direction: row;
  margin-top: 40px;
}

.tab{
  display: flex;
  margin-right: 70px;
  cursor: pointer;
}


.text{
  display: flex;
  font-family: Roboto;
  font-style: normal;
  font-weight: normal;
  font-size: 18px;
  line-height: 140.62%;
  color: #000000;
  justify-content: center;
  margin-bottom: 40px;
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
.col-hf-c{
  display: flex;
  width: calc(50% - 30px);
  flex-direction: column;
  margin-right: 30px;
  padding-top: 32px;
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

a{
  text-decoration: none;
  color: white;
}


</style>
