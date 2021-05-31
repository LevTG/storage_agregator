<template>
  <label>
    <textarea
      :type="type"
      v-bind="$attrs"
      v-on="{ ...$listeners, input }"
    />
  </label>
</template>

<script>
export default {
  name: 'CoreInput',
  inheritAttrs: false,
  props: {
    type: {
      type: String,
      default: 'text'
    }
  },
  methods: {
    input ({ target: { value } }) {
      this.$emit('input', value)
    }
  }
}
</script>

<style lang="scss" scoped>
label {
  display: inline-flex;
  cursor: text;
  box-sizing: border-box;
}

textarea {
  resize: none;
  min-height: 150px;
  width: 100%;
  padding: 0;
  margin: 0;
  border: none;
  outline: none;
  font: inherit;
  color: inherit;
  background-color: transparent;
}
</style>
