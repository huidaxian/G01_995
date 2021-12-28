<template>
  <div>
    <el-row :gutter="20">
      <el-col :span="8">
        <el-card shadow="hover" class="card mgb20">
          <div class="user-info">
            <img src="../assets/img/img.jpg" class="user-avator" alt />
            <div class="user-info-cont">
              <div>{{ username }}，您好</div>
              <div>欢迎使用汽车大数据分析平台</div>
            </div>
          </div>
          <div class="user-info-list">
            数据更新时间：
            <span>2021-7-21 10:12:12</span>
          </div>
        </el-card>
        <el-card shadow="hover" class="card mgb20">
          <template #header>
            <div class="card-title">
              <span>使用指南</span>
            </div>
          </template>
          <div class="instructions">
            &emsp;&emsp;你可以在左侧选择相关的分析功能。<br />
            &emsp;&emsp;1. 销售趋势：汽车销售发展趋势；<br />
            &emsp;&emsp;2.销量对比：按汽车种类、汽车车型等多维度对比；<br />
            &emsp;&emsp;3. 销售热点区域：相同车型的全国热点分布；<br />
            &emsp;&emsp;4. 价格对比：不同车型的价格比对；<br />
            &emsp;&emsp;5. 购车目的：多维度展示消费者购车目的；<br />
            &emsp;&emsp;6.指标分析：车辆空间、动力、操控、外观等指标分析；<br />
            &emsp;&emsp;7. 油耗分析：不同车型的平均油耗。<br />
          </div>
        </el-card>
      </el-col>
      <el-col :span="16">
        <el-card shadow="hover" class="card mgb20" style="height: 595px">
          <template #header>
            <div class="card-title">
              <span>当前热门城市</span>
            </div>
          </template>
          <el-row :gutter="40">
            <el-col :span="16">
              <img style="width: 100%" src="../assets/img/map.png" />
            </el-col>
            <el-col :span="0.5">
              <div
                style="height: 425px; width: 1px; background: darkgray"
              ></div>
            </el-col>
            <el-col :span="5.5">
              <div style="font-size: 30px; line-height: 50px; color: #f56c6c">
                No.1 广州<br />
              </div>
              <div style="font-size: 25px; line-height: 50px; color: #e6a23c">
                No.2 北京<br />
                No.3 深圳<br />
              </div>
              <div style="font-size: 15px; line-height: 40px; color: #606266">
                No.4 武汉<br />
                No.5 成都<br />
                No.6 上海<br />
                No.7 天津<br />
                No.8 杭州<br />
                No.9 青岛<br />
                No.10 重庆
              </div>
            </el-col>
          </el-row>
        </el-card>
      </el-col>
    </el-row>
    <el-row :gutter="20">
      <el-col :span="12">
        <el-card class="card" style="height: 450px">
          <template #header>
            <div class="card-title">
              <span>当前车类销售占比</span>
            </div>
          </template>
          <schart
            class="schart"
            canvasId="pie"
            :options="salesPieChart"
          ></schart>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card class="card" style="height: 450px">
          <template #header>
            <div class="card-title">
              <span>热门车辆：</span><br />
              <div style="font-size: 15px; color: grey"
                >奥迪S7 销售趋势图</div
              >
            </div>
          </template>
          <schart
            class="schart"
            canvasId="bar"
            :options="salesTrendChart"
          ></schart>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { fetchData } from "../ajax";
import Schart from "vue-schart";
export default {
  name: "home",
  components: {
    Schart,
  },
  data: function () {
    return {
      username: "",
      salesPieChart: {},
      salesTrendChart: {},
    };
  },
  mounted: function () {
    var data = new FormData();
    
    fetchData("post", "salesComparison.json", data).then((response) => {
      var result = response.data;
      this.salesPieChart = result["salesPieChart"];
    });
    data.append("cid",483)
    fetchData("post", "salesTrend.json", data).then((response) => {
      var result = response.data;
      this.salesTrendChart = result["salesTrendChart"];
    });
  },
};
</script>

<style scoped>
.card {
  background: rgba(255, 255, 255, 0.9);
}

.user-info {
  display: flex;
  align-items: center;
  padding-bottom: 20px;
  border-bottom: 2px solid #ccc;
  margin-bottom: 20px;
}

.user-avator {
  width: 120px;
  height: 120px;
  border-radius: 50%;
}

.user-info-cont {
  padding-left: 50px;
  flex: 1;
  font-size: 14px;
  color: #999;
}

.user-info-cont div:first-child {
  font-size: 30px;
  color: #222;
}

.user-info-list {
  font-size: 14px;
  color: #999;
  line-height: 25px;
  margin-left: 20px;
}

.user-info-list span {
  margin-left: 70px;
}

.instructions {
  font-size: 14px;
  color: #222;
  line-height: 25px;
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

.schart {
  height: 300px;
}
</style>