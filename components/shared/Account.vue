<template>
<div>
  <div class="dropdown" @click="openFilter()">
    {{username}}
    <div class="avatar">

    </div>
  </div>
  <div class="dropdown-filter" :class="{visible: !state.isFilterOpen}">
      <div class="menu-item" @click="toLk()">
        Личный кабинет
      </div>
      <div  style="color: #FB4A71" class="menu-item" @click="exit()">
        Выход
      </div>
  </div>
</div>
</template>

<script>

import Checkbox from '@/components/shared/Checkbox'
import InlineSvg from 'vue-inline-svg'
import Api from "@/api"
export default {
  name: 'DropDownFilter',
  components: {
    Checkbox,
    InlineSvg
  },
  props: {
    username: String,
    router: Object,
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
    toLk(){
      this.$router.push('/partners/lk')
      this.openFilter()
    },
    exit(){
      this.$router.push('/')
      this.openFilter()
      this.$emit('isAuth', false)
      const api = new Api
      let self = this
      api.logout().then(
        response => {
          console.log('Выход')
          self.isAuth = false
          //console.log(response)
        }
      )
    },
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

.avatar{
  background: #FB4A71;
  width: 40px;
  height: 40px;
  border-radius: 20px;
}

.menu-item{
  cursor: pointer;
  line-height: 24px;
  padding-left: 12px;
  padding-right: 12px;
  padding-top: 5px;
  padding-bottom: 5px;
}

.menu-item:hover{
  background: #F8F9FB;
}

.visible{
  display: none;
}
.dropdown{
  display: inline-flex;
  width: 200px;
  padding: 5px;
  line-height: 40px;
  cursor: pointer;
}
.dropdown-filter{
  position: absolute;
  background: white;
  top: 71px;
  border-radius: 8px;
  padding-top: 12px;
  padding-bottom: 12px;
  width: 200px;
  box-shadow: 6px 4px 16px rgb(0 0 0 / 25%);
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
