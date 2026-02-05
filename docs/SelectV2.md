---
component: SelectV2
category: form
tags: [选择器, 虚拟列表, 大数据选择]
aliases: [SelectV2, 虚拟选择器]
version: 1.0.0
description: "SelectV2基础用法"
---

# SelectV2 组件文档

> SelectV2基础用法

**分类**: form | **标签**: 选择器、虚拟列表、大数据选择

## 使用示例

### 输入关键字以从远程服务器中查找数据.

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

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| width | Select 宽度。组件宽度，支持像素值或百分比 | String\|Number | 250 |
| data | 数据列表。数据源，用于渲染组件内容 | Array | [] |
| modelValue/v-model | 选中项绑定值 | Array\|String\|Number | [] |
| props | 配置选项，具体看下表 | Object | { value: 'value', label: 'label', children: 'children' } |
| type | select 类型，可选项multiple，single,transfer(下拉框为搜索框的样式) | String | multiple |
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
| remote | 是否为远程搜索 | Boolean | false |
| remote-method | 远程搜索方法 | Function | -- |
| label | 指定节点标签为节点对象的某个属性值 | String | -- |
| value | 指定节点value为节点对象的某个属性值 | String | -- |
| children | 指定子树为节点对象的某个属性值 | String | -- |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| change | 绑定值变化触发事件 | Function(value) |
| clear | 可清空的单选模式下用户点击清空按钮时触发 | Function() |

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

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/select.html)

