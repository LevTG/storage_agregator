<template>
  <footer>
    <div class="left-block">
      <div class="place_to_logo">
      </div>
      <div class="place-to-link">
        <div class="col">
          <ul>
            <li>
              <nuxt-link exact active-class="active" class="nav-link" to="/">
                Как это работает
              </nuxt-link>
            </li>
            <li>
              <nuxt-link no-prefetch active-class="active" class="nav-link" to="/partners">
                О нас
              </nuxt-link>
            </li>
            <li>
              <nuxt-link no-prefetch active-class="active" class="nav-link" to="/partners">
                Часто задаваемые вопросы
              </nuxt-link>
            </li>
          </ul>
        </div>
        <div class="col">
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
          </ul>
        </div>
      </div>
    </div>
  </footer>
</template>

<style scoped>
footer{
  display: flex;
  flex-direction: row;
  height: 400px;
  background: grey;
}
.place-to-link{
  display: flex;
}
.left-block{
  display: flex;
  flex-direction: column;
}
.place_to_logo{
  background: #999;
    display: flex;
    height: 100px;
    width: 100%;
}
ul{
  display: flex;
  flex-direction: column;
  list-style-type: disc;
  margin-block-start: 0em;
  margin-block-end: 0em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  padding-inline-start: 0px;
}
li{
  display: flex;
  margin-bottom: 20px;
}
li a{
  color: #fff;
  text-decoration: none;
}
.active{
  color: #fff;
}
</style>
