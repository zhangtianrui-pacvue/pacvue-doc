---
component: DatePickerFilter
category: form
tags: [日期筛选, 表单, 过滤]
aliases: [DatePickerFilter]
version: 1.0.0
description: "PacvueDatePickerFilter Filter定制日期选择"
---

# DatePickerFilter 组件文档

> PacvueDatePickerFilter Filter定制日期选择

**分类**: form | **标签**: 日期筛选、表单、过滤

## 使用示例

### Filter定制日期选择

```vue
<template>
  <PacvueDatePickerFilter :labelInner="'Label'" v-model="val" style="width: 424px" @change="changeFn" />
</template>

<script setup>
  import { ref, reactive } from 'vue'
  var val = ref(['2023/09/06', '2023/09/12'])
  const changeFn = (e, pickerMenu) => {
    console.log(e, pickerMenu)
  }
</script>

<style scoped></style>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| labelInner | 显示的Label名称 | String | -- |
| value-format | 可选，绑定值的格式。 不指定则绑定值为 Date 对象 | String | YYYY/MM/DD |
| format | 显示在输入框中的格式 | String | YYYY-MM-DD |
| model-value / v-model | 绑定值，如果它是数组，长度应该是 2 | Array | [] |
| disabled-date | 一个用来判断该日期是否被禁用的函数，接受一个 Date 对象作为参数。 应该返回一个 Boolean 值。 | Function | -- |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| change | 日期变化触发的事件 | Function(val,pickMenu) |

