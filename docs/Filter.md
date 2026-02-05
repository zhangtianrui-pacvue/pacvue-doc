---
component: Filter
category: filter
tags: [筛选, 过滤, 搜索]
aliases: [Filter, 筛选]
version: 1.0.0
description: "基础用法"
---

# Filter 组件文档

> 基础用法

**分类**: filter | **标签**: 筛选、过滤、搜索

## 使用示例

### Filter基础简单用法。

```vue
<template>
  <el-row class="mb-4">
    <PacvueFilter
      ref="coms"
      :shareAll="true"
      :tabs="tabSimpleList"
      v-model:tabName="tabName"
      :streamline="streamline"
      @update:query="updateSimpleQuery"
      @profile-change="profileChange"
      @attrwindow-change="attrwindowChange"
      @apply="Apply"
    ></PacvueFilter>
  </el-row>
</template>

<script setup>
  import FilterTest from './FilterTest.vue'
  import { getSimpleTabList } from './filter-util'
  import { ref, defineComponent, unref, nextTick, reactive } from 'vue'
  var tabName = ref('Default')
  var streamline = ref(false)
  var tabSimpleList = reactive(getSimpleTabList())
  //定义方法
  var getCurrentTabInfo = () => {
    return unref(tabList).find((item) => {
      return item.value == tabName.value
    })
  }
  var updateQuery = (query, tabCode) => {
    //更新查询条件 Query
    if (tabCode == tabName.value) {
      var tabInfo = getCurrentTabInfo()
      tabInfo.query = query
      //需要手动更新lastSearchPlan
      //this.updateLastSearchPlan();
    }
  }
  var profileChange = (value, key, valueKeyMap) => {
    console.log('>>>>>>profileChange', value, key, valueKeyMap)
  }
  var attrwindowChange = (x, y) => {
    //报错，需要处理
    // this.filter[2].itemList.postClick.push({
    //   value: 'test',
    //   label: 'test'
    // })
  }
  var Apply = (v, index) => {
    console.log(v, index, 2333)
  }
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### Filter基础复杂用法。

```vue
<template>
  <el-row class="mb-4">
    <PacvueFilter
      ref="coms"
      :shareAll="true"
      :tabs="tabList"
      v-model:tabName="tabName"
      :streamline="streamline"
      @update:query="updateQuery"
      @profile-change="profileChange"
      @attrwindow-change="attrwindowChange"
      @apply="Apply"
      @active-plan="activePlanMethod"
      @save-name="saveName"
      @save-plan="savePlan"
      @delete-plan="deletePlan"
      :isshare-fun="shareFun"
    >
      <template v-slot:suffix>
        <div>自定义后缀</div>
      </template>
    </PacvueFilter>
  </el-row>
</template>

<script setup>
  import FilterTest from './FilterTest.vue'
  import getTabList from './filter-util'
  import { ref, defineComponent, unref, nextTick, reactive } from 'vue'
  var tabName = ref('Keyword')
  var streamline = ref(false)
  var tabList = reactive(getTabList())
  //定义方法
  var getCurrentTabInfo = () => {
    return unref(tabList).find((item) => {
      return item.value == tabName.value
    })
  }
  var updateQuery = (query, tabCode) => {
    //更新查询条件 Query
    if (tabCode == tabName.value) {
      var tabInfo = getCurrentTabInfo()
      tabInfo.query = query
      //需要手动更新lastSearchPlan
      //this.updateLastSearchPlan();
    }
  }
  var profileChange = (value, key, valueKeyMap) => {
    console.log('>>>>>>profileChange', value, key, valueKeyMap)
  }
  var attrwindowChange = (x, y) => {
    //报错，需要处理
    // this.filter[2].itemList.postClick.push({
    //   value: 'test',
    //   label: 'test'
    // })
  }
  var Apply = (v, index) => {
    console.log(v, index, 2333)
    if (typeof index != 'object') {
      //apply操作
      var tabInfo = getCurrentTabInfo()
      tabInfo.planList.forEach((item) => {
        if (item.id === index) {
          console.log(JSON.stringify(v))
          item.valueKeyMap = v
        }
      })
      tabInfo.activePlan = index
    } else {
      //查询操作
    }
    nextTick(() => {
      if (index != 'lastsearch') {
        updateLastSearchPlan(v)
      }
      //设置sortBy
      var tabInfo = unref(tabList).find((item) => {
        return item.value == tabName.value
      })
      var filterList = tabInfo.filter || []
      var sortByInfo = filterList.find((item) => {
        return item.key == 'pacvue-sort-by'
      })
      sortByInfo.itemList = []
    })
  }
  var updateLastSearchPlan = (lastQuery) => {
    //更新last search plan
    var tabInfo = getCurrentTabInfo()
    var planList = tabInfo.planList || []
    var lastSearchPlan = planList.find(function (item) {
      return item.id == 'lastsearch'
    })
    if (lastSearchPlan) {
      lastSearchPlan.valueKeyMap = tabInfo.query
    }
  }
  var activePlanMethod = (v) => {
    var tabInfo = getCurrentTabInfo()
    tabInfo.activePlan = v
  }
  //保持名称
  var saveName = (val) => {
    console.log('save-name', val)
  }
  // 保存时触发
  var savePlan = (data) => {
    console.log('save-plan', data)
  }
  // 删除计划
  var deletePlan = (data) => {
    console.log(data)
  }

  var shareFun = () => {
    return false
  }
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### Filter 类型参数详解。

```vue
//**********************filter item type如下********************//
//****mul-select（多选select），
//****mul - select - tree（多选框的tree，如果是tag，需要配置isTag: true,）,
//****Cascader - select - noRelation(有两个单选select框放在一起，但没有级联关系，postClick第一个select,postView后一个select)
//*****input （前面带有search图标的搜索框）
//****searchKeyword-dropdown (中间带有relationship,input输入框) =>下拉框+输入框*/
//*** groupinput-dropdown-textarea (中间带有relationship,input输入框) =>下拉框+textarea*/
//*** groupinput-dropdown-range (范围输入框min-max,unit是单位)*/
//****groupinput-dropdown-range-eq (范围输入框>=<某一个值)=>单选下拉框+输入框+后缀（unitType）*/
//****time 日期选择器， format: "yyyy-MM-dd",
//****cascader 单选级联下拉框，单选（普通的级联）
//****pacvue-cascader 分类多选级联下拉框,并且显示分类选中数目
//****pacvue-sort-by 单选排序级联 ，需要配置maxLength: 3,maxNum: 0, showZero: true

//****multiple-filter 两个form item组合形态
//****radio-group 单选框组
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| v-model:tabName | 当前的激活tab名称 | String | Default |
| shareAll | 是否显示共享 | Boolean | false |
| tabs | tab列表Array<label: String,value: String,query: {},filter:Array,activePlan: String,groupSort: Array,planList: Array>,具体信息如TabItem表 | Boolean | [] |
| label | tab显示的名称 | String | -- |
| value | tab的具体值 | String | -- |
| query | 当前filter的值,以filter的配置中key的字段为属性名称，选中值为属性值 | Object | -- |
| filter | filer配置列表，具体参考filterInfo信息列表 | Array<FilterInfo> | -- |
| activePlan | 当前激活的plan的id | String\|Number | -- |
| planList | 保持的plan方案列表，Array<{planName:String,id:String\|Number,valueKeyMap:Object}> | Array | -- |
| type | filter类型，为简单类型simple以及complex | String | complex |
| key | 对应传递参数中的key值 | String | -- |
| value | 指对应传递参数中的属性值 | String | -- |
| label | 对应当前filter显示的值 | String | -- |
| type | filter的form 类型。组件类型或模式 | String | -- |
| group | 分类名称 | String | -- |
| cascader | 级联关系的key值列表 | Array | -- |
| ForceCascader | 强制级联，在配置的cascader对应的字段中配置，note：cascader中配置的选项key必须存在该filter项 | Boolean | false |
| emitChangeName | filter改变事件名称 | String | -- |
| mapKeys | 列表数据对应的props配置, | Array<[label,value,children]> | -- |
| itemList | 列表数据 | Array | [] |
| placeholder | filter的placeholder。占位提示文字，在无输入时显示 | String\|Object | -- |
| isTag | 是否显示为Tag模式 | Boolean | false |
| showCascaderFn | 控制显示的级联,返回Array<{key:String,visible:Boolean}> | Function(value) | -- |
| formatRender | 对filter的值进行格式化 | Function(value) | -- |
| advFilter | 对filter显示配置弹框中，设置条件进行配置该字段是否可显示 | Function(query) | -- |
| RelationshipKey | Relationship对应的参数名称 | String | -- |
| RelationshipTip | Relationship对应的提示 | String | -- |
| RelationshipItem | Relationship对应的下拉数据 | Array | -- |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| apply | 应用的回调,注意：必须在其中更新lastSearchPlan方案,为参数为v,index,其中v为当前的filter应用信息，index为对象为查询操作,否则为Apply操作 | Function(v, index) |
| active-plan | 激活方案的回调 | Function(planId) |
| save-name | 修改名称 | Function(planInfo) |
| save-plan | 保持方案 | Function(planInfo) |
| delete-plan | 删除方案 | Function(planInfo) |
| update:query | 更新form值的回调(newQuery,tabCode) | Function(query,tabCode) |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| suffix | filter展示后缀 | -- |

