---
component: PacvueCustomDatePicker
category: form
tags: [自定义日期, 表单]
aliases: [PacvueCustomDatePicker]
version: 1.0.0
description: "PacvueCustomDatePicker 年日期范围选择"
---

# PacvueCustomDatePicker 组件文档

> PacvueCustomDatePicker 年日期范围选择

**分类**: form | **标签**: 自定义日期、表单

## 使用示例

### 示例：year Range

```vue
<template>
  <PacvueCustomDatePicker v-model="yearRange" :disabledDate="disabledDate" :disabled="false" :clearable="true" :placeholder="'Plear Select Year Range'" :type="'yearrange'" :selectionLimit="4" :weekStart='0' :formatShowLabel="formatShowLabel" ></PacvueCustomDatePicker>
</template>
<script setup>
import { ref } from 'vue'
const yearRange= ref(['2024/01/16', ' 2024/01/29'])
var disabledDate = (year) => {
 // return dayjs(year).year() > 2024
 return   year.getTime() > Date.now()
}
let formatShowLabel =({ value,showLabel})=>{
  console.log('>>>>>>value',value,showLabel)
  return showLabel
}
</script>
```

### 示例：year Range

```vue
<template>
  <PacvueCustomDatePicker v-model="yearRange" :disabledDate="disabledDate" :disabled="false" :clearable="true" :placeholder="'Plear Select Year Range'" :type="'yearrange'" :selectionLimit="4" :weekStart='0' :formatShowLabel="formatShowLabel" ></PacvueCustomDatePicker>
</template>
<script setup>
import { ref } from 'vue'
const yearRange= ref(['2024/01/16', ' 2024/01/29'])
var disabledDate = (year) => {
 // return dayjs(year).year() > 2024
 return   year.getTime() > Date.now()
}
let formatShowLabel =({ value,showLabel})=>{
  console.log('>>>>>>value',value,showLabel)
  return showLabel
}
</script>
```

### 示例：week Range

```vue
<template>
  <PacvueCustomDatePicker v-model="weekRange" :disabledDate="disabledDate" :disabled="false" :clearable="true" :placeholder="'Plear Select Week Range'" :type="'weekrange'" :selectionLimit="4" :weekStart='1' :formatShowLabel="formatShowLabelWeek" valueFormat="YYYY/MM/DD"></PacvueCustomDatePicker>
<script setup>
import { ref } from 'vue'
const weekRange= ref(['2024/01/16', ' 2024/01/29'])
var disabledDate = (year) => {
 // return dayjs(year).year() > 2024
 return   year.getTime() > Date.now()
}
let formatShowLabelWeek =({ value,showLabel,dateRange})=>{
  if(dateRange?.length){
    let startVal = dateRange[0].startOf('week').format('YYYY-MM-DD')
    let endVal = dateRange[1].endOf('week').format('YYYY-MM-DD')
    return startVal+'-'+endVal
  }
  return showLabel
}
</script>
```

### 示例：month Range

```vue
<template>
  <PacvueCustomDatePicker v-model="monthRange" :disabledDate="disabledDate" :disabled="false" :clearable="true" :placeholder="'Plear Select Week Range'" :type="'monthrange'" :selectionLimit="4" :weekStart='0' :formatShowLabel="formatShowLabel" ></PacvueCustomDatePicker>
</template>
<script setup>
import { ref } from 'vue'
const monthRange= ref(['2024/01/16', ' 2024/01/29'])
var disabledDate = (year) => {
 // return dayjs(year).year() > 2024
 return   year.getTime() > Date.now()
}
let formatShowLabel =({ value,showLabel})=>{
  console.log('>>>>>>value',value,showLabel)
  return showLabel
}
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| v-model | 当前显示的年范围。双向绑定值，用于获取和设置组件的当前值 | Array | [] |
| disabledDate | 一个用来判断该日期是否被禁用的函数，接受一个 Date 对象作为参数。 应该返回一个 Boolean 值。 | (data: Date) => boolean | -- |
| disabled | 是否禁用。是否禁用组件，禁用后无法进行交互 | Boolean | false |
| clearable | 是否有清除功能。是否显示清除按钮，点击可清空当前值 | Boolean | true |
| placeholder | 占位内容。占位提示文字，在无输入时显示 | String | -- |
| type | 日期类型可选值为weekrange/monthrange/yearrange/quarterrange | String | yearrange |
| selectionLimit | 日期范围跨度 | Number | -- |
| weekStart | 周从周几开始,周日是0,以此类推 | Number | 0 |
| formatShowLabel | 格式化选中的值,返回自定义显示的内容 | Function({ value,showLabel,dateRange:Array<dayjs>}) | -- |
| prefix-icon | 前缀图标，已替换新日历SVG | String \| Component | NewDate |
| prefix-position | 前缀图标位置 | String | right |
| rangeSeparator | 选择范围时的分隔符 | String | - |
| isPanelMultiple | 是否显示两个日期选择器(Note:目前仅支持type为weekrange) | Boolean | false |
| quickList | 快捷键功能(Note:目前仅支持type为weekrange,并且isPanelMultiple为tru时候) | Array | - |
| isIsolateCustom | 是否Custom快捷键可以激活选中(只对type为weekrange有效) | Boolean | true |
| isCustomQuick\|v-model:isCustomQuick | 当前是否是Custom快捷键(只对type为weekrange有效) | Boolean | false |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| change | 绑定值变化触发事件 | Function(value) |

