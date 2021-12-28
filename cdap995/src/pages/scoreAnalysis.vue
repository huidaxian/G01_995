<template>
  <div>
    <div class="container mgb20">
      <el-row :gutter="40">
        <el-col :span="9">
          <div class="handle-box">
            <div style="color: steelblue">选择车型：</div>
            <el-cascader
              v-model="car"
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
          <div style="height: 560px">
            <div class="score-handler">
              <h2 class="score-text">空间</h2>
              <el-rate
                class="score-bar"
                v-model="scores[0]"
                disabled
                show-score
                text-color="#ff9900"
                score-template="{value}"
              ></el-rate>
            </div>
            <div class="score-handler">
              <h2 class="score-text">动力</h2>
              <el-rate
                class="score-bar"
                v-model="scores[1]"
                disabled
                show-score
                text-color="#ff9900"
                score-template="{value}"
              >
              </el-rate>
            </div>
            <div class="score-handler">
              <h2 class="score-text">操控</h2>
              <el-rate
                class="score-bar"
                v-model="scores[2]"
                disabled
                show-score
                text-color="#ff9900"
                score-template="{value}"
              >
              </el-rate>
            </div>
            <div class="score-handler">
              <h2 class="score-text">油耗</h2>
              <el-rate
                class="score-bar"
                v-model="scores[3]"
                disabled
                show-score
                text-color="#ff9900"
                score-template="{value}"
              >
              </el-rate>
            </div>
            <div class="score-handler">
              <h2 class="score-text">舒适性</h2>
              <el-rate
                class="score-bar"
                v-model="scores[4]"
                disabled
                show-score
                text-color="#ff9900"
                score-template="{value}"
              >
              </el-rate>
            </div>
            <div class="score-handler">
              <h2 class="score-text">外观</h2>
              <el-rate
                class="score-bar"
                v-model="scores[5]"
                disabled
                show-score
                text-color="#ff9900"
                score-template="{value}"
              >
              </el-rate>
            </div>
            <div class="score-handler">
              <h2 class="score-text">内饰</h2>
              <el-rate
                class="score-bar"
                v-model="scores[6]"
                disabled
                show-score
                text-color="#ff9900"
                score-template="{value}"
              >
              </el-rate>
            </div>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import { fetchData } from "../ajax";
export default {
  data: function () {
    return {
      scores: [],
      cars: [],
      car:483
    };
  },
  methods:{
 handle(value){
   this.car=value
   var data = new FormData();
    data.append("cid",this.car)
    fetchData("post", "scoreAnalysis.json", data).then((response) => {
      var result = response.data;
      this.scores = result["scores"];
    });
 }
  },
  mounted: function () {
    var data = new FormData();
    data.append("cid",this.car)
    fetchData("post", "scoreAnalysis.json", data).then((response) => {
      var result = response.data;
      this.scores = result["scores"];
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

.score-handler {
  display: flex;
  height: 65px;
  margin: 10px;
  margin-top: 15px;
  margin-left: 50px;
}
.score-bar {
  font-size: 30px;
  margin-left: 20px;
}
.score-text {
  width: 80px;
}
</style>