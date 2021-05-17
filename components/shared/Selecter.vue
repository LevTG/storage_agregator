<template>
<div>
  <div class="dropdown" @click="openFilter()">
    Выбери меня
  </div>
  <div class="dropdown-filter" :class="{visible: !state.isFilterOpen}">
    <div class="close" @click="openFilter()">
    </div>
    <div class="" v-for="select in selects"  :key="select">

    </div>
  </div>
</div>
</template>

<script>

import Checkbox from '@/components/shared/Checkbox'
export default {
  name: 'Selecter',
  components: {
    Checkbox
  },
  props: {
    outlined: Boolean
  },
  data () {
    return {
      state: {
        isFilterOpen: false

      },
      checkboxControler: {

      }
    }
  },
  methods: {
    openFilter() {
      this.state.isFilterOpen = !this.state.isFilterOpen
      console.log('wow')
    },
    Changer(value) {
      console.log(value)
      this.checkboxControler[value.name] = value.value
      console.log(this.checkboxControler)
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
.visible{
  display: none;
}
.dropdown{
  display: inline-flex;
  border: 1px solid gray;
  padding: 5px;
}
.dropdown-filter{
  position: relative;
  border: 1px solid gray;
  padding: 5px;
  width: 200px;
}
.close{
  position: absolute;
  width: 25px;
  height: 25px;
  right: 0px;
  top: 0px;
  background: red;
}
</style>
