---
component: PacvueCascaderSelectV2
category: form
tags: [级联选择V2, 表单]
aliases: [PacvueCascaderSelectV2]
version: 1.0.0
description: "Cascader Select V2 基础用法"
---

# PacvueCascaderSelectV2 组件文档

> Cascader Select V2 基础用法

**分类**: form | **标签**: 级联选择V2、表单

## 使用示例

### 示例：index1 V2

```vue
<template>
  <PacvueCascaderSelectV2 v-model="values2" :data="options2" :labelInner="'Cascader'" :props="cascaderProps"
    placeholder="Campaign tag" :collapseTags="false" :isValRecusion="true" :countParentNode="false" :danger="danger"
    @change="selectChange" @clear="selectClear">
  </PacvueCascaderSelectV2>
</template>
<script setup>
  import { ref, shallowRef, shallowReactive } from 'vue'

  const danger = ref({ max: 5, text: '异常提示文案！' })
  // 生成假数据
  function mockData(long, length, parent) {
    const list = []
    long--
    for (let i = 0; i < length; i++) {
      const id = parent ? `${parent.tagId}|${long}-${i}` : `${long}-${i}`
      const node = { tagName: id, tagId: id }
      if (long) {
        const child = mockData(long, length, node)
        node.subTags = child
      }
      list.push(node)
    }
    return list
  }
  const cascaderProps = shallowReactive({ label: 'tagName', value: 'tagId', children: 'subTags' })
  const list = mockData(3, 20)
  for (let i = 2; i < 100; i++) {
    list.push({ tagName: `9-${i}`, tagId: `9-${i}` })
  }
  const options2 = shallowRef(list)
  const values2 = ref(['2-0|1-0|0-1', '2-0|1-0|0-0'])
  function selectChange(val) {
    console.log(val)
  }
  function selectClear() {
    console.log('clear')
  }
</script>
```

### v-model:selectData 为单向绑定值，只可以在初始化时设置一次值，之后

```vue
<template>
  <PacvueCascaderSelectV2 :useSelectData="true" v-model:selectData="selectData" :data="options2"
    :labelInner="'Cascader'" :props="cascaderProps" placeholder="Campaign tag" :collapseTags="true"
    :isValRecusion="true" :countParentNode="false" @change="selectChange" @clear="selectClear" @completed="completed">
  </PacvueCascaderSelectV2>
</template>
<script setup>
  import { ref, shallowRef, shallowReactive } from 'vue'
  // 生成假数据
  function mockData(long, length, parent) {
    const list = []
    long--
    for (let i = 0; i < length; i++) {
      const id = parent ? `${parent.tagId}|${long}-${i}` : `${long}-${i}`
      const node = { tagName: id, tagId: id }
      if (long) {
        const child = mockData(long, length, node)
        node.subTags = child
      }
      list.push(node)
    }
    return list
  }
  const cascaderProps = shallowReactive({ label: 'tagName', value: 'tagId', children: 'subTags' })
  const list = mockData(3, 20)
  for (let i = 2; i < 100; i++) {
    list.push({ tagName: `9-${i}`, tagId: `9-${i}` })
  }
  const options2 = shallowRef(list)
  const selectData = ref([
    {
      level: 2,
      tagId: '2-0|1-0|0-0',
      tagName: '2-0|1-0|0-0'
    },
    {
      level: 2,
      tagId: '2-0|1-0|0-1',
      tagName: '2-0|1-0|0-1'
    }
  ])
  function selectChange(val) {
    console.log(val)
  }
  function selectClear() {
    console.log('clear')
  }
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| modelValue/v-model | 选中项双向绑定值，只存储选中的叶节点的 id | Array | [] |
| v-model:selectData | 使用 object 管理选中数据，存储所有层级的全选状态节点，结构为一维数组。 | Array | [] |
| useSelectData | 是否使用 v-model:selectData 管理数据 | Boolean | false |
| width | 组件宽度。组件宽度，支持像素值或百分比 | String | 100% |
| labelInner | 内连显示label | String | -- |
| data | 数据列表。数据源，用于渲染组件内容 | Array | [] |
| props | 配置选项，具体看下表 | Object | { value: 'value', label: 'label', children: 'children' } |
| placeholder | Select提示信息。占位提示文字，在无输入时显示 | String | -- |
| collapseTags | 是否折叠tag显示 | Boolean | false |
| showPlaceholder | 是否显示提示信息 | Boolean | true |
| clearable | 是否可以清空选项。是否显示清除按钮，点击可清空当前值 | Boolean | false |
| disabled | 是否禁用。是否禁用组件，禁用后无法进行交互 | Boolean | false |
| teleported | 下拉列表是否添加到body中,默认true | Boolean | true |
| isSortByLetter | 下拉列表中是否按字母排序 | Boolean | true |
| dropdownMaxWidth | 下拉框的最大宽度，最小为200px | String | 800px |
| dropdownMaxHeight | 下拉框的最大高度 | String | 300px |
| hasSelectAll | 是否有全选功能 | Boolean | false |
| scrollIntoView | 级联数据出现横向滚动条时，是否自动将最新展开的数据滚动到可视区。默认开启。 | Boolean | true |
| max | 勾选的上限个数，与 props.props.max 取一个设置即可。 | Number | -- |
| min | 勾选的下限个数，与 props.props.min 取一个设置即可。 | Number | -- |
| trigger | 子节点展开的触发方式(click \| hover)。 | String | click |
| countParentNode | 勾选值中是否要包括非叶节点 | Boolead | true |
| valueLevelRise | 勾选值中，如果父节点状态是全选，则直接包含父节点而忽略子节点。当前属性与 countParentNode 互斥，countParentNode 为 true 时，当前属性失效。 | Boolead | false |
| shareSelect | 是否启用类似 share select 组件的统计逻辑：第一级节点勾选数量统计时，统计所有叶节点的勾选数量，而不是下一级子节点的数量。第一级节点没有子节点时，不显示勾选框。select all 默认隐藏。 | Boolead | false |
| showLeafTag | 节点tag展示时只展示叶节点信息，不将子节点归类成一个父节点展示。默认开启。 | Boolead | true |
| type | 组件勾选类型。。组件类型或模式 | "multiple" \| "single" | "multiple" |
| showLimitNodeTooltip | 节点禁用时是否显示 tooltip。 | Boolead | false |
| limitNodeTooltip | showLimitNodeTooltip 为 true 时，用于自定义 tooltip 文案 | Function | (node) => (`Choose up to {0} options`) |
| selectDataKeys | useSelectData 为 true 时，selectData 中存储的数据的属性名。可以理解为指定获取源数据中的哪些字段。 | Array | -- |
| hideSingleCheckbox | type 为 single 时是否需要隐藏 checkbox | Boolean | false |
| danger | 控制异常图标显示的配置对象，超出勾选上限则显示：{ max: Number（勾选数量上限，0 或 null 代表不限制勾选上限）, text: "异常图标tooltip文字"  | Object | { max: 0, text: "" } |
| createSelectLabelStyle | 生成选中项样式 | ({value})=>Object | -- |
| createItemStyle | 生成下拉列表中每一项的样式 | ({item})=>Object | -- |
| disableCallback | 下拉列表中checkbox禁用回调 | Function({item})=>Boolean | ()=>false |
| label | 指定节点标签为节点对象的某个属性值 | String | -- |
| value | 指定节点value为节点对象的某个属性值 | String | -- |
| children | 指定子树为节点对象的某个属性值 | String | -- |
| max | 勾选的上限个数，与 props.max 取一个设置即可。 | Number | -- |
| min | 勾选的上限个数，与 props.min 取一个设置即可。 | Number | -- |

## 方法 Methods

组件暴露的方法，可通过 ref 调用。

| 方法名 | 说明 | 参数 |
| --- | --- | --- |
| getSelectDataTree | 获取当前选中的数据的树形结构数组 | () => [] |
| clear | 清空选中数据 | () => {} |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| change | 绑定值变化触发事件 | Function(value) |
| clear | 可清空的单选模式下用户点击清空按钮时触发 | Function() |
| completed | 当数据初始化或数据更新后触发级联选择器重绘时，重绘完成后触发该事件 | Function() |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| empty | 当数据为空时自定义的内容 | -- |
| selectLabel | 选中显示的插槽内容,slotScop为{selectSize, totalSize, titleList, itemList,parentName,checkedNodes}(collapseTags为true时，不起作用) | -- |
| textSuffix | 输入框中自定义提示文字展示插槽 | -- |
| option | 下拉列表中每一项自定义内容展示插槽,slotScop为{item: Object} | -- |

