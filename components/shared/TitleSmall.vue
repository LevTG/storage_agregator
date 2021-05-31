<template>
  <div class="title">
    <slot/>
  </div>
</template>

<script>
export default {
  name: 'TitleSmall'
}
</script>

<style lang="css" scoped>

.title{
  font-family: Roboto;
  font-style: normal;
  font-weight: 500;
  font-size: 18px;
  line-height: 25px;
}
</style>
