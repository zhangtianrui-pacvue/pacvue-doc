---
component: Tooltip
category: feedback
tags: [文字提示, 悬浮, 提示]
aliases: [Tooltip, 提示]
version: 1.0.0
description: "Tooltip"
---

# Tooltip 组件文档

> Tooltip

**分类**: feedback | **标签**: 文字提示、悬浮、提示

## 使用示例

### Tooltip组件用法

```vue
<template>
  <PacvueButton @click="click1">取消 tooltip 的全局延时参数</PacvueButton>
  <PacvueButton @click="click2">设置 tooltip 的全局延时参数为 1s</PacvueButton>
  <PacvueTooltip class="box-item" placement="top" :fixWidth="false">
    <template #content>
      Top Left prompts infoTop Left prompts infoTop Left prompts infoTop Left prompts infoTop Left prompts infoTop Left
      prompts infoTop Left prompts infoTop Left prompts info
    </template>
    <el-button>top</el-button>
  </PacvueTooltip>
  <PacvueTooltip class="box-item" effect="dark" content="Left Center prompts info" placement="left">
    <template #content>
      Top Left prompts infoTop Left prompts infoTop Left prompts infoTop Left prompts infoTop Left prompts infoTop Left
      prompts infoTop Left prompts infoTop Left prompts info
    </template>
    <el-button>left</el-button>
  </PacvueTooltip>
  <PacvueTooltip class="box-item" effect="dark" content="Right Center prompts info" placement="right">
    <el-button>right</el-button>
  </PacvueTooltip>
  <PacvueTooltip class="box-item" effect="dark" content="Bottom Center prompts info" placement="bottom">
    <el-button>bottom</el-button>
  </PacvueTooltip>
</template>
<script setup>
  import { tooltipShowAfter } from '@pacvue/element-plus'
  const click1 = () => {
    tooltipShowAfter()
  }
  const click2 = () => {
    tooltipShowAfter(1000)
  }
</script>
```

### v-pacvueTooltip指令用法

```vue
<template>
  <el-button
    v-pacvueTooltip.enter="
    'Top Left prompts infoTop Left prompts infoTop Left prompts infoTop Left prompts infoTop Left prompts infoTop Left prompts infoTop Left prompts infoTop Left prompts info'
  "
  >
    top
  </el-button>
  <el-button
    v-pacvueTooltip:right.enter="
              '1231Top Left prompts infoTop Left prompts infoTop Left prompts infoTop Left prompts infoTop Left prompts infoTop Left prompts infoTop Left prompts infoTop Left prompts info'
            "
  >
    right
  </el-button>
</template>
<script setup></script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| effect | Tooltip 主题，内置了 dark / light 两种 | string | dark |
| fixWidth | 是否需要固定240px宽度 | Boolean | true |
| asyncBeforeShow | 在异步之前执行的函数 | Function | -- |
| v-pacvueTooltip:placement | 指令用法，其中placement为'top' \| 'bottom' \| 'left'  \| 'right'  | String | -- |
| data-show-after | 在触发后多久显示内容，单位毫秒 | Number | 0 |
| data-hide-after | 延迟关闭，单位毫秒 | Number | 200 |
| overflowShow | 显示的文本内容出现省略号时才开启tooltip | Boolean | -- |
| specialOverflowShow | 指定特定的文本元素为.ellipsis-box中的文本内容出现省略号时才开启tooltip | Boolean | -- |
| self | 没有指定tooltip 的显示内容，默认使用自身文本内容 | Boolean | -- |
| appendToParent | 是否添加在父元素上 | Boolean | -- |
| enter | 是否是mouseenter触发tooltip，默认是mouseover | Boolean | -- |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/tooltip.html)

