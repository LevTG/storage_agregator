<template>
  <div class="icotitle">
    <inline-svg
      class="core-checkbox__indicator__icon"
      :src="require('@/assets/icons/trash.svg')"
    />
    <span class="">{{title}}</span>
  </div>
</template>

<script>
import InlineSvg from 'vue-inline-svg'
export default {
  name: 'IcoTitle',
  components: {
    InlineSvg
  },
  props: {
    img: {
      type: String,
      default: ''
    },
    title: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang="css" scoped>
.core-button {
  font-family: inherit;
  color: #121212;
  background-color: gray;
  padding: 0;
  margin: 0;
  border: none;
  outline: none;
  cursor: pointer;
}
</style>
