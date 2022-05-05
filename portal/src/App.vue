<template>
  <div id="app">
    <div>
      <Headers/>
    </div>
      <el-container>
        <div>
          <Tabs/>
        </div>
          <el-main>
              <router-view/>
              <div v-if="$route.meta.pagesShow">
                <Pages/>
              </div>
          </el-main>
      </el-container>
  </div>
</template>

<script>
  import Home from "./pages/Home.vue";
  import Tab from "./components/left-tab/tab";

  export default {
    components: {Tab, Home},
    name: 'App',
    data() {
      return {
      }
    },
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

  html, body, #app {
    margin: 0;
    padding: 0;
    height: 100%;
  }
</style>
