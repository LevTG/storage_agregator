<template>
  <div class="place-to-checkbox">
    <div class="checkbox">
      <core-checkbox @change="CheckboxChange()"/>
    </div>
    <div class="title">
      {{title}}
    </div>
  </div>
</template>

<script>

import CoreCheckbox from '@/components/shared/CoreCheckbox'

export default {
  name: 'Checkbox',
  components: {
    CoreCheckbox
  },
  props: {
    title: {
      type: String,
      default: ''
    },
    name: {
      type: String,
      default: ''
    }
  },
  data () {
    return {
        state: {
          name: '',
          value: false,
          title: ''
        }
    }
  },
  methods: {
    CheckboxChange() {
      this.state.value = !this.state.value
      console.log(this.state)
      this.$emit('CheckboxChange', this.state)
    }
  },
  beforeMount: function(){
      this.state.name = this.name
      this.state.title = this.title
  }

}
</script>

<style lang="css" scoped>
.place-to-checkbox{
  display: flex;
  flex-direction: row;
}
.checkbox{
  display: flex;
}
.title{
  display: flex;
  margin-left: 12px;
}
</style>
