---
component: Breadcrumb
category: navigation
tags: [面包屑, 导航, 路径]
aliases: [Breadcrumb, 面包屑]
version: 1.0.0
description: "Breadcrumb 面包屑"
---

# Breadcrumb 组件文档

> Breadcrumb 面包屑

**分类**: navigation | **标签**: 面包屑、导航、路径

## 使用示例

### 通过 svg插槽指定一级图标

```vue
<template>
  <pacvue-breadcrumb>
    <template #primaryIcon>
      <House />
    </template>
    <pacvue-breadcrumb-item :to="{ path: '/' }">Competitive</pacvue-breadcrumb-item>
    <pacvue-breadcrumb-item>Manage SOV Keyword Tag</pacvue-breadcrumb-item>
  </pacvue-breadcrumb>
</template>
<script setup>
  import { DArrowRight, House } from '@pacvue/element-plus'
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| to | 路由跳转目标，同 vue-router 的 to 属性 | string/object | -- |
| separator | 分隔符，separator-icon 配置会使该属性失效。 | string | / |
| separator-icon | 图标分隔符的组件或组件名 | string/Component | ArrowRight |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| primaryIcon | 一级图标 | -- |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/breadcrumb.html#breadcrumb-%E5%B1%9E%E6%80%A7)

