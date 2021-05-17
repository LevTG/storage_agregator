<template>
  <core-input
    class="default-input"
    :class="{ 'default-input_invalid': invalid }"
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
    invalid: Boolean
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
  border: 1px solid #C6C8C9;
  border-radius: 8px;
  color: #121212;

  &_invalid {
    border-color: #FF0000;
  }
}
</style>
