---
component: InputRange
category: form
tags: [范围输入, 表单, 数值范围]
aliases: [InputRange, 范围输入]
version: 1.0.0
description: "PacvueInputRange 输入框"
---

# InputRange 组件文档

> PacvueInputRange 输入框

**分类**: form | **标签**: 范围输入、表单、数值范围

## 使用示例

### 基础用法 通过 width 属性指定 input 组件宽度 默认宽度为256px -->

```vue
<template>
  <PacvueInputRange
    v-model="rangeVal"
    :labelInner="'Label'"
    :firstPlaceHolder="'Please Input Start'"
    :secondPlaceHolder="'Please Input End'"
    clearable
    :labelTip="'Tip'"
    :seperate="'至'"
    style="width: 400px"
    mode="standard"
  >
    <template #prefix>
      <div class="pacvue-select-wrpper">
        <PacvueSelect v-model="selectVal" :data="selectOptions" :collapseTags="false" type="single" style="width: 60px" :height="'34px'"></PacvueSelect>
      </div>
    </template>
  </PacvueInputRange>
</template>
<script setup>
  import { ref } from 'vue'
  var rangeVal = ref([1, 5])
  var selectVal = ref('A')
  var selectOptions = [
    {
      label: 'A',
      value: 'A'
    },
    {
      label: 'B',
      value: 'B'
    }
  ]
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| v-model | 双向绑定值。双向绑定值，用于获取和设置组件的当前值 | Array | [] |
| labelInner | label的名称 | String | —— |
| firstPlaceHolder | min值的placeholder | string | min |
| secondPlaceHolder | max值的placeholder | string | -- |
| seperate | 范围输入框的分隔符 | string | ~ |
| height | 高度。组件高度，支持像素值或百分比 | string | 36px |
| clearable | 是否有clear功能。是否显示清除按钮，点击可清空当前值 | boolean | false |
| labelTip | label的提示信息 | String | -- |
| tip | 范围输入框的提示信息 | String | -- |
| mode | 范围输入框的模式，可选值为default以及standard | String | standard |
| inputType | 输入框的类型,text或者number | String | text |
| digitCount | 保留的小数位数(inputType为number时才生效) | Number | -- |
| hasBorder | 是否显示边框 | boolean | true |
| isMulitpleInput | 是否是多输入框 | boolean | true |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| change | 绑定值变化触发事件 | Function(value) |
| focus-change | 输入框中焦点变化 | Function(isFocus) |
| clear | 清空范围输入框 | Function() |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| prefix | 输入框前缀 | -- |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/input.html#input-%E5%B1%9E%E6%80%A7)

