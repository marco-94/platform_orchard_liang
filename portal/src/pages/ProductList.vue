<template>
  <div>
    <div>
      <el-main>
        <el-form :model="search_info" ref="searchForm" :inline="true">
          <el-form-item prop="product_id" label-position="left">
            <el-input
              v-model="search_info.product_id"
              placeholder="请输入商品ID"
              @input="search_info.product_id = search_info.product_id.replace(/[^\d]/g,'')"
            ></el-input>
          </el-form-item>
          <el-form-item prop="product_name">
            <el-input v-model="search_info.product_name" placeholder="请输入商品名称"></el-input>
          </el-form-item>
          <el-form-item prop="product_price">
            <el-input v-model="search_info.product_price" placeholder="请输入商品价格"></el-input>
          </el-form-item>
          <el-form-item prop="product_description">
            <el-input v-model="search_info.product_description" placeholder="请输入商品描述"></el-input>
          </el-form-item>
          <el-form-item prop="product_name">
            <el-button @click="get_data" style="background: #18a65e;color: white"><span>查询</span></el-button>
            <el-button type="button" @click="resetForm"><span>重置</span></el-button>
          </el-form-item>
        </el-form>
        <div>
          <el-row>
            <el-button style="background: #18a65e;color: white" @click="product_add">新增商品</el-button>
          </el-row>
        </div>
        <el-table :data="tableData">
          <el-table-column prop="product_id" label="商品ID">
          </el-table-column>
          <el-table-column prop="product_name" label="商品名称">
          </el-table-column>
          <el-table-column prop="product_price" label="商品价格">
          </el-table-column>
          <el-table-column prop="product_description" label="商品描述" width="300px">
          </el-table-column>
          <el-table-column prop="create_time" label="新增时间">
          </el-table-column>
          <el-table-column prop="update_time" label="更新时间">
          </el-table-column>
          <el-table-column prop="operation" label="操作" width="300px">
            <template slot-scope="scope">
              <el-row>
                <el-button @click="product_details(scope.row)">商品详情</el-button>
                <el-button @click="product_edit(scope.row)">编辑商品</el-button>
                <el-button>删除商品</el-button>
              </el-row>
            </template>
          </el-table-column>
        </el-table>
      </el-main>
    </div>
    <Pages :pages="pages"/>
  </div>
</template>

<script>
  import axios from "axios";
  import Pages from "../components/bottom-pages/pages.vue";

  export default {
    name: "ProductList",
    components: {Pages},
    data() {
      return {
        tableData: [],
        search_info: {
          product_id: '',
          product_name: '',
          product_price: '',
          product_description: '',
        },
        pages: {
          total_page: null,
          page: 1,
          size: 10,
          total: null,
        }
      }
    },
    methods: {
      // 查询
      get_data: function () {
        axios
          .get('http://127.0.0.1:8000/api/product_list_router/', {
            params: {
              "product_id": this.search_info.product_id,
              "product_name": this.search_info.product_name,
              "product_price": this.search_info.product_price,
              "product_description": this.search_info.product_description,
              "page": this.pages.page,
              "size": this.pages.size,
            }
          })
          .then(response => (
            this.tableData = response.data.data.list,
              this.pages.total = response.data.data.total,
              this.pages.currentPage = response.data.data.total_page
          ))
          .catch(function (error) {
            console.log(error)
          });
      },
      // 跳转新增页面
      product_add() {
        this.$router.push({
          path: '/product_add',
        })
      },
      // 跳转详情页面
      product_details(row) {
        this.$router.push({
          path: '/product_details',
          query: {id: row.id}
        })
      },
      // 跳转编辑页面
      product_edit(row) {
        this.$router.push({
          path: '/product_edit',
          query: {id: row.id}
        })
      },
      // 重置查询
      resetForm() {
        // this.$refs['searchForm'].resetFields();
        this.search_info = this.$options.data().search_info;
        this.pages = this.$options.data().pages;
        this.get_data();
      },
      // 设置每页显示条数
      handleSizeChange(val) {
        console.log(`每页 ${val} 条`);
        this.pages.size = val;
        this.get_data();
      },
      // 翻页
      handleCurrentChange(val) {
        console.log(`当前页: ${val}`);
        this.pages.page = val;
        this.get_data();
      },
    },
    // 进入页面默认加载列表数据
    created() {
      this.get_data();
    },
    watch: {}
  }
</script>

<style type="text/css">
  .el-header {
    background-color: #18a65e;
    color: #2b542c;
    line-height: 50px;
  }

  .el-aside {
    color: #00ff00;
  }

  .el-table {
    font-family: "Helvetica Neue", Helvetica, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "微软雅黑", Arial, sans-serif;
  }
</style>
