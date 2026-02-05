---
component: NewFilter2
category: filter
tags: [新筛选器V2, 高级筛选]
aliases: [NewFilter2]
version: 1.0.0
description: "基础用法"
---

# NewFilter2 组件文档

> 基础用法

**分类**: filter | **标签**: 新筛选器V2、高级筛选

## 使用示例

### Filter基础简单用法。

```vue
<template>
  <el-row class="mb-4">
    <PacvueNewFilter ref="coms" v-model="query" type="simple" @search="search" :filter="tabSimpleList[0].filter"
      @filter-change="filterChange"></PacvueNewFilter>
  </el-row>
</template>

<script setup>
  import FilterTest from './FilterTest.vue'
  import { ref, defineComponent, unref, nextTick, reactive } from 'vue'
  var tabSimpleList = reactive(getBaseFilter())
  var query = reactive({
    campaignNameV1: 'or2',
    profile: [],
    profileKey: 'Or',
    adgroupName: [],
    adgroupOperand: 'and',
    openDate: ['2024-10-15', '2024-11-13'],
    campaignName: [],
    campaignNameOperand: 'and',
    adgroupIds: [],
    ROAS: [],
    'radio-group': '',
    GroupByCascader: ['campaign', 'ytd'],
    selecttree: [],
    treeKey2: '1',
    attrwindow: { postClick: [], postView: '' },
    'checkbox-group': [],
    'groupinput-dropdown-range': [],
    'pacvue-cascader': [],
    'pacvue-sort-by': [{ value: 'BudgetLevel22', sort: 'desc' }]
  })
  var filterChange = ({ key, value, relationship }) => {
    if (key == 'asins' || key == 'multiple-filter') {
      console.log('>>>>>>>>>filter-change', key, value, relationship)
    }
  }
  var search = (query) => {
    console.log(query)
  }

  /** 模拟数据生成函数 */
  function getBaseFilter() {
    var tabs = ['Default']
    return tabs.map((tabName) => {
      var groupSort = [
        {
          name: 'Base'
        },
        {
          name: 'Attr'
        },
        {
          name: 'group',
          tips: 'You can choose from different types to get the performance range quickly.',
          adv: [
            {
              icon: 'pacvue-icon-tubiao',
              tips: 'High performance',
              template: {
                'groupinput-dropdown': 'ss',
                'groupinput-dropdown-textarea': [],
                'groupinput-dropdown-range': ['312', 123],
                'groupinput-dropdown-range-eq': ['<', 1],
                RelationshipKeyaa: 'Or'
              }
            },
            {
              icon: 'pacvue-icon-a-Creativeinsight',
              tips: 'test2',
              template: {
                'groupinput-dropdown-textarea': [123555, 233555],
                'groupinput-dropdown-range': ['312', 1211113],
                'groupinput-dropdown-range-eq': ['<', 1]
              }
            }
          ]
        }
      ]
      var planList = [
        {
          planName: 'Default',
          id: 'Default',
          valueKeyMap: {
            profile: ['id0', 'id1', 'test2313'],
            campaignIds: [],
            'groupinput-dropdown-range': [],
            //group: "test",
            // attrwindow: {
            //   postClick: "0",
            //   postView: "0"
            // },
            states: ['All_but_Archived', 'enabled', 'paused'],
            'groupinput-dropdown': '1111', //不支持Array
            'groupinput-dropdown-textarea': [],
            //  "groupinput-dropdown-range": ["312", 1],
            'groupinput-dropdown-range-eq': ['<', 4],
            areaprofileKey: 'ls',
            'selecttree-nomarl': ['0child-id0'],
            'editor-input': '测试数据'
          }
        }
        // {
        //   planName: 'Last Search',
        //   id: 'lastsearch',
        //   valueKeyMap: {
        //     profile: ['id0', 'id1', 'test2313'],
        //     'groupinput-dropdown-range': [],
        //     //group: "test",
        //     // attrwindow: {
        //     //   postClick: "0",
        //     //   postView: "0"
        //     // },
        //     campaignIds: [],
        //     states: ['All_but_Archived', 'enabled', 'paused'],
        //     'groupinput-dropdown': '1111', //不支持Array
        //     'groupinput-dropdown-textarea': [],
        //     //  "groupinput-dropdown-range": ["312", 1],
        //     'groupinput-dropdown-range-eq': ['<', 4],
        //     areaprofileKey: 'ls',
        //     'selecttree-nomarl': ['0child-id0']
        //     //
        //   }
        // }
      ]
      return {
        label: tabName,
        value: tabName,
        query: {
          campaignNameV1: 'or2',
          profile: [],
          profileKey: 'Or',
          adgroupName: [],
          adgroupOperand: 'and',
          openDate: ['2024-10-15', '2024-11-13'],
          campaignName: [],
          campaignNameOperand: 'and',
          adgroupIds: [],
          ROAS: [],
          'radio-group': '',
          GroupByCascader: ['campaign', 'ytd'],
          selecttree: [],
          treeKey2: '1',
          attrwindow: { postClick: [], postView: '' },
          'checkbox-group': [],
          'groupinput-dropdown-range': [],
          'pacvue-cascader': [],
          'pacvue-sort-by': [{ value: 'BudgetLevel22', sort: 'desc' }]
        },
        filter: congfigFilter.profile,
        activePlan: 'Default', //当前PlanId
        groupSort: groupSort,
        planList: planList,
        type: 'simple',
        getAsyncData: {
          campaignTagIds() {
            return new Promise((resolve) => {
              resolve(CampaignTagList)
            })
          }
        }
      }
    })
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
    <PacvueNewFilter
      ref="coms"
      :tabs="tabList"
      :share-all="true"
      v-model:tabName="tabName"
      @filter-change="filterChange"
      @search="search"
      @save-name="saveName"
      @save-plan="savePlan"
      @delete-plan="deletePlan"
      :isshare-fun="shareFun"
    >
      <template v-slot:suffix>
        <div>自定义后缀</div>
      </template>
    </PacvueNewFilter>
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
  var filterChange = ({ key, value, relationship }) => {
    if (key == 'asins' || key == 'multiple-filter') {
      console.log('>>>>>>>>>filter-change', key, value, relationship)
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
| v-model | 当前显示的filter数据。双向绑定值，用于获取和设置组件的当前值 | Array<{key:value}> | {} |
| filter | filter的配置Array<FilterInfo> | Array<FilterInfo> | {} |
| type | Filter类型,可选complex，simple,简单模式需要设置为simple | String | complex |
| clearable | 是否有清空按钮。是否显示清除按钮，点击可清空当前值 | Boolean | true |
| v-model:tabName | 当前的激活tab名称 | String | Default |
| shareAll | 是否显示共享 | Boolean | false |
| tabs | tab列表Array<label: String,value: String,query: {},filter:Array,activePlan: String,groupSort: Array,planList: Array, getAsyncData:{Key:function({formData})}>,具体信息如TabItem表 | Boolean | [] |
| label | tab显示的名称 | String | -- |
| value | tab的具体值 | String | -- |
| query | 当前filter的值,以filter的配置中key的字段为属性名称，选中值为属性值 | Object | -- |
| filter | filer配置列表，具体参考filterInfo信息列表 | Array<FilterInfo> | -- |
| activePlan | 当前激活的plan的id | String\|Number | -- |
| planList | 保持的plan方案列表，Array<{planName:String,id:String\|Number,valueKeyMap:Object}> | Array | -- |
| shareAll | 是否显示共享 | Boolean | false |
| type | filter类型，为简单类型simple以及complex | String | complex |
| getAsyncData | 获取异步数据的配置 | {key:Function({formData})} | -- |
| key | 对应传递参数中的key值 | String | -- |
| value | 指对应传递参数中的属性值 | String | -- |
| label | 对应当前filter显示的值 | String | -- |
| type | filter的form 类型。组件类型或模式 | String | -- |
| group | 分类名称 | String | -- |
| cascader(已废弃) | 级联关系的key值列表 | Array | -- |
| ForceCascader(已废弃) | 强制级联，在配置的cascader对应的字段中配置，note：cascader中配置的选项key必须存在该filter项 | Boolean | false |
| mapKeys | 列表数据对应的props配置, | Array<[label,value,children]> | -- |
| itemList | 列表数据 | Array | [] |
| placeholder | filter的placeholder。占位提示文字，在无输入时显示 | String\|Object | -- |
| isTag | 是否显示为Tag模式 | Boolean | false |
| showCascaderFn | 控制显示的级联,返回Array<{key:String,visible:Boolean}> | Function(value) | -- |
| formatRender | 对filter的值进行格式化 | Function(value) | -- |
| advFilter(已废弃) | 对filter显示配置弹框中，设置条件进行配置该字段是否可显示 | Function(query) | -- |
| RelationshipKey | Relationship对应的参数名称 | String | -- |
| RelationshipTip | Relationship对应的提示 | String | -- |
| RelationshipItem | Relationship对应的下拉数据 | Array | -- |
| isWidthMultiple | 是否宽度占两个 | Boolean | false |

## 方法 Methods

组件暴露的方法，可通过 ref 调用。

| 方法名 | 说明 | 参数 |
| --- | --- | --- |
| clear | 清空数据 | -- |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| filter-change | filter的change回调，参数为Object<{key, value, relationship,emitChangeName,fromOrigin, updateFilterInfo: (filterKey, options) => {}>,注意如果是complex的类型，更新filter请用updateFilterInfo | Function(query) |
| search | 查询的回调，参数为query | Function(query) |
| save-name | 修改名称 | Function(planInfo) |
| save-plan | 保持方案 | Function(planInfo) |
| delete-plan | 删除方案 | Function(planInfo) |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| suffix | filter展示后缀 | -- |

