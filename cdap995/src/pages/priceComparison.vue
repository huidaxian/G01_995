<template>
  <div>
    <div class="container mgb20">
      <el-row :gutter="40">
        <el-col :span="9">
          <div class="handle-box">
            <div style="color: steelblue">选择车型一：</div>
            <el-select v-model="value1" filterable placeholder="请选择" @change="handle1">
    <el-option
      v-for="item in cars"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
          </div>
          <div class="handle-box">
            <div style="color: steelblue">选择车型二：</div>
            <el-select v-model="value2" filterable placeholder="请选择" @change="handle2">
    <el-option
      v-for="item in cars"
      :key="item.value"
      :label="item.label"
      :value="item.value">
    </el-option>
  </el-select>
          </div>
          <div class="img-box">
          <img src="../assets/img/car.jpeg" class="img-car" />
          </div>
          <span class="vs">V.S.</span>
          <div class="img-box">
          <img src="../assets/img/car2.jpeg" class="img-car" />
          </div>
        </el-col>
        <el-col :span="1">
              <div
                style="height: 550px; width: 1px; background: darkgray"
              ></div>
            </el-col>
        <el-col :span="12">
          <schart
            class="schart"
            canvasId="ring"
            :options="prices"
          ></schart>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
import Schart from "vue-schart";
import {fetchData} from "../ajax";
export default {
  components: {
    Schart,
  },
  data: function () {

    return {
      prices:{},
      cars:[],
      value1:487,
      value2:487
      
    };
  },
  methods:{
    handle1(value){
      this.value1=value
      var data = new FormData();
      data.append("car1",this.value1)
    data.append("car2",this.value2)
    fetchData("post", "priceComparison.json", data).then((response)=>{
        var result = response.data
        this.prices = result["prices"]         
    })
    },
    handle2(value){
      this.value2=value
      var data = new FormData();
      data.append("car1",this.value1)
     data.append("car2",this.value2)
     fetchData("post", "priceComparison.json", data).then((response)=>{
        var result = response.data
        this.prices = result["prices"]         
    })
    }


  },
  mounted: function(){
    var data = new FormData();
    fetchData("post", "options.json", data).then((response)=>{
        var result = response.data
        this.cars = result["cars"]
    })
    data.append("car1",this.value1)
    data.append("car2",this.value2)
    fetchData("post", "priceComparison.json", data).then((response)=>{
        var result = response.data
        this.prices = result["prices"]         
    })
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
  margin-top: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.handle-select {
  width: 300px;
}

.img-box{
  max-height: 575px;
  margin: 30px auto;
  display: flex;
  justify-content: center;
  align-items: center;
}

.img-car {
  width: 60%;
  border-radius: 30px;
}

.vs {
  font-size: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.mr10 {
  margin-right: 10px;
}

.mgb20 {
  margin-bottom: 20px;
}
</style>