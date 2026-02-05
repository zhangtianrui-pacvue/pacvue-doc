---
component: Panel
category: layout
tags: [面板, 容器, 布局]
aliases: [Panel, 面板]
version: 1.0.0
description: "基础用法"
---

# Panel 组件文档

> 基础用法

**分类**: layout | **标签**: 面板、容器、布局

## 使用示例

### 可以设置显示的指标,使用v-model绑定当前选中的指标

```vue
<template>
  <PacvuePanel ref="panel" :dragDataList="dialogDataList" @change="change" v-model="value" v-model:showList="showList" @update:show-list="updateShowList" :isAutoFit="true" :showAdd="false">
</template>
<script setup>
  import { ref } from 'vue'
  var value = ref([

])
 var PavcueAdvertisingGetSummary = () => {
  var columnMap = {
    Impressions: 'Impression',
    Clicks: 'Clicks',
    CTR: 'CTR',
    Spend: 'Spend',
    Sales: 'Sales',
    CPC: 'CPC',
    CPA: 'CPA',
    ACOS: 'ACOS',
    Orders: 'Orders',
    SaleUnits: 'SaleUnits',
    ROAS: 'ROAS',
    CVR: 'CVR',
    NewToBrandSales: 'NewToBrandSales'
    //添加更多参数,
  }
  for (var i = 0; i < 12; i++) {
    var proIndexName = 'Spend' + i + ' dsfsfss dffaff dfffsf weqeq weqwewqeq wqeqe'
    columnMap[proIndexName] = proIndexName
  }
  //columnMap.NewToBrandSales = 'NewToBrandSales';
  var displayTitle = {
    TotalCost: 'Total Cost',
    SaleUnits: 'Sale Units',
    PurchaseRate: 'Purchase Rate',
    ClickThroughs: 'Click-T',
    TotalROAS: 'T-ROAS',
    TotalUnitsSold: 'T-Units Sold',
    SalesUSD: 'Sales USD',
    ConversionRate: 'CVR',
    NewToBrandSales: 'NTB Sales'
  }
  var proIndexs = []
  for (var columnName in columnMap) {
    var showName = displayTitle[columnName] ? displayTitle[columnName] : columnName
    var prop = columnMap[columnName]
    var proIndexItem = {
      label: showName,
      code: columnName,
      prop: prop,
      id: prop,
      value: 30,
      comparVal: columnName == 'Spend' ? 0 : 10,
      changeVal: columnName == 'Spend' ? 0 : 30,
      changeOriginVal: 10, //原始值,
      tip: '测试tip'
    }
    proIndexs.push(proIndexItem)
  }
  return proIndexs
}
var summaryList = PavcueAdvertisingGetSummary()
  var change = (value) => {
    console.log('组件执行了', value)
  }
  var updateShowList = (showList) => {
  console.log('>>>>>>>showList', showList)
}
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### 可以设置isShowCompar是否显示指标的对比数据

```vue
<template>
  <PacvuePanel
    ref="panel"
    :dragDataList="dialogDataList"
    @change="change"
    v-model="value2"
    v-model:showList="showList2"
    :isShowCompar="isShowCompar"
    @update:show-list="updateShowList"
    v-bind:is-show-download="true"
    v-model:tab-name="tabName"
    v-bind:is-show-switch="true"
    :hasPlan="true"
    @save="handleSavePlan"
    :planList="planList"
    :defaultPlan="defaultPlan"
    @delete="handleDelPlan"
  ></PacvuePanel>
</template>

<script setup>
  import { ref } from 'vue'
  var tabName = ref('Performance') //切换Performance和散点图
  var isShowCompar = ref(true) //是否显示对比数据
  var value2 = ref([
    { prop: 'Impression', color: '#FFB268' },
    { prop: 'SaleUnits', color: '#6ADFA7' },
    { prop: 'Clicks', color: '#9B88FA' }
  ])
  var showList2 = ref(['Impression', 'SaleUnits', 'Clicks', 'ACOS', 'Orders', 'Spend', 'Sales', 'CPC', 'CPA', 'CTR']) //显示列表
  var PavcueAdvertisingGetSummary = () => {
    var columnMap = {
      Impressions: 'Impression',
      Clicks: 'Clicks',
      CTR: 'CTR',
      Spend: 'Spend',
      Sales: 'Sales',
      CPC: 'CPC',
      CPA: 'CPA',
      ACOS: 'ACOS',
      Orders: 'Orders',
      SaleUnits: 'SaleUnits',
      ROAS: 'ROAS',
      CVR: 'CVR'
      //NewToBrandSales:'NewToBrandSales',
    }
    //columnMap.NewToBrandSales = 'NewToBrandSales';
    var displayTitle = {
      TotalCost: 'Total Cost',
      SaleUnits: 'Sale Units',
      PurchaseRate: 'Purchase Rate',
      ClickThroughs: 'Click-T',
      TotalROAS: 'T-ROAS',
      TotalUnitsSold: 'T-Units Sold',
      SalesUSD: 'Sales USD',
      ConversionRate: 'CVR',
      NewToBrandSales: 'NTB Sales'
    }
    var proIndexs = []
    for (var columnName in columnMap) {
      var showName = displayTitle[columnName] ? displayTitle[columnName] : columnName
      var prop = columnMap[columnName]
      var proIndexItem = {
        label: showName,
        code: columnName,
        prop: prop,
        id: prop,
        value: 30,
        comparVal: 10,
        changeVal: 30,
        changeOriginVal: 10 //原始值
      }
      proIndexs.push(proIndexItem)
    }
    return proIndexs
  }
  var summaryList = PavcueAdvertisingGetSummary()
  var dialogDataList = ref(summaryList)
  var updateShowList = (showList) => {
    console.log('>>>>>>>showList', showlist)
  }
  var change = (value) => {
    console.log('组件执行了', value)
  }
  const planList = ref([
  {
    planId: 1,
    planName: 'Plan-1Plan-1Plan-1Plan-1Plan-1Plan-1Plan-1Plan-1Plan-1Plan-1Plan-1Plan-1Plan-1Plan-1Plan-1Plan-1Plan-1Plan-1',
    showList: ['Impression', 'SaleUnits', 'Clicks', 'Spend', 'Sales'],
    selectedList: [
      { prop: 'Impression', color: 'var(--project-orange)' },
      { prop: 'Clicks', color: '#6ADFA7' },
      { prop: 'Spend', color: '#9B88FA' }
    ],
    dataList: PavcueAdvertisingGetSummary({ CTR: 'CTR', Spend: 'Spend', Sales: 'Sales', CPC: 'CPC', CPA: 'CPA' })
  },
  {
    planId: 2,
    planName: 'Plan-2',
    showList: ['SaleUnits', 'Clicks', 'Spend', 'Sales'],
    selectedList: [
      { prop: 'Clicks', color: 'var(--project-orange)' },
      { prop: 'Spend', color: '#6ADFA7' },
      { prop: 'Sales', color: '#9B88FA' }
    ],
    dataList: PavcueAdvertisingGetSummary({ Spend: 'Spend', Sales: 'Sales', CPC: 'CPC', CPA: 'CPA', ACOS: 'ACOS', Orders: 'Orders', SaleUnits: 'SaleUnits', ROAS: 'ROAS', CVR: 'CVR' })
  },
  {
    planId: 3,
    planName: 'Plan-3',
    showList: ['Impression', 'Spend', 'Sales'],
    selectedList: [
      { prop: 'Sales', color: 'var(--project-orange)' },
      { prop: 'Spend', color: '#6ADFA7' },
      { prop: 'Impression', color: '#9B88FA' }
    ]
  }
])
let index = 3
const defaultPlan = {
  showList: ['Impression', 'SaleUnits', 'Clicks', 'Spend', 'Sales'],
  selectedList: [
    { prop: 'Impression', color: 'var(--project-orange)' },
    { prop: 'SaleUnits', color: '#6ADFA7' },
    { prop: 'Clicks', color: '#9B88FA' }
  ]
}
  const handleSavePlan = (planInfo, reslove) => {
  const planId = planInfo.planId
  if (planId) {
    let planIndex = planList.value.findIndex((item) => item.planId == planInfo.planId)
    planList.value[planIndex] = { ...planInfo }
    //编辑
  } else {
    ++index
    planList.value = [{ ...planInfo, planId: index }].concat(planList.value)
  }
  reslove(true, planId ? undefined : { planId: index })
}
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### 可以设置isShowCompar是否显示指标的对比数据

```vue
<template>
  <PacvuePanel
    ref="panel"
    :dragDataList="dialogDataList"
    @change="change"
    v-model="value2"
    v-model:showList="showList3"
    :isShowCompar="isShowCompar"
    :showAdd="false"
    :isAutoFit="true"
    @update:show-list="updateShowList"
    v-bind:is-show-download="true"
    v-model:tab-name="tabName"
    v-bind:is-show-switch="true"
  ></PacvuePanel>
</template>

<script setup>
  import { ref } from 'vue'
  var tabName = ref('Performance') //切换Performance和散点图
  var isShowCompar = ref(true) //是否显示对比数据
  var value2 = ref([
    { prop: 'Impression', color: '#FFB268' },
    { prop: 'SaleUnits', color: '#6ADFA7' },
    { prop: 'Clicks', color: '#9B88FA' }
  ])
  var showList3 = ref(['Impression', 'SaleUnits', 'Clicks']) //显示列表
  var PavcueAdvertisingGetSummary = () => {
    var columnMap = {
      Impressions: 'Impression',
      Clicks: 'Clicks',
      CTR: 'CTR',
      Spend: 'Spend',
      Sales: 'Sales',
      CPC: 'CPC',
      CPA: 'CPA',
      ACOS: 'ACOS',
      Orders: 'Orders',
      SaleUnits: 'SaleUnits',
      ROAS: 'ROAS',
      CVR: 'CVR'
      //NewToBrandSales:'NewToBrandSales',
    }
    //columnMap.NewToBrandSales = 'NewToBrandSales';
    var displayTitle = {
      TotalCost: 'Total Cost',
      SaleUnits: 'Sale Units',
      PurchaseRate: 'Purchase Rate',
      ClickThroughs: 'Click-T',
      TotalROAS: 'T-ROAS',
      TotalUnitsSold: 'T-Units Sold',
      SalesUSD: 'Sales USD',
      ConversionRate: 'CVR',
      NewToBrandSales: 'NTB Sales'
    }
    var proIndexs = []
    for (var columnName in columnMap) {
      var showName = displayTitle[columnName] ? displayTitle[columnName] : columnName
      var prop = columnMap[columnName]
      var proIndexItem = {
        label: showName,
        code: columnName,
        prop: prop,
        id: prop,
        value: 30,
        comparVal: 10,
        changeVal: 30,
        changeOriginVal: 10 //原始值
      }
      proIndexs.push(proIndexItem)
    }
    return proIndexs
  }
  var summaryList = PavcueAdvertisingGetSummary()
  var dialogDataList = ref(summaryList)
  var updateShowList = (showList) => {
    console.log('>>>>>>>showList', showlist)
  }
  var change = (value) => {
    console.log('组件执行了', value)
  }
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
| dragDataList | 显示的指标列表,数据格式为Array<DragItemInfo>,DragItemInfo为指标的详细信息,具体参考下方说明 | Array<DragItemInfo> | [] |
| width | 指标设置弹框的宽度。组件宽度，支持像素值或百分比 | String | auto |
| v-model/value | 当前选中的值 | Array<{prop:prop,color:color}>,注意颜色只能为#FD7E14, #20C997,#7367F0其中一个 | [] |
| v-model:showList | 当前显示的指标值 | Array | [] |
| isShowCompar | 是否显示对比数据 | Boolean | false |
| is-show-download | 是否显示下载按钮 | Boolean | false |
| tab-name | 当前tab名称，可选项为Performance，Landscape,需要配合showHeader以及isShowSwitch使用 | String | Performance |
| showHeader | 是否显示头部信息,包含标题以及工具栏 | Boolean | false |
| isShowSwitch | 是否显示Landscape Chart和Performance Chart切换功能 | Boolean | false |
| showAdd | 是否显示添加功能 | Boolean | true |
| isAutoFit | 是否自动填充适应宽度 | Boolean | false |
| handlerCustomColor | 自定义变化颜色,需要返回red\|gray\|green\|orange | Function({changeVal,filedName}) | -- |
| maxSelectedNum | 限制最大的选中数目 | Number | 18(Infinity 已废弃) |
| disabled | 是否禁用切换功能。是否禁用组件，禁用后无法进行交互 | Boolean | false |
| customColorArr | 自定义颜色,如果modelValue中的颜色不在该列表中,则以modelValue中配置的颜色为准 | Array | ['var(--project-orange)', '#6ADFA7', '#9B88FA'] |
| maxNum | 最大的切换个数 | Number | 3 |
| minItemWidth | 最小的每一项的宽度 | Number | 170 |
| toMarket | 当前的货币符号 | String | -- |
| showCustomMetricsDisplayListVal | 是否限制Custom Metrics弹框中展示列表的数值 | true | -- |
| hasPlan | 是否具有方案功能 | Boolean | false |
| planStyle | 方案组件样式 | Object\|Array | -- |
| planClass | 方案组件类 | Object\|Array | -- |
| defaultPlan | 默认方案配置 | Object<{planId:String,planName:String,showList:Array<String>,selectedList:Array<{prop:String,color:String}>,dataList:Array<dragDataList>}> | -- |
| planList | 方案列表 | Array<{planId:String,planName:String,showList:Array<String>,dataList:Array<dragDataList>}> | -- |
| beforeTogglePlan | 切换方案前置钩子 | ({ planInfo })=>planInfo | -- |
| applyValidate | 应用前时候的验证 | ({ close:Function(isClose),newValues }):Promise<Boolean> | -- |
| label | 显示的名称 | String | -- |
| value | 显示的当前值 | String\|Number | -- |
| valueTip | 显示的当前值提示信息,为空则使用value | String\|Array<String> | -- |
| id | 唯一键 | String\|Number | -- |
| prop | 对应数据源中键 | String | -- |
| comparVal | 显示的对比值 | Number | -- |
| comparValTip | 显示对比值提示信息,为空则使用comparVal | String\|Array<String> | -- |
| changeVal | 显示的变化值 | Number | -- |
| changeValTip | 显示对比值提示信息,为空则使用changeVal | String\|Array<String> | -- |
| changeOriginVal | 变化原始值 | Number | -- |
| groupName | 分组名称 | String | -- |
| tip | 该指标的提示信息 | String | -- |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| change | 当前选中项改变的事件,参数Array<{prop:prop,color:color}> | val,目前的选中值 |
| update:show-list | 当前显示项改变,参数Array | val,目前显示的列表 |
| togglePlan | 切换方案事件,Function(planInfo) | -- |
| ('save', '保持方案,Function(planInfo,reslove:(isSuccess,{planId,msg:string})=>{})', 'planInfo(保持的方案), resolve(是否成功的回调)') | -- | -- |
| delete | 删除方案,Function(planInfo) | planInfo(保持的方案) |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| aside  | 节点中右边内容的占位符 | -- |
| customMetricsAside  | Custom Metrics弹窗的辅助信息 | -- |

