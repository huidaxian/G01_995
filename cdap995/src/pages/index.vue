<template>
  <div class="about">
    <v-header />
    <v-sidebar />
    <div class="content-box">
      <div class="content">
        <router-view v-slot="{ Component }">
          <transition name="move" mode="out-in">
            <keep-alive :include="tagsList">
              <component :is="Component" />
            </keep-alive>
          </transition>
        </router-view>
      </div>
    </div>
  </div>
</template>
<script>
import vHeader from "../components/Header.vue";
import vSidebar from "../components/Sidebar.vue";
export default {
  components: {
    vHeader,
    vSidebar,
  },
  computed: {},
};
</script>

  <style scoped>
.content-box {
  background-image: url(../assets/img/bg2.jpg);
  background-size: 100%;
}
</style>