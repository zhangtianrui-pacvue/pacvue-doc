---
component: PacvueVirtualList
category: data
tags: [虚拟列表, 大数据, 滚动]
aliases: [PacvueVirtualList]
version: 1.0.0
description: "PacvueVirtualList基础用法"
---

# PacvueVirtualList 组件文档

> PacvueVirtualList基础用法

**分类**: data | **标签**: 虚拟列表、大数据、滚动

## 使用示例

### 虚拟滚动列表

```vue
<template>
       <div style="width: 300px">
          <pacvue-virtual-list :data-sources="virtualListData" :estimate-size="32" :keeps="50" :props-config="propsConfig" :maxHeight="'300px'">
            <template #default="{ label, value, index }">
              <div class="pacvue-virtual-list-item" style="line-height: 32px">
                < <div>Label:{{ label }} Value:{{ value }} Index:{{ index }}</div>
              </div>
            </template>
          </pacvue-virtual-list>
        </div>
</template>
<script setup>
import { ref } from 'vue'
const propsConfig = {
  value: 'id',
  label: 'name'
}
const virtualListData = ref(Array.from({ length: 100000 }, (_, i) => ({ id: i, name: 'item' + i })))
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| dataKey | 数据源中的唯一值 | String\|Function | -- |
| dataSources | 数据源 | Array | -- |
| estimateSize | 每个项目的预估尺寸，越接近平均尺寸，滚动条长度看起来越准确 | Number | 32 |
| keeps | 您希望虚拟列表在真实 dom 中继续渲染多少个项目 | Number | 30 |
| extraProps | 额外的属性。注意:index和source,value,label均被内部占用 | Object | -- |
| maxHeight | 最大高度 | String | 300px |
| propsConfig | 配置项 | Object | {value: "value", label: "label"} |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| default | 显示内容插槽,slotScopes 包含 index,source,label,value以及extraProps | -- |

