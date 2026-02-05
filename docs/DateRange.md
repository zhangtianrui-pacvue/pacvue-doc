---
component: DateRange
category: form
tags: [日期范围, 表单, 时间范围]
aliases: [DateRange, 日期范围]
version: 1.0.0
description: "PacvueDateRange 日期范围选择"
---

# DateRange 组件文档

> PacvueDateRange 日期范围选择

**分类**: form | **标签**: 日期范围、表单、时间范围

## 使用示例

### 日期范围选择组件

```vue
<template>
  <div class="textCenter">
    <PacvueDateRange :dateRange="dateRange" type="daterange" format="MM/DD/YYYY" value-format="YYYY-MM-DD"
      range-separator="~" :start-placeholder="'start'" :end-placeholder="'end'" :showTip="true" :tipText="'tip文字'"
      :state="'error'" />
  </div>
</template>
<script lang="ts" setup>
  import { ref } from 'vue'
  import { dayjs } from '@pacvue/element-plus'

  const TODAY_FORMAT = dayjs().format('YYYY-MM-DD')
  const dateRange = ref({ start: TODAY_FORMAT, end: '' })
</script>
<style scoped>
  .textCenter {
    text-align: center;
  }
</style>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| dateRange | 当前选中的日期数据 | object | { start: "", end: "" } |
| disabled | 禁用日期控件。是否禁用组件，禁用后无法进行交互 | boolean | false |
| startDisabled | 禁止选择开始时间 | boolean | false |
| endDisabled | 禁止选择结束时间 | boolean | false |
| prefix-icon | 前缀图标设置 | string \| Component | NewDate |
| prefix-position | 前缀图标位置: "right"\|"left" | string | right |
| format | 日期格式化 | string | MM/DD/YYYY |
| value-format | 可选，绑定值的格式。 不指定则绑定值为 Date 对象 | string | YYYY/MM/DD |
| showTip | 是否显示日期控件tip | boolean | false |
| tipText | 日期控件tip内容 | string | -- |
| state | 日期控件状态: "default"\|"error" | string | default |
| startToday | 开始时间，是否禁选当天之前的时间 | boolean | true |
| width | 日期控件宽度设置。组件宽度，支持像素值或百分比 | string | 350px |
| startDisabledDate | 用于设置 开始时间禁用范围 | function | -- |
| endDisabledDate | 用于设置 结束时间禁用范围 | function | -- |
| showTodaySelect | 是否显示today日期选择按钮 | boolean | true |
| clearableStart | 是否显示开始时间清除按钮，默认开启。 | boolean | true |
| clearableEnd | 是否显示结束时间清除按钮，默认开启。 | boolean | true |

