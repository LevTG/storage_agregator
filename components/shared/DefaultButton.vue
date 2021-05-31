<template>
  <core-button
    class="default-button"
    :class="{ 'default-button_rounded': rounded, 'red-style': red }"
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
    rounded: Boolean,
    red: Boolean
  }
}
</script>

<style lang="css" scoped>
.default-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 10px 14px;
  font-size: 13px;
  line-height: 20px;
  letter-spacing: .005em;
  background: #30339B;
  border-radius: 8px;
  font-family: Roboto;
font-style: normal;
font-weight: 400;
font-size: 18px;
line-height: 25px;
/* or 25px */


color: #fff;
}

.red-style{
  background: #FB4A71;
  color: #fff;
}
</style>
