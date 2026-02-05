---
component: Skeleton
category: data
tags: [骨架屏, 加载, 占位]
aliases: [Skeleton, 骨架屏]
version: 1.0.0
description: "Skeleton"
---

# Skeleton 组件文档

> Skeleton

**分类**: data | **标签**: 骨架屏、加载、占位

## 使用示例

### 表单

```vue
<template>
    <div style="display: flex;justify-content:space-between">
        <div style="width: 450px;">
            <pacvue-skeleton type="form" :hasTitle="true" rows="5" formType="1"></pacvue-skeleton>
        </div>
        <div style="width: 450px;">
            <pacvue-skeleton type="form" rows="6" formType="2"></pacvue-skeleton>
        </div>
    </div>
</template>
```

### 列表

```vue
<template>
    <div style="display: flex;justify-content:space-between">
        <div style="width:450px">
            <pacvue-skeleton type="list" :hasTitle="true" titleRow="2" rows="3" :hasImg="true" imgSize="sm"></pacvue-skeleton>
        </div>
        <div style="width:450px">
            <pacvue-skeleton type="list" :hasTitle="false" :hasImg="true" imgSize="lg"></pacvue-skeleton>
        </div>
    </div>
</template>
```

### Panel

```vue
<template>
  <div style="display: flex; justify-content: space-between">
    <div style="border-radius: 6px; padding: 12px; height: 120px; width: 200px">
      <pacvue-skeleton type="skeleton" skeletonType="panel"></pacvue-skeleton>
    </div>
    <div style="border-radius: 6px; padding: 12px; height: 166px; width: 400px">
      <pacvue-skeleton type="skeleton" skeletonType="proIndex"></pacvue-skeleton>
    </div>
  </div>
</template>
```

### Widget

```vue
<template>
  <div style="display: flex; justify-content: space-between">
    <div style="width: 450px; border-radius: 6px; padding: 12px; height: 300px">
      <pacvue-skeleton type="skeleton" skeletonType="widget" :skeletonOptions="{ loading: true, animated: true }"></pacvue-skeleton>
    </div>
  </div>
</template>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| type | 骨架屏类型 form / list / skeleton, form:用于表单, list:用于文字,skeleton继承了el-skeleton组件，列表，图片 | String | list |
| skeletonType | type为skeleton生效，为widget/panel proIndex | String | panel |
| skeletonOptions | el-skeleton组件中配置项，参考el-skeleton组件配置 | Object | -- |
| formType | 表单骨架屏的类型 1 / 2 ,type:form 时生效, 1:一行一个, 2:一行2个 | [String, Number] | 2 |
| hasTitle | 是否需要标题位置的骨架屏 | Boolean | false |
| titleRow | 标题行数，type:list,hasTitle:true时生效 | [String, Number] | 2 |
| rows | 文字/表单行数 | [String, Number] | 3 |
| hasImg | 是否需要图片位置的骨架屏，type:list时生效 | Boolean | false |
| imgSize | 图片大小，type:list,hasImg:true时生效 sm / lg | Boolean | sm |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/skeleton.html)

