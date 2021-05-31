<template>
  <div>
    <section>
      <div class="col-hf">
        <div class="content-container">
          <div class="center-el">
            <title-big style="margin-bottom: 25px">
              Подайте заявку, чтобы стать
              <span style="color:#24287D">партнером</span>
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
            Зачем становится партнером
          </title-medium>
        </div>
        <div class="row">
          <how-it-work
            title='Дополнительные клиенты'
            img='crm1.svg'>
              С помощью нашего сервиса Вы привлечете дополнительный поток клиентов, при этом не потратив денег на рекламу
          </how-it-work>
          <how-it-work
            title='Дополнительный доход'
            img='crm2.svg'>
              Получайте больший дооход от вновь привлеченных клиентов
          </how-it-work>
          <how-it-work
            title='Дополнительный информационный канал'
            img='crm3.svg'>
              Увеличивайте свою узнаваемость с помощью Сервиса
          </how-it-work>
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
            <default-Button style="width: 160px"> Подать заявку</default-button>
          </div>
        </div>
      </div>
      <div class="col-hf-r">
        <img src="@/assets/icons/img/secondframe.svg" alt="альтернативный текст" style="transform: scale(2); margin-left: auto">
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
export default {
  components: {
    TitleMedium,
    TitleSmall,
    TitleBig,
    DefaultButton,
    HowItWork
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

a{
  text-decoration: none;
  color: white;
}


</style>
