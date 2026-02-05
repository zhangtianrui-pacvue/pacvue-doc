---
component: PacvueChart
category: chart
tags: [图表, 可视化, 数据图]
aliases: [PacvueChart, 图表]
version: 1.0.0
description: "线图基础用法"
---

# PacvueChart 组件文档

> 线图基础用法

**分类**: chart | **标签**: 图表、可视化、数据图

## 使用示例

### PacvueChart基础使用 -->

```vue
<template>
  <pacvue-chart
    :isShowSwitch="true"
    :markerEnable="true"
    :formatMarker="formatMarker"
    style="width: 100%"
    :series="series"
    xValue="Date"
    chartId="Test"
    :data="charData"
    :loading="loading"
    :height="0"
    :xCountBol="false"
    :hideXExtremeLabel="false"
    showLegend
    :isSortByYAxis="false"
    :isKeepZeroAfterDigit="true"
    :navigator="{}"
    :isAutoXAxisFit="true"
    :autoXAxisThrold="2"
    :xTickCount="8"
  ></pacvue-chart>
</template>

<script setup>
  import { ref } from 'vue'
  var chartData = ref([])
  var loading = ref(false)
  setTimeout(() => {
    //loading.value= false
    var res = []
    for (var i = 0; i < 60; i++) {
      res.push({
        Date: `2020/06/${i}`,
        Orders: 10 + i + 0.13,
        adOrders: 12 + i + 0.13,
        clicks: i % 2 ? null : 12,
        spend: 14 + i + 0.13
      })
    }
    charData.value = res
  }, 2000)

  //案列1
  var formatMarker = ({ record, xAxisName, serieName }) => {
    if (record.Date == '2020/01/02' && serieName == 'Orders') {
      console.log('>>>>>>record', serieName, record, xAxisName)
      return {
        //marketSymbol: undefined, //iconMarker,
        marketLabel: undefined,
        events: {
          click(event) {
            console.log('>>>>>>>>>event', event)
          }
        }
      }
    }
  }

  var series = ref([
    {
      title: 'Orders',
      data: 'Orders',
      zIndex: 0,
      yAxis: 0,
      chartType: 'areaspline',
      color: '#FCC473',
      onPoint: {
        position: {
          offsetY: 20
        }
      },

      mouseOut: undefined,
      mouseOver: undefined,

      yLabelFormat(value, moneyCode) {
        return value + '.00'
      },
      dataLabels: {
        enabled: true,
        color: '#e00000', //字体颜色
        useHTML: true,
        formatter() {
          var x = this.x
          var authData = this.point.authData //行数据
          var y = this.y
          if (x == '2020/01/01' || x == '2020/06/0') {
            return `<div style="display: flex;flex-direction: column;align-items: center;">
                    <div style='backgroud:#66666C;font-size:14px;'>Peak at</div>
                    <div style='backgroud:#66666C;font-size:14px;'>Rise Since</div>
                  </div>`
          }
        }
      },
      render: function (value, moneyCode) {
        return '$' + value
      }
    },
    {
      title: 'Ad Orders',
      data: 'adOrders',
      zIndex: 0,
      yAxis: 1,
      chartType: 'areaspline',
      mouseOut: undefined,
      mouseOver: undefined,
      color: '#FCC473',
      guideTextFontWeight: 700,
      lineWidth: 4,
      isOnlyLastGuide: false,
      guideText: (info) => {
        return 'QQQ 提示' + info.y
      },
      render: function (value, moneyCode) {
        return value + '%'
      }
    },
    {
      title: 'Clicks',
      data: 'clicks',
      zIndex: 0,
      yAxis: 2,
      chartType: 'areaspline',
      mouseOut: undefined,
      mouseOver: undefined,
      color: '#0747a6',
      guideTextFontWeight: 700,
      lineWidth: 4,
      guideText: (info) => {
        return 'QQQ 提示222' + info.y
      },
      isOnlyLastGuide: false,
      render: function (value, moneyCode) {
        return value + '$$$'
      }
    }
  ])
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### 示例：index2

```vue
<template>
  <div id="pacvue-chart2" style="height: 300px; width: 100%"></div>
</template>

<script setup>
  import { onMounted } from 'vue'
  import { PacvueHighchart, PacvueHighchartRender } from '"@pacvue/element-plus'
  onMounted(() => {
    var pieData = [
      {
        name: 'Auto',
        y: 20,
        color: '#ffaba5'
      },
      {
        name: 'Manual',
        y: 30,
        color: '#aba0ec'
      }
    ]
    var pacvueHighchart = PacvueHighchartRender({
      chartId: 'pacvue-chart2',
      chartType: 'pie',
      showDataLabel: true,
      data: pieData,
      hasLegend: false,
      size: 220,
      totalName: 'Spend',
      size: 200,
      render: function (val, fieldName) {
        return val
        //return formatSpendsMoney(val, monenyCode)
      }
    })
  })
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### PacvueChart基础使用 -->

```vue
<template>
  <div id="pacvue-chart2" style="height: 300px; width: 100%"></div>
</template>

<script setup>
  import { onMounted } from 'vue'
  import { PacvueHighchart, PacvueHighchartRender } from '"@pacvue/element-plus'
  onMounted(() => {
    var pieData = [
      {
        name: 'Auto',
        y: 20,
        color: '#ffaba5'
      },
      {
        name: 'Manual',
        y: 30,
        color: '#aba0ec'
      }
    ]
    var pacvueHighchart = PacvueHighchartRender({
      chartId: 'pacvue-chart2',
      chartType: 'pie',
      showDataLabel: true,
      data: pieData,
      hasLegend: false,
      size: 220,
      totalName: 'Spend',
      size: 200,
      render: function (val, fieldName) {
        return val
        //return formatSpendsMoney(val, monenyCode)
      }
    })
  })
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### PacvueChart基础使用 -->

```vue
<template>
  <pacvue-chart
    :isShowSwitch="true"
    :markerEnable="true"
    :formatMarker="formatMarker"
    style="width: 100%"
    :series="series"
    xValue="Date"
    chartId="Test"
    :data="charData"
    :loading="loading"
    :height="0"
    :xCountBol="false"
    :hideXExtremeLabel="false"
    showLegend
    :isSortByYAxis="false"
    :isKeepZeroAfterDigit="true"
    :navigator="{}"
    :isAutoXAxisFit="true"
    :autoXAxisThrold="2"
    :xTickCount="8"
  ></pacvue-chart>
</template>

<script setup>
  import { ref } from 'vue'
  var chartData = ref([])
  var loading = ref(false)
  setTimeout(() => {
    //loading.value= false
    var res = []
    for (var i = 0; i < 60; i++) {
      res.push({
        Date: `2020/06/${i}`,
        Orders: 10 + i + 0.13,
        adOrders: 12 + i + 0.13,
        clicks: i % 2 ? null : 12,
        spend: 14 + i + 0.13
      })
    }
    charData.value = res
  }, 2000)

  //案列1
  var formatMarker = ({ record, xAxisName, serieName }) => {
    if (record.Date == '2020/01/02' && serieName == 'Orders') {
      console.log('>>>>>>record', serieName, record, xAxisName)
      return {
        //marketSymbol: undefined, //iconMarker,
        marketLabel: undefined,
        events: {
          click(event) {
            console.log('>>>>>>>>>event', event)
          }
        }
      }
    }
  }

  var series = ref([
    {
      title: 'Orders',
      data: 'Orders',
      zIndex: 0,
      yAxis: 0,
      chartType: 'areaspline',
      color: '#FCC473',
      onPoint: {
        position: {
          offsetY: 20
        }
      },

      mouseOut: undefined,
      mouseOver: undefined,

      yLabelFormat(value, moneyCode) {
        return value + '.00'
      },
      dataLabels: {
        enabled: true,
        color: '#e00000', //字体颜色
        useHTML: true,
        formatter() {
          var x = this.x
          var authData = this.point.authData //行数据
          var y = this.y
          if (x == '2020/01/01' || x == '2020/06/0') {
            return `<div style="display: flex;flex-direction: column;align-items: center;">
                    <div style='backgroud:#66666C;font-size:14px;'>Peak at</div>
                    <div style='backgroud:#66666C;font-size:14px;'>Rise Since</div>
                  </div>`
          }
        }
      },
      render: function (value, moneyCode) {
        return '$' + value
      }
    },
    {
      title: 'Ad Orders',
      data: 'adOrders',
      zIndex: 0,
      yAxis: 1,
      chartType: 'areaspline',
      mouseOut: undefined,
      mouseOver: undefined,
      color: '#FCC473',
      guideTextFontWeight: 700,
      lineWidth: 4,
      isOnlyLastGuide: false,
      guideText: (info) => {
        return 'QQQ 提示' + info.y
      },
      render: function (value, moneyCode) {
        return value + '%'
      }
    },
    {
      title: 'Clicks',
      data: 'clicks',
      zIndex: 0,
      yAxis: 2,
      chartType: 'areaspline',
      mouseOut: undefined,
      mouseOver: undefined,
      color: '#0747a6',
      guideTextFontWeight: 700,
      lineWidth: 4,
      guideText: (info) => {
        return 'QQQ 提示222' + info.y
      },
      isOnlyLastGuide: false,
      render: function (value, moneyCode) {
        return value + '$$$'
      }
    }
  ])
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| data | 数据列表。数据源，用于渲染组件内容 | Array | [] |
| series | chart图serie配置为Array<Serie>如下表 | Array | [] |
| xValue | X轴取的字段属性值 | String | xValue |
| chartId | 生成chart容器的id名称 | String | 时间戳+_chart |
| loading | 是否显示loading。是否显示加载状态 | Boolean | false |
| loadingType | loaidng显示的类型，pacvue\|small | String | pacvue |
| height | chart的高度。组件高度，支持像素值或百分比 | Number | 300 |
| title | chart的标题 | String | Performance |
| ylabelColorAuto | chart的y轴label颜色是否跟随series中配置的颜色变化 | Boolean | true |
| showLegend | 是否显示legend图列 | Boolean | false |
| showHeader | 是否显示chart头部 | Boolean | true |
| xFormat | X轴label格式化 | Function(xValue) | -- |
| marketCode | 将市场装换为货币符号 | Function(market) | 默认返回$ |
| chartShow | 是否显示chart图表 | Boolean | true |
| formatMarker | Function({ record, xAxisName }),返回对象 | Function | -- |
| formatMarkerOffset | 定制图标偏移量 | Object<{x,y}> | {y:-16} |
| isSortByYAxis | 是否根据yAxis类别进行排序 | Boolean | true |
| xStep | x轴的步长 | Number | 6 |
| xTickCount | x轴刻度的个数 | Number | 6 |
| hideXExtremeLabel | 是否隐藏X轴首尾断点label | Boolean | true |
| xCountBol | false为默认,true为不设置x轴显示个数,设置为数字时可以设置x轴的显示个数 | Number\|Boolean | false |
| stacking | column中类别中stacking配置 | String | -- |
| seriesStacking | serie中类别中stacking配置 | String | -- |
| navigator | 导航器是主系列下面的一个小系列，显示整个数据集的视图。它提供了放大和缩小部分数据以及在数据集中平移的工具。 | Object | -- |
| xAxisCrosshair | false为默认,x轴的crosshair配置 | Object\|Boolean | false |
| tootltipBgColor | tooltip的背景色 | String | rgba(255,255,255,0.80) |
| isKeepZeroAfterDigit | 是否保持Y轴label后小数点的零 | Boolean | false |
| isAutoXAxisFit | 是否X轴Label显示个数根据宽度自适应 | Boolean | false |
| autoXAxisThrold | X轴Label显示个数根据宽度自适应阀值，越小越紧凑 | Number<Integer> | 1 |
| chartPadding | chart的padding配置 | Array<{left,top,right,bottom}> | 1 |
| xAxisConfig | X轴其他配置,具体可以参考Highchart官网的xAxis配置 | Object | -- |
| useCustomLegend | 是否使用自定义legend功能,插槽具体使用如下 | Boolean | false |
| tooltipConfig | tooltip相关自定义配置,具体请参考Highchart中tooltip配置 | Object | -- |
| berforeRenderInterceptors | 添加渲染前拦截器 | Array<Function(config)> | -- |
| title | 显示的serie标题 | String | -- |
| data | serie取的字段属性值。数据源，用于渲染组件内容 | String | -- |
| zIndex | serie的图表层次 | Number | 0 |
| yAxis | y轴的类别，主轴为0，次轴为1，三轴为2 | Number | 0 |
| chartType | chart的类型，为spline,line,column,pie,spider等 | Number | -- |
| color | 当前serie的颜色 | Number | -- |
| render | 当前serie的值格式化函数 | Function(value, moneyCode) | -- |
| yLabelFormat | 当前serie的yz轴值格式化函数，如果没有则使用render方法 | Function(value, moneyCode) | -- |
| dataLabels | 当前dataLabel配置项，详情可以参考highchart中dataLabels配置 | -- | -- |
| minTickInterval | 最小刻度间隔 | -- | -- |
| tickAmount | y轴刻度个数 | 5 | -- |
| isKeepZeroAfterDigit | 是否保持Y轴label后小数点的零,如果设置了优先级高于全局设置的 | -- | -- |
| serieConfig | 单个serie的相关配置 | Object | -- |
| serieYConfig | 单个serie中data的每条数据的相关配置 | Function({ val, record, filedName }) | -- |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| toolbarLeft | 显示在标题左边边的插槽 | -- |
| toolbar | 显示在标题右边的插槽 | -- |
| empty | 数据为空时的插槽 | -- |
| legend | 整个legend渲染插槽,slotScop为legendList:Array<{visible,dataIndex, color, name, show,hide}> | -- |
| legend-aside | legend的辅助信息 | -- |
| header | 表头信息 | -- |

