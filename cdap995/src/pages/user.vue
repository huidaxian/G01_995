<template>
  <div>
    <el-row :gutter="20">
      <el-col :span="12">
        <el-card shadow="hover" class="card mgb20" style="height: 432px"> 
            <template #header>
            <div class="card-title">
              <span>基础信息</span>
            </div>
          </template>
          <div class="info">
                        <div class="info-image">
                            <img src="../assets/img/img.jpg" />
                        </div>
                        <div class="info-name">{{ username }}</div>
                        <div class="info-desc">宏兴汽车有限公司</div>
                    </div>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card shadow="hover" class="card mgb20">
            <template #header>
                        <div class="card-title">
                            <span>账户编辑</span>
                        </div>
                    </template>
                    <el-form label-width="90px">
                        <el-form-item label="用户名：">{{username }}</el-form-item>
                        <el-form-item label="旧密码：">
                            <el-input type="password" v-model="password" ></el-input>
                        </el-form-item>
                        <el-form-item label="新密码：">
                            <el-input type="password" v-model="newpass"></el-input>
                        </el-form-item>
                        
                        <el-form-item>
                            <el-button type="primary" @click="onSubmit">保存</el-button>
                        </el-form-item>
                    </el-form>
             </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { fetchData } from "../ajax";

export default {
    name: "user",
    data: function(){
        return {
            username:"",
            password:"",
            newpass:"",
            

        }
    },
    methods:{
      onSubmit(){
      var data = new FormData();
      data.append("username",this.username)
    fetchData("post", "users.json", data).then((response) => {
      var result = response.data;
      if(result["password"]==this.password){
        var data = new FormData();
        data.append("username",this.username)
        data.append("password",this.newpass)
        fetchData("post", "update.json", data)
        this.$message.success("修改成功");
      }else{
        this.$message.error("修改失败");
      }
    });
      }
    },
    mounted: function(){
      this.username="user1"
        
    }
};
</script>

<style scoped>
.card {
  background: rgba(255, 255, 255, 0.9);
}

.card-title {
  font-size: 25px;
  color: #222;
  padding-bottom: 10px;
  border-bottom: 2px solid #ccc;
}

.info {
    text-align: center;
    padding: 35px 0;
}
.info-image {
    position: relative;
    margin: auto;
    width: 100px;
    height: 100px;
    background: #f8f8f8;
    border: 1px solid #eee;
    border-radius: 50px;
    overflow: hidden;
}
.info-image img {
    width: 100%;
    height: 100%;
}
.info-edit {
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    opacity: 0;
    transition: opacity 0.3s ease;
}
.info-edit i {
    color: #eee;
    font-size: 25px;
}
.info-image:hover .info-edit {
    opacity: 1;
}
.info-name {
    margin: 15px 0 10px;
    font-size: 24px;
    line-height: 70px;
    font-weight: 500;
    color: #262626;
}

.mgb20 {
  margin-bottom: 20px;
}
</style>