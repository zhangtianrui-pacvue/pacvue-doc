---
component: YearRangePicker
category: other
tags: [YearRangePicker]
aliases: [YearRangePicker]
version: 1.0.0
description: "PacvueYearRangePicker年日期范围选择"
---

# YearRangePicker 组件文档

> PacvueYearRangePicker年日期范围选择

## 使用示例

### 示例：year Range

```vue
<template>
  <PacvueYearRangePicker v-model="value" :disabledDate="disabledDate" :disabled="false" :clearable="true" :placeholder="'Plear Select Year Range'"></PacvueYearRangePicker>
</template>
<script setup>
  import { ref } from 'vue'
  import { dayjs } from 'element-plus'
  const value = ref(['2005', '2013'])
  var disabledDate = (year) => {
    return dayjs(year).year() > 2024
  }
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| prefix-icon | 前缀图标，已替换新日历SVG | String \| Component | NewDate |
| prefix-position | 前缀图标位置 | String | right |
| clearable | 是否有清除功能。是否显示清除按钮，点击可清空当前值 | Boolean | true |
| disabledDate | 一个用来判断该日期是否被禁用的函数，接受一个 Date 对象作为参数。 应该返回一个 Boolean 值。 | (data: Date) => boolean | -- |
| v-model | 当前显示的年范围。双向绑定值，用于获取和设置组件的当前值 | Array | [] |
| rangeSeparator | 选择范围时的分隔符 | String | - |
| disabled | 是否禁用。是否禁用组件，禁用后无法进行交互 | Boolean | false |
| placeholder | 占位内容。占位提示文字，在无输入时显示 | String | -- |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| change | 绑定值变化触发事件 | Function(value) |

