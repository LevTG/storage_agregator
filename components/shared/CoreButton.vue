<template>
  <button
    class="core-button"
    :class="{ 'core-button_outlined': outlined }"
    v-bind="$attrs"
    v-on="$listeners"
  >
    <slot />
  </button>
</template>

<script>
export default {
  name: 'CoreButton',
  props: {
    outlined: Boolean
  }
}
</script>

<style lang="css" scoped>
.core-button {
  font-family: inherit;
  color: #121212;
  background-color: #30339B;
  padding: 0;
  margin: 0;
  border: none;
  outline: none;
  cursor: pointer;
}
</style>
