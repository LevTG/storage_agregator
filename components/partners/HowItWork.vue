<template>
  <div class="body">
    <div class="place_to_img">
      <inline-svg
        class="core-checkbox__indicator__icon"
        :src="getIconPath"
      />
    </div>
    <div class="title" style="margin-bottom: 12px">
      <title-small>
        {{title}}
      </title-small>
    </div>
    <div class="text">
      <slot />
    </div>
  </div>
</template>

<script>
import InlineSvg from 'vue-inline-svg'
import TitleSmall from '@/components/shared/TitleSmall'
export default {
  name: 'HowItWork',
  components: {
    InlineSvg,
    TitleSmall
  },
  props: {
    title: {
      type: String,
      default: 'Впиши сюда титл'
    },
    img: {
      type: String,
      default: ''
    }
  },
  computed: {
    getIconPath () {
      return this.img ? require('@/assets/icons/img/' + this.img) : ''
    }
  }
}
</script>

<style lang="scss" scoped>
.body{
  width: calc(33% - 48px);
  padding-left: 24px;
  padding-right: 24px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.place_to_img{
  width: 100px;
  height: 100px;
  border-radius: 50px;
  background: #F8F9FB;
  display: flex;
  margin-left: auto;
  margin-right: auto;
  justify-content: center;
  align-items: center;
  margin-bottom: 30px;
}
</style>
