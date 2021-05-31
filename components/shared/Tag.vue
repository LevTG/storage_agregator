<template>
  <div class="tag">
    <slot/>
  </div>
</template>

<script>
export default {
  name: 'Tag',
  props: {
    outlined: Boolean
  }
}
</script>

<style lang="css" scoped>
.tag{
    color: #fff;display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 10px 14px;
    font-size: 13px;
    line-height: 20px;
    letter-spacing: .005em;
    background: #FB4A71;
    border-radius: 8px;
    font-family: Roboto;
    font-style: normal;
    font-weight: 400;
    font-size: 18px;
    line-height: 25px;
    color: #fff;
}
</style>
