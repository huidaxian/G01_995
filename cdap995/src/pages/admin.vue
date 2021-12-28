<template>
  <div>
    <div class="container">
      <div class="card-title">欢迎您，管理员</div>
      <div class="search-box">
          查询：
          <el-input class="input"
          v-model="search"
          placeholder="输入用户名搜索"/>
      <el-button type="primary" @click="dialogFormVisible = true">添加用户</el-button>

<el-dialog title="用户信息" :visible.sync="dialogFormVisible">
  <el-form :model="form">
    <el-form-item label="活动名称" :label-width="formLabelWidth">
      <el-input v-model="form.name" autocomplete="off"></el-input>
    </el-form-item>
    <el-form-item label="活动区域" :label-width="formLabelWidth">
      <el-select v-model="form.region" placeholder="请选择活动区域">
        <el-option label="区域一" value="shanghai"></el-option>
        <el-option label="区域二" value="beijing"></el-option>
      </el-select>
    </el-form-item>
  </el-form>
  <div slot="footer" class="dialog-footer">
    <el-button @click="dialogFormVisible = false">取 消</el-button>
    <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
  </div>
</el-dialog>

          
      </div>
      
      <div class="table-box">
        <el-table
          :data="
            tableData.filter(
              (data) =>
                !search ||
                data.username.toLowerCase().includes(search.toLowerCase())
            )
          "
          style="width: 100%"
        >
          <el-table-column prop="no" label="序号" width="100">
          </el-table-column>
          <el-table-column prop="company" label="公司" width="240">
          </el-table-column>
          <el-table-column prop="username" label="用户名" width="180">
          </el-table-column>
          <el-table-column prop="password" label="密码" width="180">
          </el-table-column>
          <el-table-column prop="control" label="操作">
            <template slot-scope="scope">
              <el-switch
                v-model="scope.row.valid"
                active-text="启用"
                inactive-text="冻结"
              >
              </el-switch>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </div>
  </div>
</template>

<script>
import { fetchData } from "../ajax";
export default {
  name:"admin",
  methods:{
    handle(){

    }
  },
  data: function () {
    return {
        dialogFormVisible: false,
        form: {
          name: '',
          region: '',
          date1: '',
          date2: '',
          delivery: false,
          type: [],
          resource: '',
          desc: ''
        },
        formLabelWidth: '120px',
        search: "",
        tableData:[]
      }
      
     
  },
  mounted:function(){
    var data = new FormData();
    fetchData("post", "admin.json", data).then((response)=>{
        var result = response.data
        this.tableData = result["data"]         
    })
    

  }
};
</script>

<style scoped>
.container {
  background: rgba(255, 255, 255, 0.9);
}

.mgb20 {
  margin-bottom: 20px;
}

.card-title {
  font-size: 25px;
  color: #222;
  padding-bottom: 10px;
  border-bottom: 2px solid #ccc;
}

.search-box {
    margin: 20px;
}

.input {
    width: 40%;
}

.table-box {
  margin: 20px;
}
</style>