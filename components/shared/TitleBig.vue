<template>
  <div class="title">
    <slot/>
  </div>
</template>

<script>
export default {
  name: 'TitleBig'
}
</script>

<style lang="css" scoped>

.title{
  font-family: Roboto;
  font-style: normal;
  font-weight: 500;
  font-size: 46px;
  line-height: 140.62%;
  /* or 65px */


  /* Текст на светлом фоне */

  color: #000000;
}
</style>
