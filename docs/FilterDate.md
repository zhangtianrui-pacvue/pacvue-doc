---
component: FilterDate
category: filter
tags: [日期筛选, 过滤]
aliases: [FilterDate]
version: 1.0.0
description: "PacvueFilterDate组件的简单应用"
---

# FilterDate 组件文档

> PacvueFilterDate组件的简单应用

**分类**: filter | **标签**: 日期筛选、过滤

## 使用示例

### 示例：index1

```vue
<template>
  <PacvueFilterDate :labelInner="'Label'" :clearable="false" :wrapWidth="'300px'" type="daterange" v-model="date"></PacvueFilterDate>
</template>

<script setup>
  import { ref } from 'vue'
  var date = ref([])
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| model-value / v-model | 绑定值，如果它是数组，长度应该是 2 | Date / number / string / Array | -- |
| type | 显示类型。组件类型或模式 | year/month/date/dates/datetime/ week/datetimerange/daterange/ monthrange | date |
| labelInner | 显示的label名称 | String | -- |
| fitWidth | 是否适应宽度,开启时最小宽度为240 | Boolean | false |
| datePickerMinW | 日期选择器的最小宽度 | String | 222px |
| wrapWidth | 容器的宽度 | String | -- |
| label | 指定节点标签为节点对象的某个属性值 | String | -- |
| value | 指定节点value为节点对象的某个属性值 | String | -- |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| focus | 日期选择器获取焦点 | Function() |
| blur | 日期选择器失去焦点 | Function() |

## 相关链接

- [Element Plus 文档](/#/datePicker)

