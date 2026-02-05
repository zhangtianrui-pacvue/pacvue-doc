---
component: DatePickerQuick
category: form
tags: [快捷日期, 表单]
aliases: [DatePickerQuick]
version: 1.0.0
description: "日期范围选择"
---

# DatePickerQuick 组件文档

> 日期范围选择

**分类**: form | **标签**: 快捷日期、表单

## 使用示例

### 示例：html1

```vue
<template>
  <PacvueDatePickerQuick v-model="modelValue" :quickRanges="quickRanges" />
</template>

<script setup>
  import { dayjs } from 'element-plus'
  function getRange(key) {
    if (key === 'Next 30 days') {
      const start = dayjs().add(1, 'day')
      const end = dayjs().add(30, 'day')
      return [start.toDate(), end.toDate()]
    }
    if (key === 'Next month') {
      const start = dayjs().add(1, 'month').startOf('month');
      const end = dayjs().add(1, 'month').endOf('month');
      return [start.toDate(), end.toDate()]
    }
    if (key === 'Next 90 days') {
      const start = dayjs().add(1, 'day')
      const end = dayjs().add(90, 'day')
      return [start.toDate(), end.toDate()]
    }
    if (key === 'Next quarter') {
      const start = dayjs().add(1, 'quarter').startOf('quarter');
      const end = dayjs().add(1, 'quarter').endOf('quarter');
      return [start.toDate(), end.toDate()]
    }
  }
  // 生成快捷日期范围
  const quickRanges = {
    'Next 30 days': getRange('Next 30 days'),
    'Next month': getRange('Next month'),
    'Next 90 days': getRange('Next 90 days'),
    'Next quarter': getRange('Next quarter')
  }
  const nextdays = quickRanges['Next 30 days']
  // 默认选中的日期范围
  const modelValue = ref([...nextdays])
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| v-model | 当前选中的时间范围，如果没有设置，则会自动选中 quickRanges 的第一个配置对象。 | [startDate, endDate] | [] |
| quickRanges | 自定义快捷日期选择的可选项 | Object | { "Next 30 days": [startDate, endDate] } |
| labelInner | 显示的Label名称 | String | -- |
| needCustomRange | 是否开启自定义框选功能 | Boolean | false |
| minDate | 最小日期 | Date | -- |
| maxDate | 最大日期 | Date | -- |
| isQuickAutoApply | 是否点击快捷键的时候自动应用 | Boolean | false |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| selectLabel | 选中显示的插槽内容,slotScope为{startDate, endDate, quickKey, startText, endText} | -- |

