<template>
  <div>
    <el-footer>
      <div>
        <div class="block" style="text-align: right">
          <el-pagination
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page="pages.page"
            :page-sizes="[10, 20, 30, 50]"
            :page-size="pages.size"
            :page-count="pages.total_page"
            :model="pages"
            layout="total, sizes, prev, pager, next, jumper"
            :total="pages.total">
          </el-pagination>
        </div>
      </div>
    </el-footer>
  </div>
</template>

<script>
  export default {
    name: "pages",
      props: ['pages'],
    data() {
      return {
      }
    },
    methods: {
      // 设置每页显示条数
      handleSizeChange(val) {
        console.log(`每页 ${val} 条`);
        this.pages.size = val;
        this.$parent.get_data();
      },
      // 翻页
      handleCurrentChange(val) {
        console.log(`当前页: ${val}`);
        this.pages.page = val;
        this.$parent.get_data();
      },
    },
  }
</script>

<style scoped>
  @import "pages.css";
</style>
