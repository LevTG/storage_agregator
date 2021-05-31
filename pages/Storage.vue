<template>
  <div class="container">
    <div class="top">
      <h1> Улица Пупкина </h1>
    </div>
    <div class="body-col">
      <div class="left-col">
        <title-medium> Информация о владельце </title-medium>
        <div class="info-about-holder">
          <div class="avatar">

          </div>
          <div class="info-about-holder_body">
            <title-small style="margin-bottom: 12px">Имя фамилия </title-small>
            <div class="info-about-holder_body_inform">
              CEO компании "ЧихПухПык"
            </div>
          </div>
        </div>
        <div class="main-info-text">
          Сдаются помещения  от 900м2 до 5000м2 под автосалон, автосервис, склад. Могут обсуждаться другие варианты целевого назначения аренды.
          Прямая аренда от собственника.  БЕЗ КОМИССИИ!
          Характеристики:
          Панорамное остекление
          Вода и водоотведение.
          Пол- бетон, нагрузка зависит от этажа.
          Есть возможность размещения наружной рекламы, а так же предоставляем арендные каникулы.

          Месторасположение уникально, благодаря удобной локации:
          -Автомобильная: удобный съезд с МКАДа и большой объем
          парковочных мест на территории.
          -Общественный транспорт: непосредственная близость к метро
          Аннино (Серпуховско-Тимирязевская линия) и метро
          Лесопраковая (Бутовская линия).
          -Рядом находится городская перехватывающая парковка
          -Въезд на территорию бесплатный
        </div>
        <div class="infograph-info-about-holder">
          <ico-title
            style="margin-bottom: 12px"
            title="Телефон"
          />
          <ico-title
            style="margin-bottom: 12px"
            title="Почта"
          />
          <ico-title
            title="Сайт"
          />
        </div>
        <title-medium> Информация о складе </title-medium>
        <div class="infograph-info-about-storage">
          <div class="left-col">
            <ico-title
              style="margin-bottom: 12px"
              title="Горячий склад"
            />
            <ico-title
              style="margin-bottom: 12px"
              title="Доступ 24/7"
            />
          </div>
          <div class="rigth-col">
            <ico-title
              style="margin-bottom: 12px"
              title="Горячий склад"
            />
            <ico-title
              style="margin-bottom: 12px"
              title="Доступ 24/7"
            />
          </div>
        </div>
      </div>
      <div class="right-col">
        <card-order />
      </div>
    </div>
    <SearchResultItem :info="info"/>
  </div>
</template>

<script>
import SearchResultItem from '@/components/storages/SearchResultItem'
import IcoTitle from '@/components/shared/IcoTitle'
import TitleMedium from '@/components/shared/TitleMedium'
import TitleSmall from '@/components/shared/TitleSmall'
import CardOrder from '@/components/storages/CardOrder'
export default {
  components: {
    SearchResultItem,
    IcoTitle,
    TitleMedium,
    TitleSmall,
    CardOrder
  },
  data() {
    return {
      info: {
        address: 'Улица Пупкина',
        type: 'Теплый склад',
        price: 500
      }
    }
  }
}
</script>
<style lang="css" scoped>
.container{
  padding-left: 10%;
  padding-right: 10%;
}
.body-col{
  display: flex;
  flex-direction: row;
}

.left-col{
  display: flex;
  flex-direction: column;
  width: 50%;
}
.right-col{
  display: flex;
  height: 500px;
  width: 50%;
}
.info-about-holder{
  display: flex;
  width: 100%;
  flex-direction: row;
  margin-top: 50px;
  margin-bottom: 50px;
}
.info-about-holder_body{
  display: flex;
  flex-direction: column;
  padding-left: 24px;
}
.avatar{
  width: 140px;
  height: 140px;
  border-radius: 70px;
  background: grey;
}
.infograph-info-about-holder{
  margin-top: 50px;
  margin-bottom: 50px;
}
.infograph-info-about-storage{
  display: flex;
  margin-top: 50px;
  margin-bottom: 50px;
}
</style>
