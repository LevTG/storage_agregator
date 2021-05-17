<template>
  <label class="core-checkbox">
    <input
      class="core-checkbox__input"
      type="checkbox"
      v-bind="$attrs"
      v-on="{ ...$listeners, input }"
    >

    <span class="core-checkbox__indicator">
      <inline-svg
        class="core-checkbox__indicator__icon"
        :src="require('@/assets/icons/check_on.svg')"
      />
    </span>
  </label>
</template>

<script>
import InlineSvg from 'vue-inline-svg'

export default {
  name: 'CoreCheckbox',
  components: {
    InlineSvg
  },
  methods: {
    input ({ target: { value } }) {
      this.$emit('input', value)
    }
  }
}
</script>

<style lang="scss" scoped>
.core-checkbox {
  display: flex;
  cursor: pointer;

  $core-checkbox: &;

  &__indicator {
    position: relative;
    width: 16px;
    height: 16px;
    border: 1px solid #C6C8C9;
    border-radius: 2px;

    &__icon {
      position: absolute;
      top: -1px;
      left: -1px;
      width: 18px;
      height: 18px;
      opacity: 0;
      transition: opacity .2s;
    }
  }

  &__input {
    position: absolute;
    width: 0;
    height: 0;
    opacity: 0;

    &:checked + #{$core-checkbox}__indicator {
      border-color: transparent;
    }

    &:checked + #{$core-checkbox}__indicator > #{$core-checkbox}__indicator__icon {
      opacity: 1;
    }
  }
}
</style>
