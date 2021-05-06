
<template>
<div style="height: 600px">
<el-row class="tac">
  <el-col :span="6">
    <el-menu
      :uniqueOpened="false"
      default-active="1"
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose"
      >
      <el-submenu v-for="i in 3" :index="i+''" :key="i+''">
        <template #title>
          <span v-text="'Camera'+i"></span>
        </template>
        <el-submenu v-for="j in 3" :key="i+'-'+j" :index="i+'-'+j">
          <template #title>
            <span v-text="'预置点'+j"></span>
          </template>
          <el-menu-item-group>
          <el-menu-item :index="i+'-'+ j +'-1'" @click.native="showTm(i+j)">设备1</el-menu-item>
          <el-menu-item :index="i+'-'+ j +'-2'" >设备2</el-menu-item>
          <el-menu-item :index="i+'-'+ j +'-3'" >设备3</el-menu-item>
        </el-menu-item-group>
        </el-submenu>
      </el-submenu>
    </el-menu>
  </el-col>
  <el-col :span="18"></el-col>
</el-row>
</div>
</template>

<script>
  export default {
    data(){
      const list = [
        {text: 'Camera#1'},
        {text: 'Camera#2'},
        {text: 'Camera#3'}
      ];
      return{
        list:list
      }
    },
    methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      },
      showTm(index){
        console.log(index)
      }
    }
  }
</script>

<style>

</style>
