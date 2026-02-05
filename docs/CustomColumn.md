---
component: CustomColumn
category: other
tags: [CustomColumn]
aliases: [CustomColumn]
version: 1.0.0
description: "PacuveCustomColumn组件基础用法"
---

# CustomColumn 组件文档

> PacuveCustomColumn组件基础用法

## 使用示例

### 可以改变column当前的显示以及调整column顺序。

```vue
<template>



      <el-row class="mb-4">
        <PacvueCustomColumns
          v-model:visible="visible"
          :tableColumns="columns"
          :propConfig="propConfig"
          v-model:loading="loading"
          ref="customColumn"
          v-model="defaultVal"
          :action-config="actionConfig"
          :isShowGuide="false"
          :mutualExclusionValitator="mutualExclusionValitator"
          :sortable="sortable"
          :mode="'new'"
          :customPlanList="customPlanList"
          :customPlanPosition="1"
          :planIdSortList="planIdSortList"
          :customPlanIdSortList="customPlanIdSortList"
          :planDragEnd="handleDragEnd"
          :customPlanDragEnd="handleCustomDragEnd"
          v-model:checkedPlanId="checkedPlanId"
          :sortGroupList="sortGroupList"
          :maxCustomFixedCount="5"
          enableCustomFixed
          v-model:customFixedSortList="customFixedVals"
          :fetchCustomCols="fetchCustomCols"
          :fetchCustomColReqId="1"
          :columnGroupConfig="columnGroupConfig"
        ></PacvueCustomColumns>
        <!-- {{ defaultVal }}
        <div style="padding-top: 15px">
          <pacvue-button @click="visible = true">修改sortable22</pacvue-button>
         <PacvueCustomColumnTrigger @click="visible = true"></PacvueCustomColumnTrigger>
        </div> -->
      </el-row>
   
</template>

<script setup>
import { ref, reactive } from 'vue'
var customColumn = ref(null)

const customFixedVals = ref(['isPacing'])
const fetchCustomCols = () => {
  return new Promise((resolve) => {
    let customMetrics = []
    for (let i = 0; i < 5; i++) {
      let customCol = {
        dataIndex: 'customCol_' + i,
        data: 'customCol_' + i,
        className: 'tab-number-right',
        align: 'right',
        title: 'customCol_' + i,
        columnType: 'Custom Mertics',
        groupTip: '这是一个自定义的group',
        withColEdit: true
      }
      customMetrics.push(customCol)
    }
    //resolve(customMetrics)
    setTimeout(() => {
      resolve(customMetrics)
    }, 3000)
  })
}
const columnGroupConfig = {
  //groupName:Object
  'Custom Mertics': {
    //是否该分组允许为空的时候也显示
    allowEmpty: true,
    //数据为空的显示文本
    emptyText: 'Create Custom Metric',
    onEmptyClick() {
      console.error('>>>>>>>>>>123123onEmptyClick')
    },
    //数据为空时候样式配置
    emptyStyle: {
      color: 'orange'
    },
    //是否有View List功能
    hasViewList: true,
    //viewTip: 'View List',//View List的tip信息
    onViewClick() {
      console.error('>>>>>>>>>>123123onViewClick')
    },
    //View List的样式配置a
    viewListStyle: {},
    //该分组下面的项编辑功能回调,需要配合column配置中的withColEdit设置为true使用
    onEditClick(_item) {
      debugger
    },
    showGroup: true, //是否一直显示分组信息,其中All分组的时候会一直显示
    groupTip: '这是一个tip22222', //分组的tip信息优先级高
    groupLabel: 'Custom Metrics'
  }
}
const sortGroupList = ['Dimension', 'Dimension2']
const visible = ref(false)
var loading = ref(false)
var sortable = ref(true)
//设置的值
var defaultVal = ref(['CampaignType', 'Tag1', 'CampaignTag:Tag4', 'CampaignName', 'Status', 'ASINTag:Tag1'])
defaultVal.value = ['ASINTag:Tag1', 'TimeColumn', 'ProfileName', 'CampaignType', 'Status', 'isPacing', 'CampaignId', 'ASINTag:Tag2', 'CampaignTag:Tag1', 'CTR', 'Action', 'customCol_4']
var latestPLan = localStorage.getItem('__lastest-plan__')
if (latestPLan) {
  defaultVal.value = JSON.parse(latestPLan)
}

var save = (params, resolve) => {
  var testPlanStr = localStorage.getItem('test_plan')
  var testPlanList = []
  if (testPlanStr) {
    testPlanList = JSON.parse(testPlanStr)
  }
  setTimeout(function () {
    testPlanList.push(params)
    localStorage.setItem('test_plan', JSON.stringify(testPlanList))
    resolve()
  }, 2000)
}
var apply = ({ columnNames, columnDatas, columns }) => {
  debugger
  visible.value = false
  console.log('>>>>>', columnNames, columnDatas, columns)
  localStorage.setItem('__lastest-plan__', JSON.stringify(columnDatas))
}
var setDefault = (params, resolve) => {
  console.log('>>>>>>params', params)
  resolve(true)
}
var deleteFn = (params, resolve) => {
  console.log('>>>>>>>>>params', params)
  resolve()
}
var update = (params, resolve) => {
  console.log('>>>>>>params', params)
  setTimeout(resolve, 2000)
}
var loadPlan = (resolve) => {
  var detail = [
    { id: 'isPacing', name: 'Budget Pacing' },
    { id: 'CTR', name: 'CTR', customFixed: 'left' },
    { id: 'Impression', name: 'Impr.', customFixed: 'left' },
    { id: 'budgetMode', name: 'Budget Level' },
    { id: 'MonthlyBudget', name: 'Monthly Budget' },
    { id: 'isControl', name: 'Stop Over-spend' },
    { id: 'Click', name: 'Clk.' },
    { id: 'Spend', name: 'Spend' },
    { id: 'CPC', name: 'CPC' },
    { id: 'Conversion', name: 'Orders' },
    { id: 'SaleUnits', name: 'Sale Units', customFixed: 'left' },
    { id: 'CPA', name: 'CPA' },
    { id: 'CVR', name: 'CVR' },
    { id: 'Sales', name: 'Sales' },
    { id: 'ACOS', name: 'ACOS' },
    { id: 'ROAS', name: 'ROAS' }
  ]
  var detail2 = [
    { id: 'Clk', name: 'Clk', customFixed: 'left' },
    { id: 'isPacing', name: 'Budget Pacing' }
  ]
  // detail = [
  //   { id: 'isPacing', name: 'Budget Pacing' },
  //   { id: 'Clk', name: 'Clk' }
  // ]
  var testPlanList = [
    {
      id: 14,
      userId: 93,
      productLine: 'amazon',
      menu: 'Profile',
      planName: 'Profile_zc_test1',
      isShareToAllUsers: false,
      detail: JSON.stringify(detail2),
      createTime: '2022-02-28T01:39:30',
      updateTime: '2022-02-28T01:39:30',
      isDefault: true
    },
    {
      id: 15,
      userId: 93,
      productLine: 'amazon',
      menu: 'Profile',
      planName: 'test21312',
      isShareToAllUsers: false,
      detail: JSON.stringify(detail),
      createTime: '2022-02-28T01:39:30',
      updateTime: '2022-02-28T01:39:30',
      isDefault: false
    },
    {
      // 自动化测试用例，勿删
      id: 16,
      userId: 93,
      productLine: 'amazon',
      menu: 'Profile',
      planName: 'autoTest',
      isShareToAllUsers: false,
      detail: JSON.stringify(detail2),
      createTime: '2022-02-28T01:39:30',
      updateTime: '2022-02-28T01:39:30',
      isDefault: true
    }
  ]
  resolve(testPlanList)
}
var actionConfig = ref({
  save, //保持
  apply, //应用
  setDefault, //设置默认
  delete: deleteFn, //删除
  update, //更新
  loadPlan //获取
})
var propConfig = ref({
  id: 'data',
  label: 'title',
  children: 'children',
  type: 'columnType'
})
var columns = ref([])
setTimeout(() => {
  columns.value = [
    {
      data: 'TimeColumn',
      title: 'Time',
      Type: 'basic',
      columnType: 'Dimension',
      groupTip: 'Test1232',
      tip: 'test1231',
      isRequire: true,
      isDefaultCheck: true,
      isCheck: false,
      fixed: true
    },
    {
      data: 'ProfileName',
      title: 'ProfileName',
      Type: 'basic',
      columnType: 'Dimension',
      isDefaultCheck: true,
      isCheck: false,
      fixed: true
    },
    {
      data: 'SaleUnitsTest',
      title: 'SaleUnitsTest1',
      Type: 'basic',
      columnType: 'Dimension',
      isCheck: false,
      tip: 'Apply different bids by placement by entering a percentage increase to your base bid for 3 placements: top of search (first page), rest of search, and product pages.',
      maxTipWidth: '400px',
      configurable: false
    },
    { data: 'SaleUnitsTest2', title: 'SaleUnitsTest2', Type: 'basic', columnType: 'Dimension', isCheck: false },
    {
      data: 'isPacing',
      title: 'isPacing',
      Type: 'basic',
      columnType: 'Dimension',
      isCheck: false,
      tip: '测试Tip',
      enableCustomFixed: false, //是否可以固定
      hasEdit: true,
      customParentNode: {
        data: 'PlacementBidAdjustment',
        title: 'Placement Bid Adjustment',
        tip: 'Apply different bids by placement by entering a percentage increase to your base bid for 3 placements: top of search (first page), rest of search, and product pages.',
        hasEdit: true
      }
    },
    {
      data: 'Impr',
      title: 'Impr.',
      title2: 'test2',
      Type: 'basic',
      columnType: 'Dimension',
      isCheck: false,
      customParentNode: {
        data: 'PlacementBidAdjustment',
        title: 'Placement Bid Adjustment',
        tip: 'Apply different bids by placement by entering a percentage increase to your base bid for 3 placements: top of search (first page), rest of search, and product pages.',
        hasEdit: true
      }
    },
    {
      data: 'Clk',
      title: 'Clk.',
      Type: 'basic',
      columnType: 'Dimension',
      isCheck: false,
      customParentNode: {
        data: 'PlacementBidAdjustment',
        title: 'Placement Bid Adjustment',
        tip: 'Apply different bids by placement by entering a percentage increase to your base bid for 3 placements: top of search (first page), rest of search, and product pages.',
        hasEdit: true
      }
    },
    { data: 'CTR', title: 'CTR.', Type: 'basic', columnType: 'Dimension', isCheck: false, configurable: false },
    {
      data: 'PortfolioName',
      title: `Portfolio Name`,
      Type: 'basic',
      columnType: 'Dimension',
      groupTip: 'Test 234239999',
      isDefaultCheck: true,
      isCheck: false,
      titleText: 'Portfolio Name'
    },
    { data: 'SaleUnits', title: 'SaleUnits', Type: 'basic', columnType: 'Dimension', isRequire: true, isCheck: false },
    { data: 'CampaignId', title: 'CampaignId', Type: 'basic', columnType: 'Dimension', isCheck: false },
    { data: 'CampaignTag2', title: 'Campaign Tag', Type: 'basic', columnType: 'Dimension', isCheck: false },
    { data: 'CampaignTag3', title: 'dimensionAutoTest', Type: 'basic', columnType: 'Dimension', isCheck: false },
    {
      data: 'CampaignSubTag',
      title: 'Campaign Tag & Sub Tag',
      Type: 'basic',
      columnType: 'Dimension2',
      isCheck: false
    },
    { data: 'CampaignType', title: 'CampaignType', Type: 'basic', columnType: 'Dimension2', isCheck: false },
    {
      data: 'CostType',
      title: 'SD CostType',
      oldName: 'Campaign CostType',
      Type: 'basic',
      columnType: 'Dimension2',
      isCheck: false
    },
    { data: 'biddingStrategy', title: 'Bidding Strategy', Type: 'basic', columnType: 'Dimension2', isCheck: false },
    { data: 'Status', title: 'Status', Type: 'basic', columnType: 'Dimension2', isDefaultCheck: true, isCheck: false },
    { data: 'Status1', title: 'dimension2AutoTest', Type: 'basic', columnType: 'Dimension2', isDefaultCheck: true, isCheck: false },
    // {
    //   data: 'CampaignTag',
    //   title: 'Campaign Tag',
    //   Type: 'basic',
    //   columnType: 'Dimension2',
    //   isDefaultCheck: true,
    //   isCheck: false,
    //   isIndeterminate: false,
    //   children: [
    //     { data: 'Tag1', title: 'Tag 1' },
    //     { data: 'Tag2', title: 'Tag 2' },
    //     { data: 'Tag3', title: 'Tag 3' },
    //     { data: 'Tag4', title: 'Tag 4' }
    //   ]
    // },
    // {
    //   data: 'ASINTag',
    //   title: 'ASIN Tag',
    //   Type: 'basic',
    //   columnType: 'Dimension2',
    //   isDefaultCheck: true,
    //   isCheck: false,
    //   isIndeterminate: false,
    //   children: [
    //     { data: 'Tag1', title: 'ASIN Tag 1' },
    //     { data: 'Tag2', title: 'Tag 2' },
    //     { data: 'Tag3', title: 'Tag 3' },
    //     { data: 'Tag4', title: 'Tag 4' }
    //   ]
    // },
    {
      data: 'AsinTag',
      title: 'Asin Tag',
      Type: 'basic',
      columnType: 'Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3',
      isDefaultCheck: true,
      isCheck: false,
      isIndeterminate: false,
      enableCustomFixed: false, //是否可以固定
      children: [
        { data: 'test-sub', title: 'test-sub', enableCustomFixed: true },
        { data: 'test-sub2', title: 'test-sub2' }
      ]
    },
    {
      data: 'AsinTag1',
      title: 'dimension3DAutoTest',
      Type: 'basic',
      columnType: 'Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3Dimension3',
      isCheck: false
    },
    { data: 'Action', title: 'Action', Type: 'basic', columnType: 'Dimension2', isCheck: false, fixed: 'right' }
  ]
}, 2000)
//配置互斥规则
var mutualExclusionValitator = (datax) => {
  if (datax == 'AsinTag' || datax == 'ASINTag') {
    return ['CampaignTag']
  } else if (datax == 'CampaignTag') {
    return ['AsinTag', 'ASINTag']
  }
}
var customPlanList = ref([
  {
    planName: 'custom test 1',
    id: 'custom1',
    columns: [
      { id: 'isPacing', name: 'Budget Pacing' },
      { id: 'Clk', name: 'Clk' }
    ]
  },
  {
    planName: 'custom test 2',
    id: 'custom2',
    columns: [{ id: 'Clk', name: 'Clk' }]
  }
])
const planIdSortList = ref([])
const customPlanIdSortList = ref([])
const handleDragEnd = ({ sortIdList, sortInfo }) => {
  console.warn('>>>>handleDragEnd', sortIdList, sortInfo)
}
const handleCustomDragEnd = ({ sortIdList, sortInfo }) => {
  console.warn('>>>>handleCustomDragEnd', sortIdList, sortInfo)
}
const checkedPlanId = ref('Default2222')



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
| v-model/value | 当前选中的值 | Array | [] |
| v-model:visible | 是否显示 | Boolean | false |
| table-columns | 显示的columns,见下表配置 | Array<{ fixed:'left'\|'right',columnType:String(分类类型)}> | [] |
| prop-config | 配置选项,具体看下表propsConfig  | Object | {id: 'prop',label: 'label',children: 'children',type: 'typeName'} |
| action-config | 请求操作配置,见下表配置,其中值Function参数params, resolve:Function(isSuccess), | {save:Function,apply:Function,setDefault:Function,delete:Function,loadPlan:Function} | { save:null,//保持,apply:null,//应用,setDefault:null,//设置默认delete:null,//删除loadPlan:null//获取} |
| v-model:loading | 是否显示loading | Boolean | false |
| mutualExclusionValitator | 配置column中字段的互斥,需要返回需要互斥的prop数组 | Function(data) | [] |
| defaultDataxs | 配置默认选中项,主要是为了Metrics时，与table中的column列显示的列统一,注意：重置的时候还是会根据column中isDefault字段来判断 | Array<datax> | [] |
| sortable | 是否支持column中排序功能 | Boolean | true |
| dialogHeight | 弹窗中body的高度,最大为65vh | String | 65vh |
| hasPlan | 是否具有方案功能 | Boolean | true |
| filterable | 是否具有column过滤功能。是否支持筛选/搜索功能 | Boolean | true |
| mode | 模式，值为default(之前的模式)或new（新版本的） | String | new |
| columnIconSize | 触发图标的大小 | Number | 24 |
| columnIconColor | 触发图标的颜色 | String | -- |
| customPlanList | 自定义方法列表 | Array<{planName:String,id:String\|Number,columns:Array<{id:String\|Number,name:String}>}> | -- |
| customPlanPosition | 自定义方法列表的位置,默认值为-1放在自定列表的最后 | Number | -1 |
| customPlanFormat | 自定义方格式化方法 | Function({planId,columns}) | -- |
| isDefaultByPerference | 默认方案中特有指标如ACOS,targetACOS,TACOS,clickACOS是否按照偏好来 | Boolean | false |
| perference | 偏好,值为ACOS或ROAS | String | ACOS |
| ignorePlanList | 添加自定义方法忽略列表 | Array | -- |
| isPlanDrag | 方案是否可以拖动 | Boolean | false |
| planIdSortList | 方案的id排序列表 | Array | -- |
| planDragEnd | 方案拖动结束回调 | Function({ sortIdList, sortInfo }) | -- |
| isCustomPlanDrag | 自定义方案是否可以拖动 | Boolean | false |
| customPlanIdSortList | 自定义方案的id排序列表 | Array | -- |
| customPlanDragEnd | 自定义方案拖动结束回调 | Function({ sortIdList, sortInfo }) | -- |
| v-model:checkedPlanId | 当前选中的方案id | String\|Number | -- |
| isMatchActivePlanBySortable | 选中方案的匹配规则是否按照column顺序来 | Boolean | true |
| sortGroupList | column分组的顺序列表 | Array | [] |
| maxCustomFixedCount | 最大自定义固定列数 | Number | 5 |
| enableCustomFixed | 是否开启自定义固定列功能 | Boolean | false |
| v-model:customFixedSortList | 自定义固定列排序列表 | Array | [] |
| fetchCustomCols | 获取异步自定义列表 | Function<Promise<Array>> | -- |
| fetchCustomColReqId | 获取异步自定义列表的请求id,用于区分请求 | String\|Number | -- |
| columnGroupConfig | 列分组配置项,具体看下表ColumnGroupConfig | Object<{groupName:ColumnGroupConfig}> | {} |
| isShowColIconGuide | 是否显示Custom Metrics新手引导 | Boolean | false |
| isShowFixedCol | 是否显示默认固定列 | Boolean | false |
| columnConfig | 列配置项 | Object<{Key:{isVisible:Boolean,label:String}}> | {} |
| groupWrapWidth | 列分组容器宽度 | String | 201px |
| disableCallback | 禁用回调 | Function | (nodeInfo) => false |
| id | 当前column的取的属性值 | String | data |
| label | 当前column显示的名称 | String | title |
| children | 当前column的子列表children属性名称 | String | children |
| columnType | 当前column的分类名称 | String | -- |
| fixed | 固定列,可选项left,right | String | -- |
| ignore | 忽略的列 | Boolean | -- |
| configurable | 是否该项可以操作 | Boolean | true |
| tip | 当前column的tip | String | -- |
| groupTip | 分组tip | String | -- |
| isDefaultCheck | 是否是默认项 | Boolean | false |
| maxTipWidth | 当前column的tip的最大宽度 | String | 250px |
| customParentNode | 存在父级的信息配置,同column配置基本雷同 | Object<{label:String,id:String,tip:String}> | -- |
| enableCustomFixed | 是否可以自定义固定列 | Boolean | true |
| sortable | 是否可以拖动排序 | Boolean | true |
| isShowFixedCol | 是否展示该固定列到column的选中列表中,需要注意的是这个受prop属性isShowFixedCol限制 | Boolean | true |
| id | 指定节点id为节点对象的某个属性值 | String | prop |
| label | 指定节点标签为节点对象的某个属性值 | String | label |
| children | 指定子树为节点对象的某个属性值 | String | children |
| type | 指定节点分组的属性值。组件类型或模式 | String | typeName |
| save | 保持方案,参数params, resolve | Function | null |
| apply | 应用方案,参数params, resolve | Function | null |
| setDefault | 设置default,参数params, resolve | Function | null |
| delete | 删除方案,参数params, resolve | Function | null |
| loadPlan | 加载方案,参数params, resolve | Function | null |
| toggle-plan | 切换方案的回调 | Function(planInfo) | null |
| asyncCustomColStateChange | 异步自定义列加载状态变化事件 | Function({state:loading\|loaded,customCols:Array}) | null |
| id | 当前column的取的属性值 | String | data |
| label | 当前column显示的名称 | String | title |
| children | 当前column的子列表children属性名称 | String | children |
| columnType | 当前column的分类名称 | String | -- |
| fixed | 固定列,可选项left,right | String | -- |
| ignore | 忽略的列 | Boolean | -- |
| configurable | 是否该项可以操作 | Boolean | true |
| tip | 当前column的tip | String | -- |
| groupTip | 分组tip | String | -- |
| isDefaultCheck | 是否是默认项 | Boolean | false |
| maxTipWidth | 当前column的tip的最大宽度 | String | 250px |
| customParentNode | 存在父级的信息配置,同column配置基本雷同 | Object<{label:String,id:String,tip:String}> | -- |
| enableCustomFixed | 是否可以自定义固定列 | Boolean | true |
| sortable | 是否可以拖动排序 | Boolean | true |
| isShowFixedCol | 是否展示该固定列到column的选中列表中,需要注意的是这个受prop属性isShowFixedCol限制 | Boolean | true |
| allowEmpty | 是否该分组允许为空的时候也显示 | Boolean | false |
| emptyText | 数据为空的显示文本 | String | -- |
| onEmptyClick | 数据为空时的点击事件回调 | Function | null |
| emptyStyle | 数据为空时的样式配置 | Object | {} |
| hasViewList | 是否有View List功能 | Boolean | false |
| viewTip | View List的提示信息 | String | -- |
| onViewClick | View List的点击事件回调 | Function | null |
| viewListStyle | View List的样式配置 | Object | {} |
| onEditClick | 编辑功能回调,需要配合column配置中的withColEdit设置为true使用 | Function(item) | null |
| showGroup | 是否一直显示分组信息,其中All分组的时候会一直显示 | Boolean | true |
| groupTip | 分组的tip信息优先级高于title,当title不显示时起作用 | String | -- |
| groupLabel | 分组显示的名称 | String | -- |
| parentGroupLabel | 父分组显示名称 | String | -- |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| groupAppend | 分组最后一项后面内容的插槽,slotScop为{groupName: String} | -- |
| footer-center | 弹窗中footer中间位置的插槽 | -- |

