<template>
<div>
  <div class="dropdown" @click="openFilter()">
    Нажми меня
  </div>
  <div class="dropdown-filter" :class="{visible: !state.isFilterOpen}">
    <div class="close" @click="openFilter()">
    </div>
    <div class="dropdown-title">
      Владелец
    </div>
    <checkbox style="margin-left: 12px; margin-bottom: 12px" @CheckboxChange="CheckboxChange"
      name = "type"
      title = "Частное лицо"
    />
    <checkbox style="margin-left: 12px; margin-bottom: 12px" @CheckboxChange="CheckboxChange"
      name = "only"
      title = "Профессиональный склад"
    />
    <div class="dropdown-title">
      Наблюдение
    </div>
    <checkbox style="margin-left: 12px; margin-bottom: 12px" @CheckboxChange="CheckboxChange"
      name = "type"
      title = "Да"
    />
    <checkbox style="margin-left: 12px; margin-bottom: 12px" @CheckboxChange="CheckboxChange"
      name = "only"
      title = "Нет"
    />
    <div class="dropdown-title">
      Доступ
    </div>
    <checkbox style="margin-left: 12px; margin-bottom: 12px" @CheckboxChange="CheckboxChange"
      name = "type"
      title = "Круглосуточно"
    />

  </div>
</div>
</template>

<script>

import Checkbox from '@/components/shared/Checkbox'
export default {
  name: 'DropDownFilter',
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
  border: 1px solid gray;
  padding: 5px;
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
  width: 25px;
  height: 25px;
  right: 0px;
  top: 0px;
  background: red;
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
