---
component: PacvueTagGroup
category: data
tags: [标签组, 分组, 展示]
aliases: [PacvueTagGroup]
version: 1.0.0
description: "PacvueTagGroup 基础用法"
---

# PacvueTagGroup 组件文档

> PacvueTagGroup 基础用法

**分类**: data | **标签**: 标签组、分组、展示

## 使用示例

### 示例：index

```vue
<template>
  <PacvueTagGroup v-model="newList" placeholder="请输入" style="width: 50%;"></PacvueTagGroup>
</template>
<script setup>
  import { ref } from 'vue'
  const newList = ref([])
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| modelValue | 存储tag数据的的数组。组件绑定值，配合 v-model 使用 | Array | -- |
| placeholder | 输入框占位文本。占位提示文字，在无输入时显示 | string | -- |
| unique | 添加tag时是否需要去重 | boolean | false |

