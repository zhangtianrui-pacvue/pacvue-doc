---
component: InputTag
category: form
tags: [标签输入, 表单, 多值输入]
aliases: [InputTag, 标签输入]
version: 1.0.0
description: "PacvueInputTag 输入框"
---

# InputTag 组件文档

> PacvueInputTag 输入框

**分类**: form | **标签**: 标签输入、表单、多值输入

## 使用示例

### 基础用法 通过 selectData 属性来指定显示的值

```vue
<template>
  <pacvue-input-tag :labelInner="'Input'" v-model:selectData="inputTagVal" style="width:300px"></pacvue-input-tag>
</template>
<script setup>
import {ref} from 'vue'
const inputTagVal = ref(['test1','test2','test-3','test-4','test-5','test-6','test-8'])
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| v-model:selectData | 双向绑定值 | Array | [] |
| labelInner | 显示的标签名 | String | -- |
| showPlaceholder | 是否显示placeholder | string | —— |
| placeholder | 提示信息。占位提示文字，在无输入时显示 | string | -- |
| propsConfig | 如果selectData是数组对象,配置选项 | Object | { value: 'value', label: 'label', children: 'children' } |
| clearable | 是否具有清除功能。是否显示清除按钮，点击可清空当前值 | Boolean | true |
| disabled | 是否禁用。是否禁用组件，禁用后无法进行交互 | Boolean | false |
| addLabel | Add的标签名称 | String | Add Tag |
| showTagClose | 是否具有Tag的close功能,注意受clearable影响 | Boolean | true |
| tip-text | 输入框提示文案。提示文案内容 | string | —— |
| state | 输入框状态 可选值:success/warning/error | string | —— |
| show-tip | 输入框是否显示提示。是否显示提示信息 | boolean | false |
| addLabelLayout | Add的标签的位置,auto/right | string | auto |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| change | 绑定值变化触发事件 | Function(value) |
| clear | 可清空的单选模式下用户点击清空按钮时触发 | Function() |
| add | 点击添加按钮事件 | Function() |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| tip-icon | 输入框提示图标 | svg |

