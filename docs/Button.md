---
component: Button
category: basic
tags: [按钮, 基础, 交互]
aliases: [Button, 按钮]
version: 1.0.0
description: "不同尺寸按钮用法"
---

# Button 组件文档

> 不同尺寸按钮用法

**分类**: basic | **标签**: 按钮、基础、交互

## 使用示例

### 按钮分为中号和小号，分别为 default small 最小宽高：default：88*36px

```vue
<template>
  <p class="mb-4">default</p>
  <el-row class="mb-4">
    <pacvue-button >button1</pacvue-button>
    <pacvue-button type="primary">button2</pacvue-button>
    <pacvue-button type="primary" plain>button3</pacvue-button>
    <pacvue-button type="primary" link>button4</pacvue-button>
    <pacvue-button type="success">button5</pacvue-button>
    <pacvue-button type="info">button6</pacvue-button>
    <pacvue-button :icon="Search" circle></pacvue-button>
    <pacvue-button type="primary" :icon="Search" circle></pacvue-button>
    <pacvue-button type="primary" plain :icon="Search" circle></pacvue-button>
    <pacvue-button type="primary" link :icon="Search" circle></pacvue-button>
  </el-row>
  <el-row class="mb-4">
    <pacvue-button type="warning">button7</pacvue-button>
    <pacvue-button type="danger">button8</pacvue-button>
    <pacvue-button type="success" plain>button9</pacvue-button>
    <pacvue-button type="info" plain>button10</pacvue-button>
    <pacvue-button type="warning" plain>button11</pacvue-button>
    <pacvue-button type="danger" plain>button12</pacvue-button>
  </el-row>
  <p class="mb-4">small</p>
  <el-row class="mb-4">
    <pacvue-button size="small">button13</pacvue-button>
    <pacvue-button size="small" type="primary">button14</pacvue-button>
    <pacvue-button size="small" type="primary" plain>button15</pacvue-button>
    <pacvue-button size="small" type="primary" link>button16</pacvue-button>
    <pacvue-button size="small" type="success">button17</pacvue-button>
    <pacvue-button size="small" type="info">button18</pacvue-button>
  </el-row>
  <el-row class="mb-4">
    <pacvue-button size="small" type="warning">button19</pacvue-button>
    <pacvue-button size="small" type="danger">button20</pacvue-button>
    <pacvue-button size="small" type="success" plain>button21</pacvue-button>
    <pacvue-button size="small" type="info" plain>button22</pacvue-button>
    <pacvue-button size="small" type="warning" plain>button23</pacvue-button>
    <pacvue-button size="small" type="danger" plain>button24</pacvue-button>
  </el-row>
</template>
<script setup>
  import { Check, Delete, Edit, Message, Search, Star } from '@pacvue/element-plus'
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### 你可以使用 disabled 属性来定义按钮是否被禁用。 使用 disabled

```vue
<template>
  <el-row class="mb-4">
    <pacvue-button type="primary" disabled>button25</pacvue-button>
    <pacvue-button type="primary" :icon="Search" circle disabled></pacvue-button>
    <pacvue-button type="primary" plain disabled>button26</pacvue-button>
    <pacvue-button type="primary" plain :icon="Search" circle disabled></pacvue-button>
    <pacvue-button type="primary" link disabled>button27</pacvue-button>
    <pacvue-button type="primary" link :icon="Search" circle disabled></pacvue-button>
    <pacvue-button disabled>button28</pacvue-button>
    <pacvue-button :icon="Search" circle disabled></pacvue-button>
    <pacvue-button type="success" plain disabled>button29</pacvue-button>
    <pacvue-button type="success" plain :icon="Search" circle disabled></pacvue-button>
  </el-row>
  <el-row class="mb-4">
    <pacvue-button type="info" disabled>button30</pacvue-button>
    <pacvue-button type="info" :icon="Search" circle disabled></pacvue-button>
    <pacvue-button type="warning" disabled>button31</pacvue-button>
    <pacvue-button type="warning" :icon="Search" circle disabled></pacvue-button>
    <pacvue-button type="danger" disabled>button32</pacvue-button>
    <pacvue-button type="danger" :icon="Search" circle disabled></pacvue-button>
    <pacvue-button type="info" plain disabled>button33</pacvue-button>
    <pacvue-button type="info" plain :icon="Search" circle disabled></pacvue-button>
    <pacvue-button type="warning" plain disabled>button34</pacvue-button>
    <pacvue-button type="warning" plain :icon="Search" circle disabled></pacvue-button>
  </el-row>
  <el-row class="mb-4">
    <pacvue-button type="danger" plain disabled>button35</pacvue-button>
    <pacvue-button type="danger" plain :icon="Search" circle disabled></pacvue-button>
  </el-row>
</template>

<script setup>
  import { Check, Delete, Edit, Message, Search, Star } from '@pacvue/element-plus'
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| size | 配置按钮默认的尺寸，可选项有 default small，这两种模式都有最小宽高限制，最小宽高：default：88*36px，small：72*32px | String | default |
| type | 类型: primary \| success \| info \| warning \| danger | String | -- |
| icon | 图标组件 | string / Component | -- |
| plain | 是否为朴素按钮 | Boolean | false |
| link | 是否为链接按钮 | Boolean | false |
| throttle | 开启按钮点击事件节流触发，用于设置节流的时间。 | Number | -- |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/button.html)

