---
component: Ellipsisbox
category: data
tags: [文本省略, 溢出, 展示]
aliases: [Ellipsisbox, 省略]
version: 1.0.0
description: "PacvueEllipsisbox基础用法"
---

# Ellipsisbox 组件文档

> PacvueEllipsisbox基础用法

**分类**: data | **标签**: 文本省略、溢出、展示

## 使用示例

### 使用lineClamp控制最多显示几行

```vue
<template>
  <PacvueEllipsisbox style="width: 200px" :lineClamp="3" :isFitContent="false" isTipDefulatSelfContent>
    这个是测试这个是测试这个是测试这个是测试这个是测试这个是测试这个是测试这个是测试这个是测试这个是测试这个是测试这个是测试这个是测试这个是测试
    <template #aside>Aside</template>
    <template #suffix>Suffix</template>
  </PacvueEllipsisbox>
</template>

<script lang="jsx"></script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| isFitContent | 是否按内容自适应宽度 | Boolean | true |
| tip | 消息提示信息 | String | -- |
| isTipDefulatSelfContent | 是否体魄默认使用自身的内容 | Boolean | false |
| isTwoRow | 最多两行显示省略号 | Boolean | true |
| lineClamp | 最多显示几行出现省略号,优先级高于isTwoRow | Number | -- |
| labelStyle | 显示的标签内容样式 | Object | {} |
| labelClass | 显示的标签内容类名 | Object\|Array | [] |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| labelClick | 点击标签触发的事件回调 | Function |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| prefix | 显示内容前缀内容 | -- |
| default | 显示内容插槽 | -- |
| aside | 显示内容的辅助内容 | -- |
| suffix | 显示内容尾部内容 | -- |

