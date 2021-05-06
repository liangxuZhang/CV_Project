 
<template>
<el-container style="height: 800px; border: 1px solid #eee">

  <el-aside width="35%" style="background-color: rgb(238, 241, 246)" height="600px">
    <el-table class="tableBox"
    :data="tableData.slice((currentPage-1)*pageSize, currentPage*pageSize)"
    size="small"
    tooltip-effect="dark" border
    style="font-size: 8px height: 100% width: 90%"
    ref="multipleTable"
    :default-sort = "{prop: '告警时间'}"
    @row-click="ShowPicture">
        <el-table-column prop="告警时间" label="时间" sortable></el-table-column>
        <el-table-column prop="XL" label="地点"></el-table-column>
        <el-table-column prop="GT" label="摄像头"></el-table-column>
        <el-table-column prop="监拍朝向" label="监拍朝向"></el-table-column>
        <el-table-column prop="单位" label="单位"></el-table-column>
        <el-table-column prop="告警原因" label="告警原因"></el-table-column>
    </el-table>
    <el-pagination
     
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="currentPage"
      :page-sizes="[10, 20, 30, 50]"
      :page-size= "pagesize"
      layout="total, sizes, prev, pager, next, jumper"
      :total= "total">
    </el-pagination>
  </el-aside>
  <el-container>
    <el-header style="text-align: right; font-size: 12px">
    </el-header>

    <el-main>
        <p>{{msg}}</p>
    </el-main>
  </el-container>
</el-container>
</template>

<script>

  export default {
    data() {
      const item = {
        告警时间: '2020-04-19 00:30',
            XL: 'ningjiang',
            GT: '#34',
            监拍朝向:'大号侧',
            单位:'ningjin',
            告警原因:'导线异物'
      };
      return {
        total: 100,
        pagesize: 20,
        currentPage: 1,
        tableData: Array(100).fill(item),
        msg: 'hello'
      }
    },
    methods:{
      handleSizeChange(val) {
        console.log(`每页 ${val} 条`);
        this.pageSize = val
      },
      handleCurrentChange(val) {
        this.currentPage = val
        console.log(`当前页: ${val}`);
      },
      ShowPicture(row){
        console.log(row.告警时间)
        this.msg = row.告警时间
      }
    }
  };
</script>

<style>
.el-header {
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }

.el-aside {
    color: #333;
  }
</style>
