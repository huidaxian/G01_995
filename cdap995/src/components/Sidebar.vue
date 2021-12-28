<template>
  <div class="sidebar">
    <el-menu
      class="sidebar-el-menu"
      :default-active="onRoutes"
      :collapse="collapse"
      background-color="#324157"
      text-color="#bfcbd9"
      active-text-color="#20a0ff"
      unique-opened
      router
    >
      <template v-for="item in items">
        <template v-if="item.subs">
          <el-submenu :index="item.index" :key="item.index">
            <template #title>
              <i :class="item.icon"></i>
              <span>{{ item.title }}</span>
            </template>
            <template v-for="subItem in item.subs">
              <el-submenu
                v-if="subItem.subs"
                :index="subItem.index"
                :key="subItem.index"
              >
                <template #title>{{ subItem.title }}</template>
                <el-menu-item
                  v-for="(threeItem, i) in subItem.subs"
                  :key="i"
                  :index="threeItem.index"
                >
                  {{ threeItem.title }}</el-menu-item
                >
              </el-submenu>
              <el-menu-item v-else :index="subItem.index" :key="subItem.index"
                >{{ subItem.title }}
              </el-menu-item>
            </template>
          </el-submenu>
        </template>
        <template v-else>
          <el-menu-item :index="item.index" :key="item.index">
            <i :class="item.icon"></i>
            <template #title>{{ item.title }}</template>
          </el-menu-item>
        </template>
      </template>
    </el-menu>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      items: [
        {
          icon: "el-icon-s-home",
          index: "/index/home.html",
          title: "系统主页",
        },
        {
          icon: "el-icon-s-marketing",
          index: "/index/salesTrend.html",
          title: "销售趋势",
        },
        {
          icon: "el-icon-s-data",
          index: "/index/salesComparison.html",
          title: "销量对比",
        },
        {
          icon: "el-icon-s-flag",
          index: "/index/hotSalesArea.html",
          title: "销售热点区域",
        },
        {
          icon: "el-icon-s-finance",
          index: "/index/priceComparison.html",
          title: "价格对比",
        },
        {
          icon: "el-icon-s-goods",
          index: "/index/carPurpose.html",
          title: "购车目的",
        },
        {
          icon: "el-icon-s-operation",
          index: "/index/scoreAnalysis.html",
          title: "指标分析",
        },
        {
          icon: "el-icon-s-tools",
          index: "/index/fuelAnalysis.html",
          title: "油耗分析",
        },
      ],
    };
  },
  computed: {},
};
</script>

<style scoped>
.sidebar {
  display: block;
  position: absolute;
  left: 0;
  top: 70px;
  bottom: 0;
  overflow-y: scroll;
}
.sidebar::-webkit-scrollbar {
  width: 0;
}
.sidebar-el-menu:not(.el-menu--collapse) {
  width: 250px;
}
.sidebar > ul {
  height: 100%;
}
</style>
