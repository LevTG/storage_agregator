<template>
  <div class="title">
    <slot/>
  </div>
</template>

<script>
export default {
  name: 'TitleMedium'
}
</script>

<style lang="css" scoped>

.title{
  font-family: Roboto;
  font-style: normal;
  font-weight: 500;
  font-size: 28px;
  line-height: 42px;;
}
</style>
