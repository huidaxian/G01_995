<template>
  <div>
    <div class="container mgb20">
      <el-row :gutter="40">
        <el-col :span="9">
          
          <div class="img-box">
            <img src="../assets/img/car.jpeg" class="img-car" />
          </div>
        </el-col>
        <el-col :span="1">
          <div style="height: 600px; width: 1px; background: darkgray"></div>
        </el-col>
        <el-col :span="12">
          <schart
            class="schart"
            canvasId="bar"
            :options="salesAreaBarChart"
          ></schart>
          <schart
            class="schart"
            canvasId="pie"
            :options="salesAreaPieChart"
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
  data: function () {
    return {
      salesAreaBarChart: {},
      salesAreaPieChart: {},
      cars: [],
    };
  },
  mounted: function () {
    var data = new FormData();
    fetchData("post", "hotSalesArea.json", data).then((response) => {
      var result = response.data;
      this.salesAreaBarChart = result["salesAreaBarChart"];
      this.salesAreaPieChart = result["salesAreaPieChart"];
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
  width: 115%;
  height: 325px;
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