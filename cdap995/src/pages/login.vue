<template>
  <div class="login-wrap">
    <div class="ms-login">
      <div class="ms-title">
        <img style="max-height: 300px" src="../assets/img/title.png" />
      </div>
      <el-form
        :model="param"
        :rules="rules"
        ref="login"
        label-width="0px"
        class="ms-content"
      >
        <el-form-item prop="username">
          <el-input v-model="username" placeholder="请输入用户名">
            <template #prepend>
              <el-button icon="el-icon-user"></el-button>
            </template>
          </el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input v-model="password" type="password" placeholder="请输入密码">
            <template #prepend>
              <el-button icon="el-icon-lock"></el-button>
            </template>
          </el-input>
        </el-form-item>
        <div class="login-btn">
          <el-button type="primary" @click="login()">登录</el-button>
        </div>
      </el-form>
    </div>
  </div>
</template>

<script>
import { fetchData } from "../ajax";

export default {
  name: "login",
  data: function () {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    login: function () {
      var data = new FormData();
      data.append("username",this.username)
      // 发起请求
      fetchData("post", "users.json", data).then((response) => {
        console.log(response);
        // 获取数据
        var result = response.data;
        if (
          result &&
          result["password"] == this.password&&
          result["status"]!="frozen"
          
        ) {
          this.$message.success("登录成功");
          if(result["status"]=="normal"){
          this.$router.push('/index');
          }else{
            this.$router.push('/admin.html');
          }
        } else {
          this.$message.error("登录失败");
        }
      });
    },
  },
};
</script>

<style scoped>
.login-wrap {
  position: relative;
  width: 100%;
  height: 100%;
  background-image: url(../assets/img/login-bg.jpg);
  background-size: 100%;
}
.ms-title {
  display: flex;
  justify-content: center;
  align-items: center;
}
.ms-login {
  position: absolute;
  left: 50%;
  top: 45%;
  width: 350px;
  margin: -190px 0 0 -175px;
  border-radius: 5px;
  background: rgba(255, 255, 255, 0.3);
  overflow: hidden;
}
.ms-content {
  padding: 0px 30px;
}
.login-btn {
  text-align: center;
}
.login-btn button {
  width: 100%;
  height: 36px;
  margin-bottom: 30px;
}
.login-tips {
  font-size: 12px;
  line-height: 30px;
  color: #fff;
}
</style>
