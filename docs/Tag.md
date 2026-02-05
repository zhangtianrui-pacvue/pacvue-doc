---
component: Tag
category: data
tags: [标签, 标记, 分类]
aliases: [Tag, 标签]
version: 1.0.0
description: "Tag"
---

# Tag 组件文档

> Tag

**分类**: data | **标签**: 标签、标记、分类

## 使用示例

### 示例：index

```vue
<template>
  <p>不同 mode</p>
  <pacvue-tag>mode sm</pacvue-tag>
  <pacvue-tag mode="bg">mode bg</pacvue-tag>

  <p>无边框</p>
  <pacvue-tag noBorder>noBorder</pacvue-tag>

  <p>显示关闭按钮</p>
  <pacvue-tag closable>closable</pacvue-tag>

  <p>不同 type</p>
  <pacvue-tag type="success">success</pacvue-tag>
  <pacvue-tag type="info">info</pacvue-tag>
  <pacvue-tag type="warning">warning</pacvue-tag>
  <pacvue-tag type="danger">danger</pacvue-tag>
  <pacvue-tag type="custom1" mode="bg" noBorder>custom1</pacvue-tag>
  <pacvue-tag type="custom2" mode="bg" noBorder>custom2</pacvue-tag>
  <pacvue-tag type="custom3" mode="bg" noBorder>custom3</pacvue-tag>
</template>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| mode | tag 的两种样式模式，分为 sm (height: 22px) 和 bg (height: 28px)。 | "sm" \| "bg" | sm |
| noBorder | tag 是否显示边框 | boolean | true |
| type | tag 类型。组件类型或模式 | "success" \| "info" \| "warning" \| "danger" \| "custom1" \| "custom2" \| "custom3" | -- |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/tag.html)

