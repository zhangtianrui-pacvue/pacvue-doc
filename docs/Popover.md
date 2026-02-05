---
component: Popover
category: feedback
tags: [气泡框, 弹出, 提示]
aliases: [Popover, 气泡]
version: 1.0.0
description: "Popover 气泡卡片"
---

# Popover 组件文档

> Popover 气泡卡片

**分类**: feedback | **标签**: 气泡框、弹出、提示

## 使用示例

### Popover customTodo 属性用于定制弹窗底部自定义文字样式，点击文字可触发

```vue
<template>
  <PacvuePopover
    placement="top-start"
    title="Title"
    trigger="hover"
    content="this is content, this is content, this is content this is content, this is content, this is content this is content, this is content, this is content"
    :auto-close="0"
    :customTodo="'Read More'"
    @customTodoClick="customTodoClick"
  >
    <template #icon>
      <el-icon><ElemeFilled /></el-icon>
    </template>
    <template #reference>
      <pacvue-button>Hover to activate</pacvue-button>
    </template>
  </PacvuePopover>
</template>
<script setup>
  import { h } from 'vue'
  import { ElemeFilled, ElMessage } from '@pacvue/element-plus'
  const customTodoClick = () => {
    ElMessage({
      message: h('p', null, 'Read More on click !'),
      type: 'success'
    })
  }
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| trigger | 触发方式 | click/focus/hover/contextmenu | hover |
| title | 标题 | String | -- |
| content | 显示的内容，也可以通过写入默认 slot 修改显示内容 | String | -- |
| auto-close | tooltip 出现后自动隐藏延时，单位毫秒 | number | 0 |
| customTodo | 弹出框底部自定义文字内容 | String | -- |
| width | 设置弹出框的 width 属性，注意：弹出框默认有 max-width: 420px; 如需自定义请自行覆盖样式 | String \| Number | max-content |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| customTodoClick | 点击底部自定义文字触发事件 | -- |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| icon | 弹窗左侧图标插槽 | -- |
| reference | 触发 Popover 显示的 HTML 元素 | -- |
| default | Popover 内嵌 HTML 文本 | -- |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/popover.html)

