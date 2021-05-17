<template>
  <core-button
    class="default-button"
    :class="{ 'default-button_rounded': rounded }"
    v-bind="$attrs"
    v-on="$listeners"
  >
    <slot />
  </core-button>
</template>

<script>
import CoreButton from './CoreButton'

export default {
  name: 'DefaultButton',
  components: {
    CoreButton
  },
  props: {
    rounded: Boolean
  }
}
</script>

<style lang="css" scoped>
.default-button {
  display: inline-flex;
  align-items: center;
  padding: 6px 14px;
  font-size: 13px;
  line-height: 20px;
  letter-spacing: .005em;
  background: #C4C4C4;
  border-radius: 8px;
  font-family: Roboto;
font-style: normal;
font-weight: 500;
font-size: 18px;
line-height: 25px;
/* or 25px */


color: #000000;
}
</style>
