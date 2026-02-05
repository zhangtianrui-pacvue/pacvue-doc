---
component: Radio
category: form
tags: [单选框, 表单, 单选]
aliases: [Radio, 单选]
version: 1.0.0
description: "Radio 单选框"
---

# Radio 组件文档

> Radio 单选框

**分类**: form | **标签**: 单选框、表单、单选

## 使用示例

### 基础用法

```vue
<template>
  <div>
    <pacvue-radio-group v-model="radio">
      <pacvue-radio label="1">Option 1</pacvue-radio>
      <pacvue-radio label="2">Option 2</pacvue-radio>
    </pacvue-radio-group>
  </div>
</template>
<script setup>
  import { ref } from 'vue'
  const radio = ref('1')
</script>
```

### 通过 disabled 属性指定 Radio 组件禁用状态

```vue
<template>
  <pacvue-radio v-model="radio1" disabled label="disabled">Option A</pacvue-radio>
  <pacvue-radio v-model="radio1" disabled label="selected and disabled">Option B</pacvue-radio>
</template>
<script setup>
  import { ref } from 'vue'
  const radio1 = ref('selected and disabled')
</script>
```

### 你可以让单选框看起来像一个按钮一样。

```vue
<template>
  <div style="margin-top: 20px;">
    <pacvue-radio-group v-model="radio3">
      <pacvue-radio-button label="New York" />
      <pacvue-radio-button label="Washington" />
      <pacvue-radio-button label="Los Angeles" />
      <pacvue-radio-button label="Chicago" />
    </pacvue-radio-group>
  </div>
  <div style="margin-top: 20px;">
    <pacvue-radio-group v-model="radio4">
      <pacvue-radio-button label="New York" />
      <pacvue-radio-button label="Washington" disabled />
      <pacvue-radio-button label="Los Angeles" />
      <pacvue-radio-button label="Chicago" />
    </pacvue-radio-group>
  </div>
</template>
<script setup>
  import { ref } from 'vue'
  const radio3 = ref('New York')
  const radio4 = ref('New York')
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| model-value / v-model | 选中项绑定值 | string / number / boolean | -- |
| disabled | 是否禁用单选框。是否禁用组件，禁用后无法进行交互 | boolean | false |
| name | 原生 name 属性 | string | -- |
| id | 原生 id 属性 | string | -- |
| disableLabel | 是否禁用label的事件 | boolean | false |
| model-value / v-model | 选中项绑定值 | string / number / boolean | -- |
| disabled | 是否禁用单选框。是否禁用组件，禁用后无法进行交互 | boolean | false |
| label | 单选框的值 | string / number / boolean | -- |
| name | 原生 name 属性 | string | -- |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/radio.html#radio-%E5%B1%9E%E6%80%A7)

