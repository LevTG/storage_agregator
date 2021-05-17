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
  margin-top: 50px;
}

</style>
