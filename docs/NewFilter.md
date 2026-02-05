---
component: NewFilter
category: filter
tags: [新筛选器, 高级筛选, 过滤]
aliases: [NewFilter, 筛选器]
version: 1.0.0
description: "基础用法"
---

# NewFilter 组件文档

> 基础用法

**分类**: filter | **标签**: 新筛选器、高级筛选、过滤

## 使用示例

### Filter基础简单用法。

```vue
<template>
  <PacvueNewFilter v-if="true" ref="coms" v-model="simpleQuery" type="simple" @search="handleSearch" :filter="simpleFilterConfig" @filter-change="simpleFilterChange"></PacvueNewFilter>
</template>
<script setup>
import { ref} from 'vue'
import filterConfigList from './filter-config'
//生成 filter配置信息
const createFilterConfig = () => {
  let filterConfig = []
  const filterInitValue = {}
  for (const key in filterConfigList) {
    let filterConfigValue = filterConfigList[key]
    filterConfig = filterConfig.concat(filterConfigValue)
    if (Array.isArray(filterConfigValue)) {
      filterConfigValue.map((item) => {
        filterInitValue[item.key] = item.value
      })
    } else if (typeof filterConfigValue === 'object') {
      filterInitValue[filterConfigValue.key] = filterConfigValue.value
    }
  }
  return {
    filters:filterConfig,
    filterInitValue
  }
}
const { filters: filterConfig, filterInitValue } = createFilterConfig()
const { query: simpleQuery, filters: simpleFilterConfig, filterChange: simpleFilterChange, handleSearch, searchQuery } = useSimpleModeFilterConfig()
function useSimpleModeFilterConfig() {
  const searchQuery = ref({})
  let handleSearch = (query) => {
    searchQuery.value = query
  }
  let simpleQuery = ref(filterInitValue)
  return {
    query: simpleQuery, //表单的值
    filters: filterConfig, //Filter配置列表
    filterChange({ key, value, eventKey, relationship, emitChangeName, updateFilterInfo }) {
      console.log('>>>>>>>>>filter-change', key, value, eventKey, relationship, emitChangeName)
      if (key == 'multiple-filter') {
        var dateType = 'date'
        var format = 'YYYY-MM-DD'
        if (value.postClick == 7) {
          dateType = 'week'
        } else if (value.postClick == 14) {
          dateType = 'month'
          format = 'YYYY-MMM'
        } else if (value.postClick == 30) {
          dateType = 'year'
          format = 'YYYY'
        }
        updateFilterInfo('multiple-filter', {
          extraOption: {
            postClick: {
              type: 'single'
            },
            postView: {
              type: 'time',
              dateType: dateType,
              format: format, //'MMM,YYYY'
              valueFormat: format, //'yyyy-MM-dd'
              disabledDate(date) {
                console.log('>>>>>>>>>disabledDate', date)
                return false
              }
            }
          }
        })
        console.log('>>>>>>>>>filter-change222', key, value, relationship, emitChangeName)
      } else if (key == 'multiple-filter-3') {
        updateFilterInfo('multiple-filter-3', {
          placeholder: {
            postClick: 'please select ',
            postView: 'please select ' + value.postClick
          }
        })
      } else if (key == 'asins' || key == 'multiple-filter' || key == 'profile') {
        console.log('>>>>>>>>>filter-change', key, value, relationship, emitChangeName)
      }
    },
    handleSearch,
    searchQuery
  }
}
</script>
```

### Filter基础复杂用法。

```vue
<template>
  <PacvueNewFilter
    ref="comsComplex"
    :tabs="complexTabList"
    :share-all="true"
    :divideNum="3"
    v-model:tabName="activeTabCode"
    @filter-change="handleFilterChange"
    @search="handleSearchMultiple"
    @save-name="saveName"
    @save-plan="savePlan"
    @delete-plan="deletePlan"
    :isshare-fun="shareFun"
   >
  </PacvueNewFilter>
</template>
<script setup>
import { ref, unref } from 'vue'
import filterConfigList,{ initDataFilterSelect } from './filter-config'
//生成 filter配置信息
const createFilterConfig = () => {
  let filterConfig = []
  const filterInitValue = {}
  for (const key in filterConfigList) {
    let filterConfigValue = filterConfigList[key]
    filterConfig = filterConfig.concat(filterConfigValue)
    if (Array.isArray(filterConfigValue)) {
      filterConfigValue.map((item) => {
        filterInitValue[item.key] = item.value
      })
    } else if (typeof filterConfigValue === 'object') {
      filterInitValue[filterConfigValue.key] = filterConfigValue.value
    }
  }
  return {
    filters:filterConfig,
    filterInitValue
  }
}
const { filters: filterConfig, filterInitValue } = createFilterConfig()
const {
  tabList: multipleTabList,
  activeTabCode,
  handleFilterChange,
  handleSearch: handleSearchMultiple,
  searchQuery: searchQueryMultiple,
  saveName,
  savePlan,
  deletePlan
} = useMultipleModeFilterConfig()
function getTabList() {
  var tabs = ['Keyword', 'PAT', 'RealTime']
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
          profile: [1],
          campaignIds: [2],
          ACOS: [],
          CampaignBox: {
            campaignState: 'test-23',
            campaignIds: []
          }
        }
      },
      {
        planName: 'plan 2',
        id: 1,
        isShareToAll: true,
        valueKeyMap: {
          profile: ['test1'],
          profileKey: 'Or',
          campaignTagIds: [],
          campaignName: [],
          campaignNameOperand: 'or'
        }
      },
      {
        planName: 'Last Search',
        id: 'lastsearch',
        valueKeyMap: {
          profile: ['test1'],
          campaignIds: [],
          states: ['All_but_Archived', 'enabled', 'paused'],
          'groupinput-dropdown': '1111', //不支持Array
          'groupinput-dropdown-textarea': [],
          //  "groupinput-dropdown-range": ["312", 1],
          'groupinput-dropdown-range-eq': ['<', 4],
          areaprofileKey: 'ls',
          'selecttree-nomarl': ['0child-id0'],
          //
          campaignName: [],
          campaignNameOperand: 1,
          profileKey: 'Or',
          campaignTagIds: [],
          isAnd: '0',
          isSearchNG: {
            checked: false,
            value: 1
          },
          CampaignTypeItems: [],
          GroupByCascader: ['campaign', 'ytd'],
          asins: [],
          asinsOperand: 'LikeOr',
          servingStatus: [],
          startDate: '',
          SortBy: [{ sort: 'desc', value: 'Spend' }],
          selecttree: [],
          treeKey2: '1',
          attrwindow: { postClick: [], postView: '' },
          group: 'test',
          groupinput: '',
          profileKeyaa: 'Or',
          time: 'yyyy-01-Sa',
          cascader: [],
          'pacvue-cascader': [],
          'pacvue-sort-by': [{ sort: 'desc', value: 'Spend' }],
          radio: false,
          ACOS: Array[0],
          nonbid: { checked: false, value: '' }
        }
      }
    ]
    // 快捷键功能配置
    var avgROAS = undefined
    var avgClick = undefined
    var avgCTR = undefined
    var quickPlanList = [
      {
        icon: 'PacvueIconCompetitorAnalysis', //'pacvue-icon-a-highperformance',
        tips: 'Highest Performers',
        template: {
          Impression: ['1000', undefined],
          ROAS: [0, avgROAS]
        }
      },
      {
        icon: 'PacvueIconWastedAdSpendReduceBids', //'pacvue-icon-a-WastedAdSpend',
        tips: 'Wasted Ad Spend',
        template: {
          Click: [10, undefined],
          Conversion: [0, 0]
        }
      },
      {
        icon: 'PacvueIconIncreaseReach', //'pacvue-icon-a-IncreaseReach',
        tips: 'Increase Reach',
        template: {
          Click: [0, 5],
          Impression: [0, 1000]
        }
      },
      {
        icon: 'PacvueIconIncreaseBids', //'pacvue-icon-a-IncreaseBids',
        tips: 'Increase Bids',
        template: {
          Click: [0, avgClick],
          ROAS: [avgROAS, undefined]
        }
      },
      {
        icon: 'PacvueIconReduceBids', //'pacvue-icon-a-ReduceBids',
        tips: 'Reduce Bids',
        template: {
          Impression: [0, 1000],
          CTR: [avgCTR, undefined],
          ROAS: [0, avgROAS]
        }
      }
    ]
    var innerPlanList = [
      {
        planName: 'Best-Selling Best-Selling Best-Selling Best-Selling Best-Selling', //名称
        //id: 'Best-Selling_isVirtual',
        icon: 'PacvueIconCompetitorAnalysis', //'pacvue-icon-a-highperformance',
        tips: 'Highest Performers',
        valueKeyMap: {
          profile: [1],
          //campaignIds: [2],
          ACOS: [],
          CampaignBox: {
            campaignState: 'test-23',
            campaignIds: []
          }
        }
      },
      {
        planName: 'Show-Selling', //名称
        //id: 'Best-Selling_isVirtual',
        icon: 'PacvueIconCompetitorAnalysis', //'pacvue-icon-a-highperformance',
        tips: 'Highest Performers',
        valueKeyMap: {
          profile: [1],
          //campaignIds: [2],
          ACOS: [],
          CampaignBox: {
            campaignState: 'test-23',
            campaignIds: []
          }
        }
      }
    ]
    return {
      label: tabName,
      value: tabName,
      isRealTime: tabName == 'RealTime', //是否是Real Time
      query: { ...filterInitValue },
      filter: filterConfig,
      activePlan: 'lastsearch', //当前激活的plan
      groupSort: groupSort,
      planList: planList, //方案列表
      quickPlanList: quickPlanList, //快捷键功能
      innerPlanList: innerPlanList, //内置方法功能
      type: 'complex', //Filter 组件的类型为simple Or complex
      hasPlan: true, //是否具有plan功能
      canEdit: true, //是否具有编辑功能
      visibilityCallBack({ filterInfo } = {}) {
        //Filter是否显示的配置
        if (filterInfo.key == 'profile') {
          return false
        }
      },
      filterDisableCallback({ filterKey, filterVal, formData }) {
        console.log('>>>>>>>>>filterDisableCallback', filterKey, filterVal, formData)
        return true
      },
      getAsyncPlanSortList({ tabCode }) {
        console.log('>>>>>>>>>getAsyncPlanSortList', tabCode)
        //获取方案的id排序列表
        return new Promise((resolve) => {
          setTimeout(() => {
            resolve([1, 'Best-Selling Best-Selling Best-Selling Best-Selling Best-Selling_isVirtual', 'Show-Selling_isVirtual', 2])
          }, 2000)
        })
      },
      planDragEnd({ sortIdList, sortInfo }, tabInfo) {
        console.log('>>>>>>>>>planDragEnd', sortIdList, sortInfo, tabInfo)
        //方案拖拽排序后的回调
      },
      getAsyncData: {
        //获取异步数据的配置{Key:Function<Promise>}
          //获取异步数据的配置{Key:Function<Promise>}
        Store: () => {
          return new Promise((resolve) => {
            setTimeout(() => {
              resolve([
                { name: 'Store-1', id: 'Store-1' },
                { name: 'Store-2', id: 'Store-2' }
              ])
            }, 2000)
          })
        },
        filterSelect: initDataFilterSelect
        
      }
    }
  })
}
function useMultipleModeFilterConfig() {
  let activeTabCode = ref('Keyword')
  const searchQuery = ref({})
  let handleFilterChange = ({ key, value, relationship, fromOrign, updateFilterInfo, eventKey } = {}) => {
    console.log('>>>>>>>>>filterInfo', key, value, relationship, fromOrign, updateFilterInfo, eventKey)
  }
  let tabList = getTabList()
  let handleSearch = (query) => {
    searchQuery.value = query
  }
  //定义方法
  var getCurrentTabInfo = () => {
    return unref(tabList).find((item) => {
      return item.value == activeTabCode.value
    })
  }
  //保持名称
  var saveName = (planInfo) => {
    console.log('save-name', planInfo)
    var tabInfo = getCurrentTabInfo()
    var planList = tabInfo.planList
    var planInfo2 = planList.find((planItem) => {
      return planItem.id == planInfo.id
    })
    planInfo2.planName = planInfo.name
  }
  // 保存时触发
  var savePlan = (data) => {
    let tabInfo = getCurrentTabInfo()
    console.log('save-plan', data)
    if (tabInfo) {
      let newPlan = {
        planName: data.planName,
        id: data.id,
        valueKeyMap: data.SearchModel,
        isShareToAll: data.isShare
      }
      let planList = tabInfo.planList
      planList.splice(1, 0, newPlan)
    }
  }
  // 删除计划
  var deletePlan = (planInfo) => {
    console.log(planInfo)
    var tabInfo = getCurrentTabInfo()
    var planList = tabInfo.planList
    var planIndex = planList.findIndex((planItem) => {
      return planItem.id == planInfo.id
    })
    planList.splice(planIndex, 1)
    //更新planList
  }
  return {
    tabList,
    activeTabCode,
    handleFilterChange,
    searchQuery,
    handleSearch,
    //操作的回调
    saveName,
    savePlan,
    deletePlan
  }
}
var shareFun = () => {
  return false
}
</script>
```

### Filter filter-config.js详细配置。

```vue
import { defineComponent, h, markRaw } from 'vue'
import { dayjs } from '@pacvue/element-plus'
import info from '@/assets/info.svg'
// 单选Select
const singleSelect = [
  {
    key: 'Store', // 筛选框的唯一值
    label: 'Store', // 筛选框的label
    value: '', // 筛选框的默认值
    type: 'single-select', // 筛选框的类型
    group: 'PacvueSelect', // 筛选框的分组名称
    isValRecusion: false, //是否必选
    mapKeys: ['name', 'id', 'children'], // 筛选框的值的映射key
    itemList: [
      // 筛选框的选项列表
      {
        name: 'test',
        id: 'test'
      },
      {
        name: 'test-2',
        id: 'test-2'
      }
    ]
  }
]
// 多选Select
const mulSelect = [
  {
    // 筛选框的基础配置
    key: 'profile', // 筛选框的唯一值
    value: [], // 筛选框的默认值
    label: 'Profile', // 筛选框的label
    type: 'mul-select', // 筛选框的类型
    group: 'PacvueSelect', // 筛选框的分组名称
    mapKeys: ['name', 'id', 'children'], // 筛选框的选项列表的映射字段key配置
    isWidthMultiple: false, // 宽度是否占有两列的宽度，默认是false
    isRequire: false, //是否必选
    itemList: [
      // 筛选框的选项列表
      {
        name: 'test-1',
        id: 1,
        children: [
          {
            name: 'test-233',
            id: 88,
            children: [
              { name: 'test-888', id: 888 },
              { name: 'autoTest1', id: 'autoTest1' },
              { name: 'test-889', id: 889 },
              { name: 'test-887', id: 887 }
            ]
          }
        ]
      },
      { name: 'test-2', id: 2 }
    ],
    // 筛选框的埋点配置
    dataCy: 'auto_component_00206', // 筛选框的埋点data-cy
    dataCyValue: 'auto_component_00207', // 筛选框的埋点data-cy-value
    dataCyFilter: 'auto_component_00208', // 筛选框的埋点data-cy-filter
    relationshipDataCy: 'auto_component_00209', // 筛选框的埋点data-cy-relationship
    // 筛选框的额外配置
    RelationshipKey: 'profileKey', // 筛选框的关联key
    RelationshipTip: 'RelationshipTip:xxxxxxxxxxxxxxx', // 筛选框的关联提示
    RelationshipItem: [
      {
        name: 'Or',
        id: 'Or'
      },
      {
        name: 'And',
        id: 'And'
      },
      {
        name: 'Not',
        id: 'Not'
      }
    ],
    // 筛选框的高级配置
    extraOption: {
      //minLimit: 1, // 筛选框的最小限制
      clearable: true, // 筛选框的清空按钮
      isCascaderRecusion: true // 筛选框的级联配置
    },
    isVisibleRequired: false, //是否必须显示
    forceDefault: false, //是否强制默认显示
    isFirstExcute: false, //是否首次触发
    isFeadToday: false, //是否是feadToday
    placeholder: 'please select', // 筛选框的placeholder
    // 筛选框的插槽配置
    optionRender: markRaw(
      // 筛选框的选项渲染
      defineComponent({
        props: ['id', 'label', 'level', 'source'],
        render() {
          return h('div', [this.label, h('img', { src: info })])
        }
      })
    ),
    selectLabelRender: markRaw(
      // 筛选框的选项标签渲染
      defineComponent({
        props: ['selectSize', 'totalSize', 'titleList', 'itemList', 'parentName'],
        render() {
          return h('div', [this.parentName, '>', this.titleList?.[0]])
          // return h('div', [this.titleList, h('img', { src: info })])
        }
      })
    ),
    emptyRender: markRaw(
      // 筛选框的空状态渲染
      defineComponent({
        props: [],
        render() {
          return h('div', ['这是个定义的empty', h('img', { src: info })])
        }
      })
    )
  },
  {
    key: 'adgroupIds', //筛选框的唯一值
    value: [], //筛选框的默认值
    label: 'Adgroup', //筛选框的label
    type: 'mul-select', //筛选框的类型
    group: 'PacvueSelect', // 筛选框的分组名称
    isCascaderRecusion: true, //是否保持原有值，并且回流操作
    mapKeys: ['Name', 'Id'], //筛选框的选项列表的映射字段key配置
    placeholder: 'Select All', //筛选框的placeholder
    //筛选框的选项列表
    itemList: [
      {
        Id: 1,
        Name: 'test12332_1'
      },
      {
        Id: 2,
        Name: 'test12332_2'
      },
      {
        Id: 'autoTest2',
        Name: 'autoTest2'
      },
      {
        Id: 3,
        Name: 'test12332_3'
      }
    ],
    //筛选框的埋点配置
    dataCy: 'auto_component_00213',
    dataCyValue: 'auto_component_00214', //筛选框选中值埋点
    dataCyFilter: 'auto_component_00215', //下拉框中过滤框埋点
    emitChangeName: 'adgroup-change' //筛选框的emitChangeName
  }
]
// 复杂输入框
const complexInput = [
  {
    key: 'complexInput', // 对应数据库的key
    value: '', // 筛选框的默认值
    label: 'Complex Input', // 筛选框的label
    type: 'complexInput', //筛选框的类型,可选值为complexInput,dropdown-input-textarea,input,editor-input,dropdown-input,dropdown-input-range-eq
    group: 'Input', // 筛选框的分组名称
    unitType: '%', // 筛选框的单位类型
    placeholder: 'Complex Input', // 筛选框的placeholder
    mapKeys: ['name', 'id'], // 筛选框的选项列表的映射字段key配置
    // 筛选框的关联配置
    RelationshipKey: 'complexInputRelationship', // 筛选框的关联key
    RelationshipItem: [
      {
        name: '=',
        id: '='
      },
      {
        name: '>',
        id: '>'
      },
      {
        name: '<',
        id: '<'
      }
    ],
    // 筛选框的高级配置
    selectLabelTemplate: 'Keywords input', // 筛选框的选项标签模板
    textareaPlaceholder: 'One Keyword per line', // 筛选框的textarea placeholder
    inputStyle: {}, // 筛选框的input样式
    labelStyle: {}, // 筛选框的label样式
    rowSplitRule: ({ itemVal } = {}) => {
      //行拆分规则
      return itemVal.split(/[；;,，]/)
    }
  },
  {
    key: 'asins', // 筛选框的唯一值
    value: [], // 筛选框的默认值
    label: 'ASIN', // 筛选框的label
    type: 'dropdown-input-textarea', // 筛选框的类型
    group: 'Input', // 筛选框的分组名称
    inputTag: 'ASINs input', // 筛选框的input标签
    mapKeys: ['name', 'id'], // 筛选框的值的映射key
    placeholder: 'Input ASINs', // 筛选框的placeholder
    // 筛选框的关联配置
    RelationshipKey: 'asinsOperand', // 筛选框的关联key
    RelationshipTip: '', // 筛选框的关联提示
    RelationshipItem: [
      {
        id: 'LikeOr',
        name: 'Contains(or)'
      },
      {
        id: 'Like',
        name: 'Contains(and)'
      }
    ]
  },
  {
    key: 'adgroupName', //筛选框的唯一值
    value: [], // 筛选框的默认值
    label: 'AdGroup Name', // 筛选框的label
    type: 'dropdown-input-textarea', //筛选框的类型
    group: 'Input', // 筛选框的分组名称
    groupTip: 'Test', //筛选框的groupTip
    cascader: [], //筛选框的级联数据
    emitChangeName: '', //筛选框的emitChangeName
    isWidthMultiple: true, //是否占用两倍宽度
    mapKeys: ['name', 'id'], //筛选框的选项列表的映射字段key配置
    selectLabelTemplate: 'Adgroups input', //筛选框的选项标签模板
    textareaPlaceholder: 'One Adgroup per line', //筛选框的textarea placeholder
    placeholder: 'Input AdGroup Name', //筛选框的placeholder
    //筛选框的额外配置
    extraOption: {
      createSelectLabelStyle({ value: _value } = {}) {
        return { color: 'red' }
      },
      createItemStyle({ item }) {
        let id = item.tagId
        if (id == '1|0') {
          return {
            color: 'red'
          }
        }
      }
    },
    //筛选框的关联配置
    RelationshipKey: 'adgroupOperand', //筛选框的关联key
    relationshipDataCy: 'auto_component_00202', //筛选框的关联埋点data-cy
    RelationshipItem: [
      //筛选框的关联选项列表
      {
        id: 'and',
        name: 'And'
      },
      {
        id: 'or',
        name: 'Or'
      },
      {
        id: 'contain',
        name: 'Contain'
      }
    ]
  }
]
// 输入范围筛选框
const inputRange = [
  {
    key: 'inputRange', // 筛选框的唯一值
    value: [], //筛选框的默认值
    label: 'searchKeyword-dropdown-range', // 筛选框的label
    type: 'dropdown-input-range', // 筛选框的类型
    group: 'Input', // 筛选框的分组名称
    isWidthMultiple: true, //是否占用两倍宽度
    unit: 'day', // 筛选框的单位
    labelTip: 'Label Tip', // 筛选框的label提示
    extraOption: {
      inputType: 'number', // 筛选框的input类型 number|int(整数)
      digitCount: 2, // 筛选框的数字位数
      //inputRenderMode: 'Component', // 筛选框的input渲染模式 Native(原生)|Component(组件)
      showInputOverflowTip: true // 筛选框的input溢出提示
    },
    mapKeys: ['name', 'id'], // 筛选框的值的映射key
    // 筛选框的关联配置
    RelationshipKey: `inputRangeOperand`, // 筛选框的关联key
    RelationshipTip: '', // 筛选框的关联提示
    RelationshipItem: [
      // 筛选框的关联选项列表
      {
        id: 'is',
        name: 'Is'
      },
      {
        id: 'not',
        name: 'Not'
      }
    ]
    // 筛选框的高级配置
    //   dataCy: 'auto_component_00222', // 筛选框的埋点data-cy
    //   validation({ value = [], relationshipVal } = {}) {
    //     // 筛选框的验证配置
    //     if (relationshipVal == 'not') {
    //       if (value.length < 2 || value.some((item) => item === undefined || item === '')) return 'error'
    //     }
    //   }
  },
  {
    key: 'ROAS', //筛选框的唯一值
    value: [], //筛选框的默认值
    label: 'ROAS', //筛选框的label
    type: 'dropdown-input-range', //筛选框的类型
    group: 'Input', //筛选框的分组名称
    unit: '%', //筛选框的单位
    labelTip: '这是个测试tip', //筛选框的label提示信息
    dataCy: 'auto_component_00225', //筛选框的埋点data-cy
    mapKeys: ['name', 'id'], //筛选框的选项列表的映射字段key配置
    //筛选框的关联配置
    RelationshipKey: `ROASOperand`, //筛选框的关联key
    RelationshipItem: [
      {
        id: 'is',
        name: 'Is'
      },
      {
        id: 'not',
        name: 'Not'
      }
    ],
    //筛选框的验证配置
    validation({ value = [], relationshipVal, query: _formData } = {}) {
      //需要添加min以及max的大小验证规则
      var min = value[0]
      var max = value[1]
      if (min !== '' && min !== undefined && max !== '' && max !== undefined) {
        if (parseFloat(min) > parseFloat(max)) {
          return {
            state: 'error',
            msg: 'The minimum value cannot be greater than the maximum value.'
          }
        }
      }
      if (relationshipVal == 'not') {
        var valueMap = {}
        for (var i = 0; i < 2; i++) {
          var item = value[i]
          var keyName = 'hasValue'
          if (item === undefined || item === '') {
            keyName = 'emptyValue'
          }
          if (!valueMap[keyName]) {
            valueMap[keyName] = []
          }
          valueMap[keyName].push({
            index: i,
            value,
            filedKey: i == 0 ? 'min' : 'max'
          })
        }
        if (valueMap.emptyValue?.length == 1) {
          var emptyInfo = valueMap.emptyValue[0]
          return {
            state: 'error',
            msg: emptyInfo.filedKey == 'min' ? 'Please enter the minimum value' : 'Please enter the maximum value'
          }
        }
      }
    }
  }
]
// Tag 筛选框
const mulSelectTree = [
  {
    key: 'campaignTagIds', // 对应数据库的key
    value: [], // 筛选框的默认值
    label: 'Campaign Tag', // 筛选框的label
    isTag: true, // 筛选框是否为tag类型
    addTagLabel: 'Add Tag', // 筛选框的添加标签label
    type: 'mul-select-tree', // 筛选框的类型
    isDefault: true, // 筛选框的默认值
    group: 'PacvueSelect', // 筛选框的分组名称
    isWidthMultiple: true, // 筛选框的宽度是否占用两列
    mapKeys: ['tagName', 'tagId', 'subTags'], // select select-tree select-cascader都需要配置这个属性
    itemList: [], // 筛选框的选项列表
    placeholder: 'Plase Select', // 筛选框的placeholder
    // 筛选框的关联配置
    RelationshipKey: 'isAnd', // 筛选框的关联key
    RelationshipExtraOption: { dropdownWidth: '500px' }, // 筛选框的关联配置
    //筛选框关联tip
    RelationshipTip:
      'Check "Or" to see the union of the campaigns in selected tags or subtags. Check "And" to see the intersection of the campaigns in selected tags.Check "Not" to see the other campaigns not in selected tags. If multiple subtags are selected,it will intersect the union of the subtags under same tag.',
    RelationshipItem: [
      // 筛选框的关联选项列表
      {
        tagName: 'Or',
        tagId: '0'
      },
      {
        tagName: 'And',
        tagId: '1'
      }
    ]
  },
  {
    key: 'selecttree', //筛选框的唯一值
    value: [], //筛选框的默认值
    label: 'selecttree', //筛选框的label
    type: 'mul-select-tree', //筛选框的类型
    group: 'PacvueSelect', //筛选框的分组名称
    cascader: [], //筛选框的级联数据
    mapKeys: ['Name', 'Id', 'Child'], //筛选框的选项列表的映射字段key配置
    itemList: [
      //筛选框的选项列表
      {
        Name: 'test',
        Id: 'test',
        Child: [
          {
            Name: 'all active BR campaigns =所有活跃的BR运动= dsfsffv df dffsdf afdssfqwaadadqwq eqwe qq qeqwsdfdsf',
            Id: 'child1'
          },
          {
            Name: 'child2',
            Id: 'child2'
          },
          {
            Name: 'child3',
            Id: 'child3'
          },
          {
            Name: 'child4',
            Id: 'child4'
          },
          {
            Name: 'child5',
            Id: 'child5'
          },
          {
            Name: 'child6',
            Id: 'child6'
          }
        ]
      },
      {
        Name: 'test2',
        Id: 'test2'
      },
      {
        Name: 'test3',
        Id: 'test3'
      },
      {
        Name: 'test4',
        Id: -10
      }
    ],
    placeholder: 'please select', //筛选框的placeholder
    isTag: true, //筛选框是否为tag类型,对应CampaignTag筛选框
    //筛选框的埋点配置
    dataCy: 'auto_component_00218', //筛选框的埋点data-cy
    dataCyValue: 'auto_component_00228', //筛选框选中值埋点
    dataCyFilter: 'auto_component_00229', //下拉框中过滤框埋点
    //筛选框的关联配置
    RelationshipKey: 'treeKey2',
    RelationshipTip: 'RelationshipTip:xxxxxxxxxxxxxxx',
    RelationshipItem: [
      //筛选框的关联选项列表
      {
        Name: 'Or',
        Id: '1'
      },
      {
        Name: 'And',
        Id: '2'
      },
      {
        Name: 'Not',
        Id: '3'
      }
    ]
  }
]
// 级联筛选框
const cascader = [
  {
    key: 'GroupByCascader', // 筛选框的唯一值
    value: ['campaign', 'ytd'], // 筛选框的默认值
    label: 'Group By', // 筛选框的label
    type: 'cascader', // 筛选框的类型
    group: 'Cascader', // 筛选框的分组名称
    mapKeys: ['name', 'id', 'children'], // 筛选框的值的映射key
    placeholder: 'Campaign', // 筛选框的placeholder
    itemList: [
      // 筛选框的选项列表
      {
        name: 'Campaign',
        id: 'campaign',
        children: [
          {
            id: 'ytd',
            name: 'YTD'
          },
          {
            id: 'date',
            name: 'Day'
          },
          {
            id: 'week',
            name: 'Week'
          },
          {
            id: 'month',
            name: 'Month'
          },
          {
            id: 'quarter',
            name: 'Quarter'
          },
          {
            id: 'year',
            name: 'Year'
          }
        ]
      },
      {
        name: 'Placement',
        id: 'placement',
        children: [
          {
            id: 'ytd',
            name: 'YTD'
          },
          {
            id: 'date',
            name: 'Day'
          },
          {
            id: 'week',
            name: 'Week'
          },
          {
            id: 'month',
            name: 'Month'
          },
          {
            id: 'quarter',
            name: 'Quarter'
          },
          {
            id: 'year',
            name: 'Year'
          }
        ]
      },
      {
        name: 'CampaignType',
        id: 'campaigntype',
        children: [
          {
            id: 'ytd',
            name: 'YTD'
          },
          {
            id: 'date',
            name: 'Day'
          },
          {
            id: 'week',
            name: 'Week'
          },
          {
            id: 'month',
            name: 'Month'
          },
          {
            id: 'quarter',
            name: 'Quarter'
          },
          {
            id: 'year',
            name: 'Year'
          }
        ]
      }
    ],

    // 筛选框埋点配置
    dataCy: 'auto_component_00217'
  }
]
// 级联筛选框-无关系
const cascaderSelectNoRelation = [
  {
    key: 'attrwindow', // 对应数据库的key
    value: {
      postClick: [],
      postView: ''
    },
    label: 'Attr.Window',
    // type是 "Cascader-select-noRelation" 时，subType优先级更高，用于设置设置下拉框单选或多选
    subType: {
      postClick: 'multiple',
      postView: 'single'
    },
    type: 'Cascader-select-noRelation',
    group: 'Cascader',
    cascader: [],
    mapKeys: ['label', 'value'], // select select-tree select-cascader都需要配置这个属性
    itemList: {
      postClick: [
        {
          value: '2',
          label: 'Default Post-click'
        },
        {
          value: '7',
          label: '7 Days Post-click'
        },
        {
          value: '14',
          label: '14 Days Post-click'
        },
        {
          value: '30',
          label: '30 Days Post-click'
        }
      ],
      postView: [
        {
          value: '4',
          label: 'Default Post-view'
        },
        {
          value: '2',
          label: 'No Post View'
        },
        {
          value: '1',
          label: '1 Day Post-view'
        },
        {
          value: '7',
          label: '7 Days Post-view'
        },
        {
          value: '14',
          label: '14 Days Post-view'
        },
        {
          value: '30',
          label: '30 Days Post-view'
        }
      ]
    },
    placeholder: {
      postClick: 'please select',
      postView: 'please select'
    },
    // 筛选框埋点配置
    dataCy: 'auto_component_00219',
    dataCyValue: 'auto_component_00300',
    dataCyFilter: 'auto_component_00301'
  }
]
// 复杂组合筛选框
const multipleFilter = [
  {
    key: 'multiple-filter', // 筛选框的唯一值
    value: {
      postClick: '', // 筛选框的默认值
      postView: '' // 筛选框的默认值
    },
    label: 'multiple-filter', // 筛选框的label
    type: 'multiple-filter', // 筛选框的类型
    group: 'MultipleFilter', // 筛选框的分组名称
    cascader: [], // 筛选框的级联数据
    isWidthMultiple: true, // 筛选框的宽度是否占用两列
    extraOption: {
      // 筛选框子项配置
      postClick: {
        type: 'single'
      },
      postView: {
        type: 'time',
        dateType: 'daterange',
        format: 'YYYY-MM-DD', //'MMM,YYYY'
        valueFormat: 'yyyy-MM-dd',
        disabledDate(time) {
          return time.getTime() > Date.now()
        }
      }
    },
    mapKeys: ['label', 'value'], // 筛选框的值的映射key
    itemList: {
      // 筛选框子项选项列表
      postClick: [
        {
          value: '2',
          label: 'Default Post-click'
        },
        {
          value: '7',
          label: '7 Days Post-click'
        },
        {
          value: '14',
          label: '14 Days Post-click'
        },
        {
          value: '30',
          label: '30 Days Post-click'
        }
      ],
      postView: [
        {
          value: '4',
          label: 'Default Post-view'
        },
        {
          value: '2',
          label: 'No Post View'
        },
        {
          value: '1',
          label: '1 Day Post-view'
        },
        {
          value: '7',
          label: '7 Days Post-view'
        },
        {
          value: '14',
          label: '14 Days Post-view'
        },
        {
          value: '30',
          label: '30 Days Post-view'
        }
      ]
    },
    placeholder: {
      // 筛选框子项placeholder
      postClick: 'please select', // 筛选框的placeholder
      postView: 'please select' // 筛选框的placeholder
    }
  }
]
// 根据日期类型切换日期选择器筛选框
const timeGroup = [
  {
    key: 'timeGroup', // 筛选框的唯一值
    type: 'timeGroup', // 筛选框的类型
    label: 'timeGroup', // 筛选框的日期选择器label
    group: 'pacvue-radio-group', // 筛选框的分组名称
    value: {
      // 筛选框的默认值
      dateType: 'week',
      dateVal: ''
    },
    //日期类型列表配置
    dateTypeList: [
      // 筛选框的日期类型列表
      { label: 'W', value: 'week', pickerOptions: { format: 'YYYY-WW', valueFormat: 'yyyy-MM-dd' } },
      { label: 'M', value: 'month', pickerOptions: { format: 'MMM,YYYY', valueFormat: 'yyyy-MM-dd' } },
      { label: 'Q', value: 'quarter', pickerOptions: { format: 'QQ-YYYY', valueFormat: 'yyyy-MM-dd' } }
    ],
    //日期选择器配置
    placeholder: 'Select Date', //日期选择器的placeholder、
    rangeSeparator: '~', //日期选择器的范围分隔符
    startPlaceholder: 'Start Date', //日期选择器的开始日期placeholder
    endPlaceholder: 'End Date', //日期选择器的结束日期placeholder
    clearable: true, //日期选择的clear功能
    pickerOptions: {
      //日期选择器的配置
      disabledDate(time) {
        return time.getTime() > Date.now()
      }
    },
    isWidthMultiple: true // 筛选框的宽度是否占用两列
  }
]
// 日期选择器
const time = [
  {
    key: 'time', // 筛选框的唯一值
    type: 'time', // 筛选框的类型
    value: '', // 筛选框的默认值
    label: 'time2', // 筛选框的label
    timeType: 'month', // 日期类型
    group: 'PacvueFilterDate', // 筛选框的分组名称
    format: 'MMM,YYYY', // 日期选择器的显示日期格式
    valueFormat: 'yyyy-MM-dd', // 日期选择器的值的日期格式
    rangeSeparator: '~', // 日期选择器的范围分隔符
    startPlaceholder: 'Start Date', // 日期选择器如果是daterange的开始日期placeholder
    endPlaceholder: 'End Date', // 日期选择器如果是daterange的结束日期placeholder
    clearable: true, // 日期选择器的clearable
    placeholder: 'time Select', // 日期选择器的placeholder
    pickerOptions: {
      disabledDate(time) {
        return time.getTime() > Date.now()
      }
    }
  }
]
// 日期选择器-快速选择
const datepickerWithQuicks = [
  {
    key: 'openDate', // 筛选框的唯一值
    value: [dayjs().subtract(29, 'day').format('YYYY-MM-DD'), dayjs().format('YYYY-MM-DD')],
    label: 'Open Date', // 筛选框的label
    type: 'datepicker-with-quicks', // 筛选框的类型
    timeType: 'daterange', // 筛选框的日期类型
    format: 'MM/DD/YYYY', // 筛选框显示的日期格式
    valueFormat: 'YYYY-MM-DD', // 筛选框的值的日期格式
    group: 'DatePicker', // 筛选框的分组名称
    clearable: true, // 筛选框的clearable
    isWidthMultiple: true, // 筛选框的宽度是否占用两列
    // 筛选框埋点配置
    dataCy: 'auto_component_00210',
    dataCyValue: 'auto_component_00211',
    dataCyFilter: 'auto_component_00212',
    pickerOptions: {
      disabledDate(time) {
        return time.getTime() > Date.now()
      }
    }
  }
]
// 多级级联筛选框
const pacvueCascader = [
  {
    key: 'pacvue-cascader', // 筛选框的唯一值
    value: [], // 筛选框的默认值
    label: 'pacvue-cascader', // 筛选框的label
    type: 'pacvue-cascader', // 筛选框的类型
    group: 'Cascader', // 筛选框的分组名称
    cascader: [], // 筛选框的级联数据
    itemList: [
      // 筛选框的选项列表
      {
        name: 'A-Group',
        id: 'A',
        children: []
      },
      {
        name: 'B-Group',
        id: 'B',
        children: [
          {
            name: 'b1',
            id: 'b1'
          }
        ]
      },
      {
        name: 'C-Group',
        id: 'C',
        children: [
          {
            name: 'c1',
            id: 'c1'
          }
        ]
      }
    ],
    mapKeys: ['name', 'children', 'name', 'id'], // 筛选框的值的映射key
    placeholder: 'Please Select', // 筛选框的placeholder
    // 筛选框埋点配置
    dataCy: 'auto_component_00223', // 筛选框的dataCy
    dataCyValue: 'auto_component_00302', // 筛选框的dataCyValue
    dataCyFilter: 'auto_component_00303' // 筛选框的dataCyFilter
  }
]
// 排序筛选框
const pacvueSortBy = [
  {
    key: 'pacvue-sort-by', // 筛选框的唯一值
    value: [
      // 筛选框的默认值
      {
        value: 'BudgetLevel22',
        sort: 'desc'
      }
    ],
    label: 'pacvue-sort-by', // 筛选框的label
    type: 'pacvue-sort-by', // 筛选框的类型
    group: 'Cascader', // 筛选框的分组名称
    isWidthMultiple: 2, // 筛选框的宽度是否占用两列
    itemList: [
      // 筛选框的选项列表
      {
        label: 'Profile',
        value: 'profile'
      },
      {
        label: 'Budget Level',
        value: 'BudgetLevel'
      },
      {
        label: 'a',
        value: 'a'
      },
      {
        label: 'b',
        value: 'b'
      },
      {
        label: 'c',
        value: 'c'
      }
    ],
    maxLength: 3, // 筛选框的级联层级
    placeholder: 'time Select', // 筛选框的placeholder
    // 筛选框埋点配置
    dataCy: 'auto_component_00224',
    dataCyValue: 'auto_component_00304',
    dataCyFilter: 'auto_component_00305'
  }
]
// 单选Radio
const radio = [
  {
    type: 'radio', // 筛选框的类型
    key: 'radio', // 筛选框的唯一值
    value: true, // 筛选框的默认值
    label: 'radio', // 筛选框的label
    group: 'PacvueRadio' // 筛选框的分组名称
  }
]
// 单选RadioGroup
const radioGroup = [
  {
    key: 'radio-group', // 筛选框的唯一值
    value: '', // 筛选框的默认值
    label: 'radio-group', // 筛选框的label
    type: 'radio-group', // 筛选框的类型
    group: 'PacvueRadio', // 筛选框的分组名称
    isWidthMultiple: true, //是否宽度占两个
    forceDefault: false, //是否强制显示
    placeholder: 'holder 2', // 筛选框的placeholder
    dataCy: 'auto_component_00220', // 筛选框的dataCy
    mapKeys: ['name', 'id'], // 筛选框的值的映射key
    itemList: [
      // 筛选框的选项列表
      { id: 'Month', name: 'Month' },
      { id: 'Week', name: 'Week' },
      { id: 'Quarter', name: 'Quarter' }
    ]
  }
]
// 多选框组
const checkboxGroup = [
  {
    key: 'checkbox-group', // 筛选框的唯一值
    value: [], // 筛选框的默认值
    label: 'checkbox-group', // 筛选框的label
    type: 'checkbox-group', // 筛选框的类型
    group: 'Checkbox', // 筛选框的分组名称
    cascader: [], // 筛选框的级联数据
    isWidthMultiple: true, // 筛选框的宽度是否占用两列
    mapKeys: ['name', 'id'], // 筛选框的值的映射key
    itemList: [
      // 筛选框的选项列表
      { id: 'Month', name: 'Month' },
      { id: 'Week', name: 'Week' },
      { id: 'Quarter', name: 'Quarter' }
    ],
    // 筛选框埋点配置
    dataCy: 'auto_component_00221'
  }
]
// 带有勾选项的select筛选框
const radioSelect = [
  {
    key: 'nonbid', // 对应数据库的key
    value: {
      checked: false, //是否勾选
      value: '' //选中的select值
    },
    label: 'Non-bid Queries', // 筛选框的label
    type: 'radio-select', // 筛选框的类型
    group: 'PacvueRadio', // 筛选框的分组名称
    mapKeys: ['name', 'id'], // 筛选框的值的映射key配置
    itemList: [
      // 筛选框的选项列表
      {
        name: 'test',
        id: 'test'
      },
      {
        name: 'test-2',
        id: 'test-2'
      }
    ]
  }
]
// 多级级联筛选框v2
const cascaderSelectV2 = [
  {
    key: 'cascader-select-v2', // 筛选框的唯一值
    value: [], // 筛选框的默认值
    label: 'cascader-select-v2', // 筛选框的label
    type: 'cascader-select-v2', // 筛选框的类型
    group: 'Cascader', // 筛选框的分组名称
    cascader: [], // 筛选框的级联数据
    emitChangeName: 'treechange', // 筛选框的emitChangeName
    mapKeys: ['Name', 'Id', 'Child'], // 筛选框的值的映射key
    // 筛选框的选项列表
    itemList: [
      {
        Name: 'test',
        Id: 'test',
        Child: [
          {
            Name: 'all active BR campaigns =所有活跃的BR运动= dsfsffv df dffsdf afdssfqwaadadqwq eqwe qq qeqwsdfdsf',
            Id: 'child1'
          },
          {
            Name: 'child2',
            Id: 'child2'
          },
          {
            Name: 'child3',
            Id: 'child3'
          },
          {
            Name: 'child4',
            Id: 'child4'
          },
          {
            Name: 'child5',
            Id: 'child5'
          },
          {
            Name: 'child6',
            Id: 'child6'
          }
        ]
      },
      {
        Name: 'test2',
        Id: 'test2'
      },
      {
        Name: 'test3',
        Id: 'test3'
      },
      {
        Name: 'test4',
        Id: -10
      }
    ],
    placeholder: 'please select', // 筛选框的placeholder
    // 筛选框的额外配置
    extraOption: {
      useSelectData: true, // 筛选框的useSelectData
      dataCy: 'auto_component_00216', // 筛选框的dataCy
      dataCySelectLabel: 'auto_component_00217'
    },
    placeIndex: 0
  }
]
// 多级级联筛选框v3
const cascaderSelectV3 = [
  {
    key: 'cascader-select-v3', // 筛选框的唯一值
    value: [], // 筛选框的默认值
    label: 'cascader-select-v3', // 筛选框的label
    type: 'cascader-select-v3', // 筛选框的类型
    group: 'Cascader', // 筛选框的分组名称
    mapKeys: ['Name', 'Id', 'Child'], // 筛选框的值的映射key
    // 筛选框的选项列表
    itemList: [
      {
        Name: 'test',
        Id: 'test',
        hasChildren: true
      },
      {
        Name: 'test2',
        Id: 'test2'
      },
      {
        Name: 'test3',
        Id: 'test3'
      },
      {
        Name: 'test4',
        Id: -10
      }
    ],
    placeholder: 'please select', // 筛选框的placeholder
    // 筛选框的额外配置
    extraOption: {
      useSelectData: true, // 筛选框的useSelectData
      onExpand(node, next) {
        // 请求子节点数据
        var list = [
          {
            Name: 'all active BR campaigns =所有活跃的BR运动= dsfsffv df dffsdf afdssfqwaadadqwq eqwe qq qeqwsdfdsf',
            Id: 'child1'
          },
          {
            Name: 'child2',
            Id: 'child2'
          },
          {
            Name: 'child3',
            Id: 'child3'
          },
          {
            Name: 'child4',
            Id: 'child4'
          },
          {
            Name: 'child5',
            Id: 'child5'
          },
          {
            Name: 'child6',
            Id: 'child6'
          }
        ]
        next(list)
      },
      dataCy: 'auto_component_00216',
      dataCySelectLabel: 'auto_component_00217'
    },
    placeIndex: 0
  }
]
// 带有滑动懒加载的select筛选框
const scrollSize = 100
const filterSelect = [
  {
    key: 'filterSelect', // 筛选框的唯一值
    value: [], // 筛选框的默认值
    label: 'filterSelect', // 筛选框的label
    type: 'filter-select', // 筛选框的类型
    group: 'PacvueSelect', // 筛选框的分组名称
    mapKeys: ['label', 'id'], // 筛选框的值的映射key
    //必需配置
    scrollSize, // 筛选框的滚动加载条数，默认500条
    scrollTotal: 0, // 筛选框选项的总条数
    maxLimit: 2000, // 筛选框选中的的最大条数，默认2000条
    selectedNameList: [], //筛选框选中值名称列表
    extraOption: {
      isUseValNoLabel: false, //没有label的时候不要使用id作为显示值
      isDynamicH: true //是否动态高度
    },
    filterChange: loadPageData, // 筛选框过滤条件变化时触发
    scrollEnd: loadPageData, // 筛选框滚动到底部时触发
    onSelectedChange(event, { key, updateFilterInfo, eventKey }) {
      // 筛选框选中值发生变化时触发
      let value = event.value ?? []
      let firstName = event.firstName
      console.log('onSelectedChange', { key, eventKey })
      if (value.length == 1) {
        if (!firstName) {
          //模拟请求接口
          if (eventKey == 'campaignIds') {
            setTimeout(() => {
              updateFilterInfo('filterSelect', {
                selectedNameList: ['123']
              })
            }, 2000)
          }
        }
      }
    },
    // 筛选框的选项列表
    itemList: [],
    placeholder: 'Select All' // 筛选框的placeholder
  }
]
// 单选按钮组
const radioBtnGroup = [
  {
    key: 'radioGroup', // 筛选框的唯一值
    type: 'radio-btn-group', // 筛选框的类型
    group: 'PacvueRadio', // 筛选框的分组名称
    mapKeys: ['name', 'id'], // 筛选框的值的映射key
    label: '', // 筛选框的label
    itemList: [
      // 筛选框的选项列表
      {
        name: 'Top Categories',
        id: 'top',
        tip: 'Top 10 Categories by Sales'
      },
      {
        name: 'Custom',
        id: 'custom'
      }
    ]
  }
]
export default [
  singleSelect,
  mulSelect,
  complexInput,
  inputRange,
  mulSelectTree,
  cascader,
  cascaderSelectNoRelation,
  multipleFilter,
  timeGroup,
  time,
  datepickerWithQuicks,
  pacvueCascader,
  pacvueSortBy,
  radio,
  radioGroup,
  checkboxGroup,
  radioSelect,
  cascaderSelectV2,
  cascaderSelectV3,
  filterSelect,
  radioBtnGroup
]
function loadPageData({ keyword: searchKeyword, scrollInfo }, { key, eventKey, searchQuery, updateFilterInfo }) {
  console.log('loadPageData', { key, eventKey, searchQuery, updateFilterInfo })
  //eventKey为 filterChange(关键词变化) 或scrollEnd(滚动到底部)
  let pageIndex = eventKey == 'filterChange' ? 1 : scrollInfo.current
  //存储查询Keyword
  // if (eventKey == 'filterChange') {
  //   searchKeywordShadow[key] = searchKeyword
  // }
  var profileIds = searchQuery.profileIds?.length ? searchQuery.profileIds : []
  var campaignIds = searchQuery.campaignIds || []
  var adgroupIds = searchQuery.adgroupIds || []
  const pageInfo = {
    pageIndex,
    pageSize: scrollSize
  }
  let query = {
    profileIds,
    campaignIds,
    adgroupIds,
    searchKeyword: searchKeyword,
    ...(pageInfo ?? {})
  }
  if (pageInfo) {
    query.pageInfo = {
      OrderByField: 'AdId',
      OrderAsc: true,
      PageSize: pageInfo.pageSize,
      PageIndex: pageInfo.pageIndex
    }
  }
  return new Promise((resolve) => {
    if (searchKeyword) {
      setTimeout(() => {
        const list = []
        const key = searchKeyword
        for (let i = 0; i < pageInfo.pageSize; i++) {
          list.push({
            label: `filter-${key}-${i}`,
            id: `filter-${key}-${i}`
          })
        }
        resolve(list)
      }, 1000)
    } else {
      initDataFilterSelect(({ updateFilterInfo } = {})).then(resolve)
    }
  })
}
// 创建假数据
export function initDataFilterSelect({ updateFilterInfo } = {}) {
  return new Promise((resolve) => {
    setTimeout(() => {
      const list = []
      for (let i = 0; i < scrollSize; i++) {
        list.push({
          label: `nosearch-${i}`,
          id: `nosearch-${i}`
        })
      }
      if (typeof updateFilterInfo == 'function') {
        updateFilterInfo('filterSelect', {
          scrollTotal: 205 //这个要以接口返回的数据总条数为准,这里只是一个模拟值
        })
      }
      resolve(list)
    }, 1000)
  })
}
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
| isPlanDrag | 方案是否可以拖动 | Boolean | false |
| planDragEnd | 方案拖动结束回调 | Function({ sortIdList, sortInfo }) | -- |
| getAsyncPlanSortList | 获取方案的id排序列表, | Function({ tabCode }):Promise | -- |
| isSearchDisableNoChange | 是否开启查询条件没有变化时,搜索按钮禁用 | Boolean | false |
| isSearchByClear | 是否开启清空条件时,自动搜索功能 | Boolean | false |
| isInitSearch | 是否会首次查询,是为了isSearchDisableNoChange开启了组件内部初始的时候把search按钮禁用 | Boolean | false |
| label | tab显示的名称 | String | -- |
| value | tab的具体值 | String | -- |
| query | 当前filter的值,以filter的配置中key的字段为属性名称，选中值为属性值 | Object | -- |
| filter | filer配置列表，具体参考filterInfo信息列表 | Array<FilterInfo> | -- |
| activePlan | 当前激活的plan的id | String\|Number | -- |
| planList | 保持的plan方案列表，Array<{planName:String,id:String\|Number,valueKeyMap:Object}> | Array | -- |
| shareAll | 是否显示共享 | Boolean | false |
| type | filter类型，为简单类型simple以及complex | String | complex |
| canEdit | filter是否具有编辑功能 | Boolean | true |
| getAsyncData | 获取异步数据的配置 | {key:Function({formData})} | -- |
| filterVisibleCallBack | filter是否隐藏显示回调 | Function({filterKey,filterInfo},tabName) | -- |
| filterDisableCallback | filter是否禁用回调(注意：目前只支持select，input两种大类型),返回Boolean\|{disabled:Boolean,tip:String} | Function({filterKey,filterVal,filterInfo,formData,tabCode}) | -- |
| isFilterChangeBtnDisable | filter和plan 按钮是否禁用 | Boolean | false |
| isAutoTop | 查询的时候是否自动滑动顶部 | Boolean | false |
| autoScrollEl | 自动滑动顶部的元素 | Object<Dom>\|String | window |
| isAutoMergeCache | 是否把缓存中的自动合并query | Boolean | false |
| isAutoRun | 是否自动调用search方法 | Boolean | false |
| isByTabStore | 是否需要按照tab进行分别存储 | Boolean | false |
| storeKey | filter缓存存储的key值,注意：可以手动从组件中导出方法PacvueGetLastFilterQuery({ isByTabStore = true, tabCode="Default" , storeKey } )方法中获取存储query | String\|Number | -- |
| storeQueryFormat | 存储的查询条件过滤函数 | Function | -- |
| quickPlanList | 快捷方案列表，Array<{icon:String,tips:String\|Number,template:Object<{key:value}>}> | Array | -- |
| innerPlanList | 内置方案列表，Array<{icon:String,tips:String,planName:String,valueKeyMap:Object}> | Array | -- |
| clearable | 是否有清空按钮。是否显示清除按钮，点击可清空当前值 | Boolean | true |
| showSearchText | 是否显示查询按钮的文本内容 | Boolean | true |
| isFeadToday | 是否当前是realtime情况 | Boolean | false |
| isMultiFilter | 是否开启多规则匹配，为onlyFilter不显示多种类型切换(仅对mul-select或者single-select有效) | Boolean\|Boolean | false |
| hasPlan | 是否具有保持Plan功能 | Boolean | true |
| isCanHandUpdateFilters | 是否需要更新FilterSetting中的filter配置 | Boolean | false |
| isWatchChange | 是否监控每一个Filter值得变化并且显示对应的样式 | Boolean | true |
| isWatchSimple | 是否监控简单模式Filter列表的变化,默认只监控一次 | Boolean | false |
| isRecusionToChange | 组件回流匹配是否触发change事件 | Boolean | false |
| divideNum | 组件显示格局中每一行至少显示的filter个数(已废弃,请使用minFilterWidth来判断) | Number | 4 |
| minFilterWidth | 组件中显示格局中每一个filter的最小的宽度 | Number | 300 |
| isWithToggleAll | 是否有切换全部filter的问题 | Boolean | true |
| isSearchDisable | search按钮是否禁用 | Function({query,tabCode}) | -- |
| searchTip | search按钮tip | String | -- |
| searchDisabled | search按钮是否禁用 | Boolean | false |
| excludeFilters | 排除那些字段不显示,注意:如果忽略的Filter对应的表单中默认是有值的,应用方案不会覆盖该表单对应的值 | Array | [] |
| isAsyncUpdateName | 是否应用的时候异步更新方案名称,如果为真的时候需要在save-plan回调中手动调用resolve | Boolean | false |
| applyValidator | Plan Setting弹窗应用方案时候的拦截器 | Function({ planId,realPlanId,tabCode,query,internal,icon}) | -- |
| withFiltersOnlyInPlanSetting | 仅在方案配置中包含的筛选项字段列表 | Array | [] |
| excludeClearFilters | 排除清空项filter的配置 | Array | [] |
| beforePlanApply | 方案应用前的回调函数,其中planDetail为方案详情,filterKeyMap为filter的隐射,tabCode为当前激活的tab,返回的结果中isContinue为true,之前的运行逻辑,如果为false,则只抛出apply-plan事件;toTabCode以及toQuery是改变指定tab的表单值 | Function({planDetail:Object,filterKeyMap:Object,tabCode:String}):{ isContinue:Boolean, toQuery:Object, toTabCode:String} | Function |
| customSearchStyle | 自定义的search按钮样式 | Object | -- |
| isSearchDisableNoChange | 是否开启查询条件没有变化时,搜索按钮禁用 | Boolean | false |
| isSearchByClear | 是否开启清空条件时,自动搜索功能 | Boolean | false |
| isInitSearch | 是否会首次查询,是为了isSearchDisableNoChange开启了组件内部把search按钮禁用 | Boolean | false |
| isResetWithAutoSearchDisable | 当搜索禁用自动解封时,是否重置状态 | Boolean | true |
| includeExtraQuery | 查询条件是否变化的额外参数 | Object | -- |
| prefixCustomFilter | 前置自定义filter的配置,需要配合custom-filter-[key]插槽使用,SlotScop为{filterInfo, modelValue, updateModelValue, change} | Array<{key:String,label:String,defaultVal:Any}> | -- |
| suffixCustomFilter | 后置自定义filter的配置,需要配合custom-filter-[key]插槽使用,SlotScop为{filterInfo, modelValue, updateModelValue, change} | Array<{key:String,label:String,defaultVal:Any}> | -- |
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
| groupTip | 分类名称提示信息 | String | -- |
| RelationshipKey | Relationship对应的参数名称 | String | -- |
| RelationshipTip | Relationship对应的提示 | String | -- |
| RelationshipItem | Relationship对应的下拉数据 | Array | -- |
| isWidthMultiple | 是否宽度占两个 | Boolean | false |
| isRequire | 是否必须选中 | Boolean | false |
| isVisibleRequired | 是否必须显示 | Boolean | false |
| optionRender | type为mul-select或者single-select时，下拉列表的渲染组件为Component,其中提供的props: ['id', 'label', 'level', 'source'] | Component | -- |
| selectLabelRender | type为mul-select或者single-select时，选中内容插槽,其中提供的props: ['selectSize', 'totalSize', 'titleList', 'itemList', 'parentName'] | Component | -- |
| extraOption | filter相对应的组件的额外配置 | Object | -- |
| forceDefault | 是否强制默认显示 | Boolean | false |
| isFirstExcute | 是否首次触发(仅有type为mul-select生效) | Boolean | false |
| dataCy | 自动化测试埋点属性，注意当type为mul-select，single-select时，生效在下拉列表中 | String | -- |
| dataCyValue | select显示值得自动化测试埋点属性，注意当type为mul-select，single-select时生效 | String | -- |
| dataCyFilter | select下拉列表中过滤框得自动化测试埋点属性，注意当type为mul-select，single-select时生效 | String | -- |
| emptyRender | type为mul-select或者single-select时,下拉列表为空时显示的内容 | Component | -- |
| isDynamicDefaultVal | 是否是动态默认值 | Boolean | -- |

## 方法 Methods

组件暴露的方法，可通过 ref 调用。

| 方法名 | 说明 | 参数 |
| --- | --- | --- |
| clear | 清空数据 | -- |
| search | 查询数据 | -- |
| initModelValue | 初始化filter中的modelValue值,注意：主要是为了简单模式的情况，无法准确捕捉初始化完成状态,类型为Function(query),其中query可以为空 | -- |
| getSelectedFilterInfo | 根据相对应的filterKeys列表获取filter信息，类型为Function({filterKeys:Array<String>}) | -- |
| updateFilterInfo | 更新相对应的filter配置信息，类型为Function({filterKey, options, beforeHook:Function({ filterKeyMap, options, filterInfo, formData) }) | -- |
| updateFilterList | 更新当前显示的filter配置列表,类型为Function({filterList, mergeType :"cover"\|"add" }) | -- |
| runFilterMethod | 运行filter实例方法 | Function({filterKey, methodName, params}) |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| filter-change | filter的change回调，参数为Object<{key, value,eventKey, relationship,emitChangeName,fromOrigin, updateFilterInfo: (filterKey, options) => {},updateModelValue(filterKey, options,{isVisible:true})) => {},注意如果是complex的类型，更新filter请用updateFilterInfo | Function(query) |
| search | 查询的回调，参数为query | Function(query,filterKeyMap,{planId,planName,visibleFilterList}) |
| save-name | 修改名称 | Function(planInfo) |
| save-plan | 保持方案,其中planInfo中添加了resolve(isSuccess)参数 | Function(planInfo) |
| delete-plan | 删除方案 | Function(planInfo) |
| init-complete | filter初始化完成事件 | Function(query) |
| apply-complete | apply应用完成的回调事件 | Function({filterKeyMap,query}) |
| apply-plan | 应用方案 | Function(query, hiddenQueryCacheTemp, extraOptions) |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| suffix | filter展示后缀 | -- |
| search-prefix | search按钮前置内容 | -- |
| custom-filter-[key] | 自定义filter的插槽,SlotScop为{filterInfo, modelValue, updateModelValue, change},key为filter的key | -- |

