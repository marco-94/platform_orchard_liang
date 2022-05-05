<template>
  <div>
    <div>
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
            <el-button style="background: #18a65e;color: white" @click="product_add" :disabled="is_null">新增</el-button>
            <el-button @click="$router.back()">取消</el-button>
          </el-form-item>
        </el-form>
      </el-footer>
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
              }, 1000)
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

</style>
