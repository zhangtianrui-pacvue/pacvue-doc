---
component: PacvueCascaderSelect
category: form
tags: [级联选择, 表单, 多级]
aliases: [PacvueCascaderSelect, 级联]
version: 1.0.0
description: "Cascader Select基础用法"
---

# PacvueCascaderSelect 组件文档

> Cascader Select基础用法

**分类**: form | **标签**: 级联选择、表单、多级

## 使用示例

### 示例：index1

```vue
<template>
  <pacvue-cascader-select
    ref="homeTagOption"
    v-model="values"
    :data="options"
    :labelInner="'Cascader'"
    :props="{ label: 'tagName', value: 'tagId', children: 'subTags' }"
    @change="selectChange"
    :valueType="'object'"
    style="width: 100%"
    placeholder="Campaign tag"
    :showPlaceholder="true"
    :showAddTag="false"
    :isSortByLetter="true"
    :collapseTags="false"
    :isMutuallyExclusive="false"
    :isValRecusion="true"
  >
    <template #empty>NOT DATA</template>
  </pacvue-cascader-select>
</template>
<script setup>
  import { ref, getCurrentInstance } from 'vue'
  const values = ref([1005, '1004_100', '1004_1'])
  const options = ref([
    { tagName: 'btoB1-1', tagId: '1009-1' },
    { tagName: 'atoB1-1', tagId: '1008-1' },
    { tagName: 'btoB', tagId: '1009' },
    { tagName: 'atoB', tagId: '1008' },
    { tagName: 'ctoB', tagId: '1007', isTop: true },
    { tagName: 'BtoA', tagId: '1001' },
    { tagName: 'AtoB', tagId: '1002' },
    {
      tagName: 'My Brands',
      tagId: '1003',
      subTags: getSubTags()
    },
    { tagName: 'otherBrands', tagId: '1006', subTags: [] }
  ])
  var selectChange = (values) => {
    console.log('>>>>>>>>selectChange', values)
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
| modelValue/v-model | 选中项绑定值 | Array\|String\|Number | [] |
| labelInner | 内连显示label | String | -- |
| data | 数据列表。数据源，用于渲染组件内容 | Array | [] |
| props | 配置选项，具体看下表 | Object | { value: 'value', label: 'label', children: 'children', max: undefined} |
| placeholder | Select提示信息。占位提示文字，在无输入时显示 | String | -- |
| collapseTags | 是否折叠tag显示 | Boolean | false |
| showPlaceholder | 是否显示提示信息 | Boolean | false |
| clearable | 是否可以清空选项。是否显示清除按钮，点击可清空当前值 | Boolean | false |
| disabled | 是否禁用。是否禁用组件，禁用后无法进行交互 | Boolean | false |
| teleported | 下拉列表是否添加到body中,默认true | Boolean | true |
| isSortByLetter | 下拉列表中是否按字母百姓 | Boolean | true |
| dropdownWidth | 下拉框的宽度 | String | auto |
| dropdownHeight | 下拉框的高度 | String | 300px |
| hasSelectAll | 是否有全选功能 | Boolean | false |
| addTagLabel | Add Tag按钮的名称 | String | Add Tag |
| showAddTag | 是否显示Add Tag按钮 | Boolean | true |
| isMutuallyExclusive | 是否一级互斥 | Boolean | false |
| isValRecusion | 是否值逆向匹配 | Boolean | false |
| tagUnit | 显示为tag模式下的代为 | String | -- |
| valueType | change事件中参数的类型,可取值为auto或object | String | auto |
| max | 勾选的上限个数，与 props.props.max 取一个设置即可。 | Number | -- |
| createSelectLabelStyle | 生成选中项样式 | ({value})=>Object | -- |
| createItemStyle | 生成下拉列表中每一项的样式 | ({item})=>Object | -- |
| disableCallback | 下拉列表中checkbox禁用回调 | Function({item})=>Boolean | ()=>false |
| dropdownWidthRatio | 下拉框的宽度相对应触发元素的宽度比例 | Number | 0.5 |
| label | 指定节点标签为节点对象的某个属性值 | String | -- |
| value | 指定节点value为节点对象的某个属性值 | String | -- |
| children | 指定子树为节点对象的某个属性值 | String | -- |
| max | 勾选的上限个数 | Number | -- |

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
| textSuffix | 输入框中自定义提示文字展示插槽 | -- |
| option | 下拉列表中每一项自定义内容展示插槽,slotScop为{item: Object} | -- |

