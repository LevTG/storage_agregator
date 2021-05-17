<template>
  <div class="container">
    <h1> тут склад </h1>
    <SearchResultItem :info="info"/>
    <ico-title
      title="Телефон"
    />
  </div>
</template>

<script>
import SearchResultItem from '@/components/storages/SearchResultItem'
import IcoTitle from '@/components/shared/IcoTitle'
export default {
  components: {
    SearchResultItem,
    IcoTitle
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
<style>

</style>
