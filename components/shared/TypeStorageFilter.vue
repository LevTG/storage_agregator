<template>
<div>
  <div class="dropdown" @click="openFilter()">
    Тип склада
    <div class="" v-for="item in arrCheckbox"  :key="arrCheckbox.name">

    </div>
  </div>
  <div class="dropdown-filter" :class="{visible: !state.isFilterOpen}">
    <div class="close" @click="openFilter()">
      <inline-svg
        :src="require('@/assets/icons/exitsmall.svg')"
      />
    </div>
    <div class="dropdown-title">
      Выберите то, что вам подходит
    </div>
    <checkbox style="margin-left: 12px; margin-bottom: 12px" @CheckboxChange="CheckboxChange"
      name = "cloud"
      title = "Облачное хранение"
    />
    <checkbox style="margin-left: 12px; margin-bottom: 12px" @CheckboxChange="CheckboxChange"
      name = "individual"
      title = "Индивидуальное хранение"
    />
    <checkbox style="margin-left: 12px; margin-bottom: 12px" @CheckboxChange="CheckboxChange"
      name = "responsibility"
      title = "Ответственное хранение"
    />
    <checkbox style="margin-left: 12px; margin-bottom: 12px" @CheckboxChange="CheckboxChange"
      name = "private"
      title = "Частные кладовки"
    />

  </div>
</div>
</template>

<script>

import Checkbox from '@/components/shared/Checkbox'
import InlineSvg from 'vue-inline-svg'
export default {
  name: 'DropDownFilter',
  components: {
    Checkbox,
    InlineSvg
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

      },
      arrCheckbox: {
        
      }
    }
  },
  methods: {
    openFilter() {
      this.state.isFilterOpen = !this.state.isFilterOpen
      console.log('wow')
    },
    CheckboxChange(value) {
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
  padding: 11px 16px;
  font-size: 14px;
  line-height: 20px;
  letter-spacing: 0.005em;
  border-radius: 8px;
  color: #121212;
  background-color: #F8F9FB;
}
.dropdown-filter{
  position: relative;
  border: 1px solid gray;
  border-radius: 8px;
  padding: 12px;
  width: 300px;
}
.close{
  position: absolute;
    width: 17px;
    height: 17px;
    right: 12px;
    top: 12px;
    cursor: pointer;
}
.dropdown-title{
  font-family: Roboto;
font-style: normal;
font-weight: 500;
font-size: 18px;
line-height: 25px;
margin-bottom: 12px;
/* or 25px */
}
</style>
