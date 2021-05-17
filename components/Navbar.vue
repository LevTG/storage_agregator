<template>
  <nav>
    <ul>
      <li>
        <nuxt-link exact active-class="active" class="nav-link" to="/">
          Домой
        </nuxt-link>
      </li>
      <li>
        <nuxt-link no-prefetch active-class="active" class="nav-link" to="/partners">
          Партнерам
        </nuxt-link>
      </li>
      <li>
        <nuxt-link no-prefetch active-class="active" class="nav-link" to="/storage">
          Склад
        </nuxt-link>
      </li>
    </ul>
  </nav>
</template>

<style scoped>
nav{
  height: 50px;
  width: 100%;
  background: #dfdfdf;
  position: fixed;
  top: 0px;
}
ul{
  display: flex;
  height: 100%;
  flex-direction: row;
  list-style-type: disc;
  margin-block-start: 0em;
  margin-block-end: 0em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  padding-inline-start: 0px;
  align-items: center;
}
li{
  display: flex;
  margin-left: 25px;
}
li a{
  color: #777;
  text-decoration: none;
}
.active{
  color: #333;
}
</style>
