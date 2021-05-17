<template>
  <div v-if='show' class='modal-window'>
    <div class='modal-window-content'>
      <div class='modal-window-content_header'>
        <span> </span>
        <div class="modal-window-content_close-button" v-on:click='onClose'>
          <inline-svg
            :src="require('@/assets/icons/add.svg')"
          />
        </div>
      </div>
      <div class="title">
        <h3>{{headerText}}</h3>
      </div>
      <div class='modal-window-content_body'>
        <slot name='body'/>
      </div>
      <div class='modal-window-content_footer'>
        <slot name='footer'/>
      </div>
    </div>
  </div>
</template>

<script>
import InlineSvg from 'vue-inline-svg'
export default {
  name: 'Modal',
  components: {
    InlineSvg
  },
  props: {
    headerText: {
      type: String,
      default: ''
    },
    show: {
      type: Boolean,
      default: false
    },
    onClose: {
      type: Function
    }
  }
}
</script>

<style lang='scss' scoped>

.title{
  display: flex;
  text-align: center;
  justify-content: center;
}
.modal-window {
  position: fixed;
  background-color: rgba(0, 0, 0, 0.3);
  right: 0;
  bottom: 0;
  z-index: 1;
  margin-left: auto;
  margin-right: auto;
  width: 100%;
  height: 100%;

  &-content {
    position: relative;
    background: #FFFFFF;
    box-shadow: 5px 5px 20px 1px;
    border-radius: 8px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
    width: 500px;
    overflow: hidden;
    //height: 200px;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);

    &_header {
      padding: 16px;
      display: flex;
      justify-content: space-between;

      h3 {
        margin: 0;
      }
    }
    &_body {
      position: relative;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 20px 32px;
    }
    &_footer {
      border-top: 1px solid #eeeeee;
      display: flex;
      justify-content: center;
      padding: 16px 32px;
    }
    &_close-button {
      width: 24px;
      height: 24px;
      cursor: pointer;

      svg {
        transform: rotate(45deg) scale(2);
      }
    }
  }
}
</style>
