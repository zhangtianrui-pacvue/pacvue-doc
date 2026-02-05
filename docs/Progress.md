---
component: Progress
category: data
tags: [进度条, 进度, 百分比]
aliases: [Progress, 进度]
version: 1.0.0
description: "Progress"
---

# Progress 组件文档

> Progress

**分类**: data | **标签**: 进度条、进度、百分比

## 使用示例

### Progress

```vue
<template>
    <div style="width: 400px">
        <pacvue-progress :percentage="50" :show-text="false"></pacvue-progress>
        <br/>
        <pacvue-progress :text-inside="true" :percentage="25" pacColor="purple"></pacvue-progress>
        <br/>
        <pacvue-progress :text-inside="true" :percentage="35" pacColor="gray"></pacvue-progress>
        <br/>
        <pacvue-progress :text-inside="true" :percentage="45" pacColor="green"></pacvue-progress>
        <br/>
        <pacvue-progress :text-inside="true" :percentage="55" pacColor="red"></pacvue-progress>
        <br/>
        <pacvue-progress :text-inside="true" :percentage="65" pacColor="orange"></pacvue-progress>
        <br/>
        <pacvue-progress :text-inside="true" :percentage="75" pacColor="blue"></pacvue-progress>
        <br/>
    </div>
</template>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| pacColor | 进度条颜色 purple / gray / green / red / orange / blue | String | orange |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/progress.html)

