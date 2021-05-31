<template>
  <footer>
    <div class="left-block">
      <div class="place_to_logo">
        <title-medium style="color: #fff"> StÖrage </title-medium>
      </div>
      <div class="place-to-link">
        <div class="col">
          <ul>
            <li>
              <nuxt-link exact active-class="active" class="nav-link" to="/">
                Как это работает
              </nuxt-link>
            </li>
            <li>
              <nuxt-link no-prefetch active-class="active" class="nav-link" to="/partners">
                О нас
              </nuxt-link>
            </li>
            <li>
              <nuxt-link no-prefetch active-class="active" class="nav-link" to="/partners">
                Часто задаваемые вопросы
              </nuxt-link>
            </li>
          </ul>
        </div>
        <div class="col" style="padding-left: 100px; width: calc(100% - 100px)">
          <ul>
            <li>
              <nuxt-link exact active-class="active" class="nav-link" to="/">
                Контакты
              </nuxt-link>
            </li>
            <li>
              <nuxt-link no-prefetch active-class="active" class="nav-link" to="/partners">
                Телефон
              </nuxt-link>
            </li>
            <li>
              <nuxt-link no-prefetch active-class="active" class="nav-link" to="/partners">
                Юридический адрес
              </nuxt-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div class="right-block">
      <div class="place_to_logo">
        <title-medium style="color: #fff"> Остались вопросы? Напишите нам </title-medium>
      </div>
      <div class="form">
        <default-input white style="width: 300px; margin-bottom: 12px" placeholder="Почта" />
        <default-input white style="width: 300px; margin-bottom: 12px" placeholder="Телефон" />
        <default-area  white style="width: 300px; margin-bottom: 12px" placeholder="Сообщение" />
        <default-button red style="width: 200px;">Отправить</default-button>
      </div>

    </div>
  </footer>
</template>

<script>
  import DefaultInput from '@/components/shared/DefaultInput'
  import DefaultButton from '@/components/shared/DefaultButton'
  import DefaultArea from '@/components/shared/DefaultArea'
  import TitleSmall from '@/components/shared/TitleSmall'
  import TitleMedium from '@/components/shared/TitleMedium'
  export default{
    components: {
      DefaultButton,
      TitleSmall,
      DefaultArea,
      DefaultInput,
      TitleMedium
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
footer{
  display: flex;
  flex-direction: row;
  height: 648px;
  background: #30339B;
  padding-left: 10%;
  padding-right: 10%;
}
.form{
  display: flex;
  flex-direction: column;
}
.place-to-link{
  display: flex;
}
.left-block{
  width: 50%;
  display: flex;
  flex-direction: column;
}
.place_to_logo{
    display: flex;
    height: 100px;
    width: 100%;
    align-items: center;
}
ul{
  display: flex;
  flex-direction: column;
  list-style-type: disc;
  margin-block-start: 0em !important;
  margin-block-end: 0em !important;
  margin-inline-start: 0 !important;
  margin-inline-end: 0 !important;
  padding-inline-start: 1 !important;
  padding: 0px;
}
li{
  display: flex;
  margin-bottom: 20px;
}
li a{
  color: #fff;
  text-decoration: none;
}
.active{
  color: #fff;
}
</style>
