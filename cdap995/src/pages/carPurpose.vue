<template>
  <div>
    <div class="container mgb20">
      <el-row :gutter="40">
        <el-col :span="9">
          <div class="handle-box">
            <div style="color: steelblue">选择车型：</div>
            <el-cascader
             v-model="thisdata"
             @change="handle"
              class="handle-select mr10"
              placeholder="试试搜索：奔驰"
              :options="cars"
              filterable
            ></el-cascader>
          </div>
          <div class="img-box">
            <img src="../assets/img/car.jpeg" class="img-car" />
          </div>
        </el-col>
        <el-col :span="1">
          <div style="height: 550px; width: 1px; background: darkgray"></div>
        </el-col>
        <el-col :span="12">
          <schart class="schart" canvasId="pie" :options="purposes"></schart>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import Schart from "vue-schart";
import { fetchData } from "../ajax";
export default {
  name: "basecharts",
  components: {
    Schart,
  },
  methods:{
    handle(value){
      var data =new FormData()
      data.append("cid",value)
      fetchData("post", "carPurpose.json", data).then((response) => {
      
      var result = response.data;
      this.purposes = result["purposes"];
    });
    }

  },
  data: function () {
    return {
      purposes: {},
      cars: [],
      thisdata:483
    };
  },
  mounted: function () {
    var data =new FormData()
    data.append("cid",this.thisdata)
    fetchData("post", "carPurpose.json", data).then((response) => {
      
      var result = response.data;
      this.purposes = result["purposes"];
    });
    fetchData("post", "options.json", data).then((response) => {
      var result = response.data;
      this.cars = result["cars"];
    });
  },
};
</script>

<style scoped>
.container {
  background: rgba(255, 255, 255, 0.9);
}

.schart {
  width: 675px;
  height: 575px;
}

.handle-box {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.handle-select {
  width: 300px;
}

.img-box {
  max-height: 575px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  margin-top: 25%;
}

.img-car {
  width: 100%;
  border-radius: 30px;
}

.mr10 {
  margin-right: 10px;
}

.mgb20 {
  margin-bottom: 20px;
}
</style>