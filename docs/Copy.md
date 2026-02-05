---
component: Copy
category: utility
tags: [复制, 剪贴板, 工具]
aliases: [Copy, 复制]
version: 1.0.0
description: "简单使用（只能复制文本内容）"
---

# Copy 组件文档

> 简单使用（只能复制文本内容）

**分类**: utility | **标签**: 复制、剪贴板、工具

## 使用示例

### 通过默认插槽在页面中使用

```vue
<template>
  <PacvueCopy>这个是要复制的内容。</PacvueCopy>
</template>

<script setup>
  import { PacvueCopy } from '@pacvue/element-plus'
</script>
```

### 通过属性copyContent使用，优先级比defualt插槽高

```vue
<template>
  <PacvueCopy :copyContent="'这个是通过属性配置的复制内容'">这个是要复制的内容。</PacvueCopy>
</template>

<script setup>
  import { PacvueCopy } from '@pacvue/element-plus'
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| copyIconSize | 复制图标的大小 | Number | 20 |
| copyIconColor | 复制图标的颜色 | String | #b2b2b8 |
| copyIconTipDisabled | 复制图标是否禁用 | Boolean | true |
| showCopyIcon | 是否显示复制图标 | Boolean | true |
| copyContent | 复制的内容，如果没有设置，则默认取插槽default中的文本内容 | Number\|String | -- |
| showType | 复制图标显示类型，visbile是常显示，hover是鼠标hover上去才显示 | visible\|hover | visible |

