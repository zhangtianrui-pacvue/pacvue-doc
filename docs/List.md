---
component: List
category: data
tags: [列表, 数据展示]
aliases: [List, 列表]
version: 1.0.0
description: "List 列表"
---

# List 组件文档

> List 列表

**分类**: data | **标签**: 列表、数据展示

## 使用示例

### PacvueList 组件分为有边框和无边框两种样式

```vue
<template>
  <PacvueList :data="listdata">
    <template #left="item">
      <el-icon>
        <Burger />
      </el-icon>
    </template>
    <template #right="item">
      <el-icon>
        <ArrowRightBold />
      </el-icon>
    </template>
  </PacvueList>
  <hr style="margin: 30px 0" />
  <PacvueList :data="listdata" :border="false">
    <template #left="item">
      <el-icon>
        <Burger />
      </el-icon>
    </template>
    <template #right="item">
      <el-icon>
        <ArrowRightBold />
      </el-icon>
    </template>
  </PacvueList>
</template>
<script setup>
  const listdata = [
    { title: '11111', text: '22222', mark: 'mark1' },
    { title: '', text: '22222', mark: 'mark2' },
    { title: '11111', text: '', mark: 'mark3' },
    { title: '11111', text: '', mark: '' }
  ]
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| data | 需要展示的列表数组，数组中每一个索引位置为一个 { title, text, mark }, 对象，title 为列的标题，text 为列的正文，mark 为列的右侧徽标文字 | Array | -- |
| border | 判断组件是否需要显示边框 | Boolean | true |
| options | data 中的列数据如果需要自定义 title,、text、mark 的接收字段，则使用此项进行配置 | Object | `{ title: 'title', text: 'text', mark: 'mark' }` |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| left | 单列最左侧样式插槽 | -- |
| right | 单列最右侧样式插槽 | -- |

