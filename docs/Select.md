---
component: Select
category: form
tags: [选择器, 表单, 下拉选择]
aliases: [Select, 选择, 下拉框]
version: 1.0.0
description: "可输入的Select"
---

# Select 组件文档

> 可输入的Select

**分类**: form | **标签**: 选择器、表单、下拉选择

## 使用示例

### 示例：index3

```vue
<template>
  <PacvueSelect
    ref="selectRef2"
    :data="singleOption"
    v-model="value3"
    :props="props3"
    width="200px"
    class="mx-8"
    type="single"
    :disabled="false"
    :clearable="true"
    @change="changeFuc"
    valueType="auto"
    :maxLength="10"
    :isCanInput="true"
    :isDynamicTooltip="true"
    :dataCy="'auto_000001'"
    @visible-change="popperVisibleChange"
    show-tip
    state="error"
    :tip-text="'这个是个错误信息'"
  >
    <template #selectLabel="{ selectSize, totalSize, titleList, itemList }">----LIST-----</template>
    <template #tooltip>test Tooltip</template>
    <template #aside>999</template>
  </PacvueSelect>
</template>
<script setup>
  import { ref } from 'vue'
  const value3 = ref('')
  const value4 = ref([])
  const singleOption = ref([])
  var props3 = ref({ value: 'id', label: 'name', children: 'children' })
  const options2 = [
    {
      id: 'Option1',
      name: 'Option1 Option1 Option1 Option1 Option1 Option1 Option1'
    },
    {
      id: 'Option2',
      name: 'Option2',
      disabled: true
    },
    {
      id: 'Option3',
      name: 'Option3'
    },
    {
      id: 'Option4',
      name: 'Option4'
    },
    {
      id: 'Option5',
      name: 'Option5'
    }
  ]
  var changeFuc = ($event) => {
    console.log('>>>>>>>$envet', $event)
    //value3.value = '123123'
  }
  var popperVisibleChange = (isShow) => {
    if (isShow) {
      singleOption.value = [
        {
          name: 'My Brands',
          id: 'mybrands',
          children: [
            {
              id: 'null',
              name: null
            },
            {
              id: '‘’@！#￥%……&*（“”）tetwetwerewrwrwerwerewrerwrwwrwerewrew',
              name: '‘’@！#￥%……&*（“”）（“”）tetwetwerewrwrwerwerewrerwrwwrwerewrew'
            }
          ]
        },
        {
          name: 'Other Brands',
          id: 'otherbrands',
          children: []
        }
      ]
    }
  }
  setTimeout(() => {
    singleOption.value = options2
  }, 3000)
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### 适用广泛的基础单选 v-model 的值为当前被选中的

```vue
<template>
  <div>
    <p class="mb-4">单选select，值是基本类型</p>
    <PacvueSelect
      :data="singleOption"
      v-model="value3"
      style="width: 200px"
      :props="props3"
      type="single"
      :clearable="true"
      labelInner="Label"
      :showLabelInner="false"
      :disabled="false"
      :disableCallback="disableCallback"
      :autoResize="true"
      :dropdownWidth="'400px'"
      :filterable="true"
      :isKeywordMatchValue="isKeywordMatchValue"
      :validation="validation"
      ref="selectRef"
      @change="changeFn"
      @clear="clearFn"
      isTipAbsolute
      showTip
      state="error"
    >
      <template #empty>Empty Data</template>
      <template #selectLabel="{ selectSize, totalSize, titleList, itemList, value, checkedNodes, parentName, defaultShowLabel }">
        {{ parentName ? parentName + '--' : '' }}{{ titleList[0] || '' }}
      </template>
      <template #option="item">{{ item.label }}</template>
    </PacvueSelect>
  </div>
  <div>
    <p class="mb-4">单选select，值是数组类型</p>
    <pacvue-button @click="updateDisabledFields">改变禁用字段</pacvue-button>
    <div style="width: 400px; display: flex; flex-direction: column; margin-top: 16px">
      <PacvueSelect
        :data="singleOption"
        v-model="value4"
        :props="props3"
        style="width: 100%"
        type="single"
        :clearable="true"
        labelInner="Label"
        :tip="'2121231'"
        :showLabelInner="true"
        :autoResize="false"
        isValRecusion
        isRequireVal
        valueType="array"
        @change="changeFn"
      >
        <template #header>Header</template>
      </PacvueSelect>
    </div>
  </div>
</template>
<script setup>
  import { ref } from 'vue'
  const value3 = ref('')
  const value4 = ref([])
  const singleOption = ref([])
  var isKeywordMatchValue = ref(true)
  var props3 = ref({ value: 'id', label: 'name', children: 'children' })
  var validation = (value) => {
    if (value) {
      return ''
    } else {
      return 'not emtpy'
    }
  }
  const options2 = [
    {
      id: 'Option1',
      name: 'Option1 Option1 Option1 Option1 Option1 Option1 Option1'
    },
    {
      id: 'Option2',
      name: 'Option2',
      disabled: true
    },
    {
      id: 'Option3',
      name: 'Option3'
    },
    {
      id: 'Option4',
      name: 'Option4'
    },
    {
      id: 'Option5',
      name: 'Option5'
    }
  ]
  var disabledDatas = ref([3, 4])
  var disableCallback = computed(() => {
    var disabledData = disabledDatas.value
    return (node) => {
      if (disabledData.includes(node.id) || node.source.disabled) {
        return true
      } else if (node.source.disabled === false) {
        return false
      }
    }
  })
  var updateDisabledFields = () => {
    disabledDatas.value = [2, 3, 4, 5]
  }
  var changeFn = (values) => {
    console.log('>>>>>>>change', values)
  }
  var clearFn = (values) => {
    console.log('>>>>>>>clear', values)
  }
  setTimeout(() => {
    singleOption.value = options2
  }, 3000)
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### 你可以通过设置type为multiple，使用多选

```vue
<template>
  <div style="display: flex; align-items: center; width: 300px">
    <PacvueSelect
      ref="curSelelectRef"
      :data="options3"
      v-model="value"
      :props="props3"
      @change="changeFn2"
      :showSelectAll="true"
      :isMutuallyExclusive="false"
      clearable
      style="width: 100%"
      :popperClass="'pacvue-test-popperCalss'"
      class="pacvue-test-select"
    />
  </div>
  <div style="display: flex; align-items: center; width: 300px; margin-left: 24px">
    <PacvueSelect
      :data="options2"
      v-model="value2"
      width="100%"
      :props="props3"
      type="multiple"
      isValRecusion
      :minLimit="1"
      :maxLimit="3"
      :showSelectAll="true"
      @change="changeFn3"
      :collapseTags="false"
      clearable
    />
  </div>
</template>

<script setup>
  import { ref } from 'vue'
  //单选
  var props3 = ref({ value: 'id', label: 'name', children: 'children' })
  const options3 = ref([])
  const value = ref(['3_0'])
  const value2 = ref(['Option1', 'test113', 'test114', 'Option2', 'GGGG'])
  const handleChange = (value) => {
    console.log(value)
  }
  const options2 = ref([
    {
      id: 'Option1Group',
      name: 'Option1Group',
      isOptionGroup: true
    },
    { id: 'Option0', name: 'Option0' },
    {
      id: 'Option1',
      name: 'Option1',
      children: [
        {
          id: 'test113',
          name: 'test-sub 123 test-sub 123 test-sub 123 test-sub 123 test-sub 123 test-sub 123 test-sub 123 test-sub 123 test-sub 123 test-sub 123 test-sub 123'
        },
        {
          id: 'test114',
          name: 'test-sub 444'
        }
      ]
    },
    {
      id: 'Option2',
      name: 'Option2',
      disabled: true
    },
    {
      id: 'Option1Group2',
      name: 'Option1Group-2',
      isOptionGroup: true
    },
    {
      id: 'Option309999',
      name: 'Option30999999'
    },
    {
      id: 'Option4',
      name: 'Option4'
    },
    {
      id: 'Option5',
      name: 'Option5'
    },
    {
      id: 'Option11',
      name: 'Option1',
      children: [
        {
          id: 'test1133',
          name: 'test-sub 123 test-sub 123 test-sub 123 test-sub 123 test-sub 123 test-sub 123 test-sub 123 test-sub 123 test-sub 123 test-sub 123 test-sub 123'
        },
        {
          id: 'test1141',
          name: 'test-sub 4443'
        }
      ]
    },
    {
      id: 'Option21',
      name: 'Option21',
      disabled: true
    },
    {
      id: 'Option31',
      name: 'Option3'
    },
    {
      id: 'Option41',
      name: 'Option41'
    },
    {
      id: 'Option51',
      name: 'Option51'
    }
  ])
  var changeFn2 = (values) => {
    console.log('>>>>>>>>>>change2', values)
  }
  var changeFn3 = (values) => {
    console.log('>>>>>>>change3', values)
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
| width | Select 宽度。组件宽度，支持像素值或百分比 | String\|Number | 250 |
| data | 数据列表。数据源，用于渲染组件内容 | Array | [] |
| modelValue/v-model | 选中项绑定值 | Array\|String\|Number | [] |
| props | 配置选项，具体看下表 | Object | { value: 'value', label: 'label', children: 'children' } |
| type | select 类型，可选项multiple，single | String | multiple |
| showCheckbox | 是否显示checkbox | Boolean | true |
| clearable | 是否可以清空选项。是否显示清除按钮，点击可清空当前值 | Boolean | false |
| labelInner | 内连显示label | String | -- |
| collapseTags | 是否折叠选中显示的内容 | Boolean | false |
| autoResize | 宽度是否随着内容增多，自动扩展宽度 | Boolean | false |
| disableCallback | 判断节点是否可用，参数为当前节点信息node,需要返回boolean | Function | function(node) |
| isValRecusion | 是否值逆向匹配 | Boolean | false |
| valueType | 选中项的类型，默认auto，可选类型为array,auto | String | auto |
| isRequireVal | 是否必须选中一项，只针对type=single模式(note:需要设置isValRecusion为true) | Boolean | false |
| dropdownWidth | 下拉框的宽度，默认auto | String | auto |
| dropdownHeight | 下拉框的高度，默认auto | String | 300px |
| filterable | 是否显示过滤框。是否支持筛选/搜索功能 | Boolean | true |
| disabled | 是否禁用。是否禁用组件，禁用后无法进行交互 | Boolean | false |
| height | 显示框的高度。组件高度，支持像素值或百分比 | String | 36px |
| maxLimit | 限制选中的最大数目 | Number | - |
| minLimit | 限制选中的最小数目 | Number | - |
| showCollapseTagsList | 是否显示collaseTag的列表 | Boolean | false |
| teleported | 下拉列表是否添加到body中,默认true | Boolean | true |
| showSelectAll | 是否全选功能 | Boolean | true |
| isOnlyHandTrigger | 是否只有手动切换触发change事件 | Boolean | true |
| limitLevel | 是否限制为一级多选，二级只能单选一个 | Boolean | false |
| itemHeight | 手动设置单个节点的行高 | Boolean | 38 |
| validation(已废弃),具体参考state用法 | 验证规则,返回的是错误信息 | Function(modelValue) | -- |
| tip-text | 输入框提示文案。提示文案内容 | string | —— |
| state | 输入框状态 可选值:success/warning/error | string | —— |
| show-tip | 输入框是否显示提示。是否显示提示信息 | boolean | false |
| minDropdownWidth | 下拉框的宽度最小宽度 | String | -- |
| maxDropdownWidth | 下拉框的宽度最大宽度 | String | -- |
| isCanInput | 是否可以输入(只针对单选) | Boolean | false |
| maxLength | 最大输入数目(只针对单选) | Number/String | -- |
| popperClass | 下拉框容器的class | String | -- |
| isMultiFilter | 是否开启多规则匹配，为onlyFilter不显示多种类型切换 | Boolean\|Boolean | false |
| multipleFilterPlaceholder | 多规则匹配placeholder | String | -- |
| hasBorder | 是否有border | Boolean | false |
| isDynamicTooltip | 是否开启动态tip(内容超出宽度显示tooltip) | Boolean | true |
| transformToString | 是否要将 tree 的唯一 id 统一转换成 String 类型，默认不转换。 | Boolean | false |
| defaultExpanded | 是否默认展开子节点 | Boolean | true |
| useNewTextWrap | 使用 内容在换行时 上下边（15px）距相等 的显示规则，并且支持 内容动态高度， 默认不开启。 | Boolean | false |
| selectLoading | 用于控制下拉框的 loading 状态。 | Boolean | false |
| dropdownAppendTo | 指示 Tooltip 的内容将附加在哪一个网页元素上 | CSSSelector/HTMLElement | -- |
| isInDialog | 是否在dialog中 | Boolean | false |
| isMutuallyExclusive | 是否一级互斥 | Boolean | false |
| isKeywordMatchValue | 是否开启搜索框中匹配prop为vlaue所对应的文本 | Boolean | false |
| isWithPausedRecusion | 是否开启禁用无法设值的回流功能 | Boolean | false |
| dataCy | 下拉列表中dataCy属性 | String | -- |
| dataCyValue | select显示值的dataCy属性 | String | -- |
| dataCyFilter | 下拉列表中过滤框的dataCy属性 | String | -- |
| lineClamp | 下拉列表中每一列出现省略号的行数的 | String\|Number | 2 |
| isWatchResize | 是否监控下拉列表中每一行的大小 | Boolean | false |
| dropdownMaxWidthRatio | 下拉列表最大宽度基于select框宽度的比率 | Number | 1.5 |
| dropdownPlaceholder | dropdown 中关键词筛选 input 的 placeholder 设置 | String | -- |
| isAutoPosition | 是否实时更新dropdown位置 | Boolean | false |
| hasPrependSplitLine | 前置内容跟主体内容是否有分隔线 | Boolean | false |
| hasAppendSplitLine | 后置内容跟主体内容是否有分隔线 | Boolean | false |
| isDynamicH | 是否支持下拉列表中动态高度 | Boolean | false |
| isEmptyShowFilterable | 是否开启下拉列表为空的时候显示过滤框 | Boolean | false |
| isAutoHidePopper | 是否开启触发元素隐藏立即关闭下拉框 | Boolean | false |
| dropdownListVisible/v-dropdownListVisible | 下拉框是否显示 | Boolean | false |
| createCustomUUId | 下拉列表中每一项自定义唯一值 | Function | ({id, item}) => String |
| isUniqueData | 是否下拉列表中去除重复项 | Boolean | true |
| createSelectLabelStyle | 生成选中项样式 | ({value})=>Object | -- |
| createItemStyle | 生成下拉列表中每一项的样式 | ({item})=>Object | -- |
| isShowAllWithEnable | 是否在有可选的节点时候才显示SelectAll功能 | Boolean | false |
| isSelectAllReverseToMaxLimit | 是否达到最大限制时候,全选可以反向选择 | Boolean | false |
| showSelectAllThrold | 显示全选功能阈值,如果为0,则不起作用,小于等于该值时显示全选功能 | Number | 0 |
| showSelectAllThroldMode | 显示全选功能阈值对比数据模式,可选值为filter(过滤后的数据)\|data(源数据) | String | filter |
| hasAddNewItem | 是否有新增条目功能 | Boolean | false |
| addNewItemOptions | 新增条目功能配置,Object<{validation:Function,save:Function}> | Object | -- |
| itemVerticalAlign | 下拉列表中每一项的垂直对齐方式,可选值为start(默认)\|center | String | start |
| isKeepHoverOnRight | 是否保持悬浮在右侧时，一级hover样式不消失 | Boolean | false |
| enableWithPaused | 是否可以设置暂停状态的勾选状态 | Boolean | false |
| isRecusionByLimit | 是否根据限制数目的min或max配置进行逆向匹配 | Boolean | false |
| hasRelationship | 是否显示关系选择 | Boolean | false |
| relationshipData | 关系选择数据 | Array | [] |
| v-model:relationship | 关系选择绑定值 | String\|Number | -- |
| label | 指定节点标签为节点对象的某个属性值 | String | -- |
| value | 指定节点value为节点对象的某个属性值 | String | -- |
| children | 指定子树为节点对象的某个属性值 | String | -- |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| change | 绑定值变化触发事件 | Function(value) |
| clear | 可清空的单选模式下用户点击清空按钮时触发 | Function() |
| customRowHover | 鼠标悬浮在节点上时触发 | Function(item) |
| customRowEnter | 鼠标进入下拉列表节点时触发 | Function({ record, updatePopoverPosition }) |
| customRowLeave | 鼠标离开下拉列表节点时触发 | Function({ event, record, updatePopoverPosition }) |
| customTreeBodyLeave | 鼠标离开下拉列表树形结构时触发 | Function({ updatePopoverPosition }) |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| empty | 当数据为空时自定义的内容 | -- |
| selectLabel | 选中显示的插槽内容,slotScop为{selectSize, totalSize, titleList, itemList,parentName,checkedNodes}(collapseTags为true时，不起作用) | -- |
| option | 每一个item选项slotScop为{id: Any,label: String,level: Number,source: Object},source为源数据 | -- |
| header | 在搜索框之后，tree之前的位置 | -- |
| tip-icon | 输入框提示图标 | svg |
| tooltip | 下拉内容tooltip 内容插槽 | -- |
| aside | 下拉内容右边辅助插槽 | -- |
| customIcon | 自定义图标插槽，生成在展开图标和删除图标的左侧。 | -- |
| labelIcon | 内连显示label后面的图标 | -- |
| prepend | 输入框前置内容 | -- |
| append | 输入框后置内容 | -- |
| keyowrdInputApendSlot | 下拉框过滤框后置内容 | -- |
| itemSuffix | 下拉内容最右边插槽 | -- |
| addNewItem | 新增条目插槽 | -- |
| dropDownTreeRight | 下拉框树形结构右边辅助插槽 | -- |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/select.html)

