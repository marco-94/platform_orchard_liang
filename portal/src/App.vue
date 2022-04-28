<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
  import Home from "./pages/Home.vue";

  export default {
    components: {Home},
    name: 'App'
  }
</script>

<style lang="scss">
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    margin-top: 60px;
  }
  html,body,#app{
  margin: 0;
  padding: 0;
  height:100%;
}
</style>
