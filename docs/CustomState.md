---
component: CustomState
category: other
tags: [CustomState]
aliases: [CustomState]
version: 1.0.0
description: "PacvueCustomState 组件的简单应用"
---

# CustomState 组件文档

> PacvueCustomState 组件的简单应用

## 使用示例

### 示例：State1

```vue
<template>
  <PacvueCustomState v-model="stateVal" :data="itemList" :props="{ value: 'id', label: 'name' }"></PacvueCustomState>
</template>

<script setup>
  import { PacvueCustomState } from '@pacvue/element-plus'
  import { ref } from 'vue'
  var stateVal = ref('paused')
  var itemList = ref([
    {
      id: 'enabled',
      name: 'Enabled'
    },
    {
      id: 'paused',
      name: 'Paused'
    },
    {
      id: 'archived',
      name: 'Archived'
    }
  ])
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| modelValue/v-model | 当前选中的值 | String, Number | -- |
| data | 下拉列表数据,注意：你可以配置每一项的color来定义state的状态颜色(如果没有设置，有部分通用的颜色)，你也可以在每一项配置disabled属性是确定是否禁用它 | Array\|({rowData})=>Array | [] |
| props | 配置选项，具体看下表 | Object | { value: 'value', label: 'label'} |
| showLabel | 是否显示state的文本内容 | Boolean | tru |
| disabled | 是否禁用。是否禁用组件，禁用后无法进行交互 | Boolean | false |
| record | 行数据(data使用函数的时候，才需要) | Object | {} |
| label | 指定节点标签为节点对象的某个属性值 | String | -- |
| value | 指定节点value为节点对象的某个属性值 | String | -- |
| label | 显示数据节点名称 | String | -- |
| value | 数据的id | String | -- |
| color | 颜色 | String | -- |
| disabled | 是否禁用，如果禁用的化则会隐藏。是否禁用组件，禁用后无法进行交互 | Boolean | false |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| prefix | 文本前缀的内容,slotScope为{value,color} | -- |

