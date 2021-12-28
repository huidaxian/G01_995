<template>
  <div>
    <div class="container mgb20">
      <el-row :gutter="40">
        <el-col :span="9">
          <div class="handle-box">
            <div style="color: steelblue">suv: </div>
            <el-cascader
              class="handle-select mr10"
              v-model="car1"
              @change="handle1"
              placeholder=""
              :options="cars"
              filterable
            ></el-cascader>
          </div>
          <div class="handle-box">
            <div style="color: steelblue">轿车:</div>
            <el-cascader
              class="handle-select mr10"
              v-model="car2"
              @change="handle2"
              placeholder=""
              :options="cars"
              filterable
            ></el-cascader>
          </div>
          <div class="handle-box">
            <div style="color: steelblue">跑车:</div>
            <el-cascader
              class="handle-select mr10"
              v-model="car3"
              @change="handle3"
              placeholder=""
              :options="cars"
              filterable
            ></el-cascader>
          </div>
          <div class="handle-box">
            <div style="color: steelblue">mpv:</div>
            <el-cascader
              class="handle-select mr10"
              v-model="car4"
              @change="handle4"
              placeholder=""
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
          <schart
            class="schart"
            canvasId="line"
            :options="salesLineChart"
          ></schart>
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
    handle1(value){
      this.car1=value
      var data = new FormData();
      data.append("car1",this.car1);
    data.append("car2",this.car2);
    data.append("car3",this.car3);
    data.append("car4",this.car4);
      fetchData("post", "salesComparison.json", data).then((response) => {
        var result = response.data;
        
        this.salesLineChart = result["salesLineChart"];
      });
    },
    handle2(value){
      this.car2=value
      var data = new FormData();
      data.append("car1",this.car1);
    data.append("car2",this.car2);
    data.append("car3",this.car3);
    data.append("car4",this.car4);
      fetchData("post", "salesComparison.json", data).then((response) => {
        var result = response.data;
        
        this.salesLineChart = result["salesLineChart"];
      });
    },
    handle3(value){
      this.car3=value
      var data = new FormData();
      data.append("car1",this.car1);
    data.append("car2",this.car2);
    data.append("car3",this.car3);
    data.append("car4",this.car4);
      fetchData("post", "salesComparison.json", data).then((response) => {
        var result = response.data;
        
        this.salesLineChart = result["salesLineChart"];
      });
    },
    handle4(value){
      this.car4=value
      var data = new FormData();
      data.append("car1",this.car1);
    data.append("car2",this.car2);
    data.append("car3",this.car3);
    data.append("car4",this.car4);
      fetchData("post", "salesComparison.json", data).then((response) => {
        var result = response.data;
        this.salesLineChart = result["salesLineChart"];
      });
    }

  },
  data: function () {
    return {
      
      salesLineChart: {},
      cars: [],
      car1:1,
      car2:1,
      car3:1,
      car4:1
    };
  },
  mounted: function () {
    var data = new FormData();
    data.append("car1",this.car1);
    data.append("car2",this.car2);
    data.append("car3",this.car3);
    data.append("car4",this.car4);
    fetchData("post", "salesComparison.json", data).then((response) => {
      var result = response.data;
      this.salesLineChart = result["salesLineChart"];
      this.cars = result["cars"];
    });
    
      
    }
  
};
</script>

<style scoped>
.container {
  background: rgba(255, 255, 255, 0.9);
}

.schart {
  width: 115%;
  height: 575px;
}

.handle-box {
  margin-top: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.handle-select {
  width: 300px;
}

.img-box {
  max-height: 550px;
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