<template>
  <div style="height: 100%;">
    <div style="height: 100%;">
      <el-container style="height: 100%; border: 1px solid #eee">
        <el-header style="text-align: right; font-size: 12px">
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
        <el-container>
          <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
            <el-menu :default-openeds="['1', '3']" style="height: 100%;">
              <el-submenu index="1">
                <template slot="title"><i class="el-icon-message"></i>导航一</template>
                <el-menu-item-group>
                  <template slot="title">分组一</template>
                  <el-menu-item index="1-1">商品列表</el-menu-item>
                  <el-menu-item index="1-2">选项2</el-menu-item>
                </el-menu-item-group>
                <el-menu-item-group title="分组2">
                  <el-menu-item index="1-3">选项3</el-menu-item>
                </el-menu-item-group>
                <el-submenu index="1-4">
                  <template slot="title">选项4</template>
                  <el-menu-item index="1-4-1">选项4-1</el-menu-item>
                </el-submenu>
              </el-submenu>
              <el-submenu index="2">
                <template slot="title"><i class="el-icon-menu"></i>导航二</template>
                <el-menu-item-group>
                  <template slot="title">分组一</template>
                  <el-menu-item index="2-1">选项1</el-menu-item>
                  <el-menu-item index="2-2">选项2</el-menu-item>
                </el-menu-item-group>
                <el-menu-item-group title="分组2">
                  <el-menu-item index="2-3">选项3</el-menu-item>
                </el-menu-item-group>
                <el-submenu index="2-4">
                  <template slot="title">选项4</template>
                  <el-menu-item index="2-4-1">选项4-1</el-menu-item>
                </el-submenu>
              </el-submenu>
              <el-submenu index="3">
                <template slot="title"><i class="el-icon-setting"></i>导航三</template>
                <el-menu-item-group>
                  <template slot="title">分组一</template>
                  <el-menu-item index="3-1">选项1</el-menu-item>
                  <el-menu-item index="3-2">选项2</el-menu-item>
                </el-menu-item-group>
                <el-menu-item-group title="分组2">
                  <el-menu-item index="3-3">选项3</el-menu-item>
                </el-menu-item-group>
                <el-submenu index="3-4">
                  <template slot="title">选项4</template>
                  <el-menu-item index="3-4-1">选项4-1</el-menu-item>
                </el-submenu>
              </el-submenu>
            </el-menu>
          </el-aside>
          <el-container>
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
                  <el-button type="success" @click="get_data"><span>查询</span></el-button>
                  <el-button type="button" @click="resetForm"><span>重置</span></el-button>
                </el-form-item>
              </el-form>
              <div>
                <el-row>
                  <el-button type="success" @click="product_add">新增商品</el-button>
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
          </el-container>
        </el-container>
      </el-container>
    </div>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    name: "ProductList",
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
        this.$refs['searchForm'].resetFields();
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
