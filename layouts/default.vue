<template>
  <div>
    <Navbar />
    <main>
      <Nuxt />
    </main>
    <Footer />
  </div>
</template>

<script>
import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer'
export default {
  components: {
    Navbar,
    Footer
  }
}
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap');

html{
  padding: 0px;
  font-family: sans-serif;

}
body{
  margin: 0;
  padding: 0;
  top: 0px;
}
main{
  min-height: 100vh;
  margin-top: 70px;
}

</style>
