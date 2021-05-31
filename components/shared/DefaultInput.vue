<template>
  <core-input
    class="default-input"
    :class="{ 'default-input_invalid': invalid, 'white-style': white }"
    v-bind="$attrs"
    v-on="$listeners"
  />
</template>

<script>
import CoreInput from './CoreInput'

export default {
  name: 'DefaultInput',
  components: { CoreInput },
  props: {
    invalid: Boolean,
    white: Boolean
  }
}
</script>

<style lang="scss" scoped>
.default-input {
  display: inline-flex;
  padding: 11px 16px;
  font-size: 14px;
  line-height: 20px;
  letter-spacing: 0.005em;
  border-radius: 8px;
  color: #121212;
  background-color: #F8F9FB;

  &_invalid {
    border-color: #FF0000;
  }
}
.white-style{
  background-color: white;
}
</style>
