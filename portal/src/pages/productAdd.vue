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
              <el-form ref="add_info" :model="add_info" label-width="80px">
                <el-form-item label="商品ID">
                  <el-input v-model="add_info.product_id" style="width: 400px"></el-input>
                </el-form-item>
                <el-form-item label="商品名称">
                  <el-input v-model="add_info.product_name" style="width: 400px"></el-input>
                </el-form-item>
                <el-form-item label="商品价格">
                  <el-input v-model="add_info.product_price" style="width: 400px"></el-input>
                </el-form-item>
                <el-form-item label="商品描述">
                  <el-input type="textarea" v-model="add_info.product_description" style="width: 400px"></el-input>
                </el-form-item>

              </el-form>
            </el-main>
            <el-footer>
              <el-form style="text-align: center">
                <el-form-item>
                  <el-button type="success" @click="product_add" :disabled="is_null">新增</el-button>
                  <el-button @click="$router.back()">取消</el-button>
                </el-form-item>
              </el-form>
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
    name: "productAdd",
    data() {
      return {
        add_info: {
          product_id: "",
          product_name: "",
          product_price: "",
          product_description: "",
        },
        is_null: true
      }
    },
    methods: {
      product_add: function () {
        let that = this;
        axios
          .post('http://127.0.0.1:8000/api/product_list_router/', {
            "product_id": this.add_info.product_id,
            "product_name": this.add_info.product_name,
            "product_price": this.add_info.product_price,
            "product_description": this.add_info.product_description,
          })
          .then(response => (
            this.$message({
              message: response.data.msg,
              type: "success"
            }),
              setTimeout(() => {
                this.$router.push({
                  path: '/product',
                });
              },1000)
          ))
          .catch(function (error) {
            if (error.response) {
              that.$message({
                message: error.response.data.data.message,
                type: 'error'
              });
            } else if (error.request) {
              that.$message({
                message: error.request,
                type: 'error'
              });
            } else {
              that.$message({
                message: error.message,
                type: 'error'
              });
            }
          });
      },
    },
    watch: {
      add_info: {
        handler: function () {
          this.is_null = this.add_info.product_id === "" ||
            this.add_info.product_name === "" ||
            this.add_info.product_price === "" ||
            this.add_info.product_description === "";
        },
        deep: true
      }
    }
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
