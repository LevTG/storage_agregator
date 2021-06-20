<template>
<div>
  <div class="dropdown" @click="openFilter()" :class="{paddingbottomzero: !isEmpty}">
    <span style="margin-right: 12px">Тип хранения: </span> <span style="margin-right: 12px" v-if="isEmpty">любой</span>
    <div class="" v-for="item in arrCheckbox"  :key="item.name">
        <div class="tag"> {{item.title}} </div>
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
      name = "warm"
      title = "Теплый склад"
    />
    <checkbox style="margin-left: 12px; margin-bottom: 12px" @CheckboxChange="CheckboxChange"
      name = "cold"
      title = "Холодный склад"
    />
    <checkbox style="margin-left: 12px; margin-bottom: 12px" @CheckboxChange="CheckboxChange"
      name = "sea"
      title = "Морской контейнер"
    />
    <checkbox style="margin-left: 12px; margin-bottom: 12px" @CheckboxChange="CheckboxChange"
      name = "box"
      title = "Индивидуальный бокс (умный замок)"
    />
    <checkbox style="margin-left: 12px; margin-bottom: 12px" @CheckboxChange="CheckboxChange"
      name = "zshk"
      title = "Кладовки в ЖК"
    />
    <checkbox style="margin-left: 12px; margin-bottom: 12px" @CheckboxChange="CheckboxChange"
      name = "free"
      title = "Свободные помещения"
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
      arrCheckbox: [],
      isEmpty: true
    }
  },
  methods: {
    openFilter() {
      this.state.isFilterOpen = !this.state.isFilterOpen
      console.log('wow')
    },
    isEmptyF(){
      if(this.arrCheckbox.length == 0){
        console.log(true)
        this.isEmpty = true
        return true
      }else{
        console.log(false)
        this.isEmpty = false
        return false
      }
    },
    CheckboxChange(value) {
      console.log(value)
      this.checkboxControler[value.name] = value.value
      let array = this.arrCheckbox
      this.arrCheckbox.forEach((item, i) => {
        if(item.name == value.name && item.value == false){
          array.splice(i, 1)
        }
      });
      if(value.value == true){
            this.arrCheckbox.push(value)
      }
        this.isEmptyF()
      console.log(this.arrCheckbox)
      console.log(this.checkboxControler)
      this.$emit('set', this.checkboxControler)
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

.tag{
  display: flex;
  background: rgba(251 ,74 ,113, 0.7);
  color: white;
  margin-right: 12px;
  border-radius: 5px;
  padding-left: 5px;
  padding-right: 5px;
  margin-bottom: 12px;
}

.paddingbottomzero{
  padding-bottom: 0px !important;
}

.visible{
  display: none;
}
.dropdown{
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  padding-top: 11px;
  padding-right: 16px;
  padding-bottom: 11px;
  padding-left: 16px;
  font-size: 14px;
  line-height: 20px;
  letter-spacing: 0.005em;
  border-radius: 8px;
  color: #808080;
  cursor: pointer;
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
