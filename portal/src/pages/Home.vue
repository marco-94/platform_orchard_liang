<template>
  <div>
    <h1>首页</h1>
  </div>
</template>

<script>
  export default {
    name: "Home",
    data() {
      const item = {
        date: '2016-05-02',
        name: '王小虎',
        address: '上海市普陀区金沙江路 1518 弄'
      };
      return {
        tableData: Array(20).fill(item)
      }
    }
  }
</script>

<style>
  .el-header {
    background-color: #B3C0D1;
    color: #2b542c;
    line-height: 50px;
  }

  .el-aside {
    color: #00ff00;
  }
</style>
