<template>
  <div>
    <el-header>
      <div>
        <el-image
          src="../../../static/logo.png"
          style="float:left;height: 60px;width: 200px"
          @click="loading_home"></el-image>
      </div>
      <el-dropdown>
        <i class="el-icon-setting" style="margin-right: 15px"></i>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item>查看</el-dropdown-item>
          <el-dropdown-item>新增</el-dropdown-item>
          <el-dropdown-item>删除</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <span>王小虎</span>
    </el-header>
  </div>
</template>

<script>
  export default {
    name: "headers",
    methods: {
      // 跳转到首页
      loading_home() {
        this.$router.push({
          path: '/',
        })
      }
    }
  }
</script>

<style scoped>
  @import "headers.css";

</style>
