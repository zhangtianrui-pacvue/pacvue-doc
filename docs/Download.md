---
component: Download
category: utility
tags: [下载, 文件, 导出]
aliases: [Download, 下载]
version: 1.0.0
description: "本地下载同步用法"
---

# Download 组件文档

> 本地下载同步用法

**分类**: utility | **标签**: 下载、文件、导出

## 使用示例

### 示例：Download1

```vue
<template>
  <PacvueDownload tip="test" :size="24" :disabled="false"></PacvueDownload>
</template>
```

### 通过disabled控制是否禁用

```vue
<template>
  <PacvueDownload tip="test" :size="24" :disabled="true"></PacvueDownload>
</template>
```

### downloadType: Button | Icon | Text

```vue
<template>
  <div style="display: flex; align-items: center">
    <div>
      <PacvueDownload tip="Button" :size="24" downloadType="Button">
        <template #default>Button</template>
      </PacvueDownload>
    </div>

    <div style="margin-left: 24px">
      <PacvueDownload tip="Button-icon" :size="24" downloadType="Button">
        <template #icon>
          <el-icon :size="24" :color="'#66666c'"><PacvueIconDataDownload /></el-icon>
        </template>
      </PacvueDownload>
    </div>

    <div style="margin-left: 24px">
      <PacvueDownload tip="Text" :size="24" downloadType="Text">
        <template #default>Text</template>
      </PacvueDownload>
    </div>
  </div>
</template>
```

### 通过属性 isAsync = true 开启异步下载

```vue
<template>
  <PacvueDownload tip="test" :size="24" :disabled="false" :isAsync="true"></PacvueDownload>
</template>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| toEl | 异步下载的时候下载图标动画的目标对象 | String\|Dom | -- |
| size | 图标的大小。组件尺寸大小，可选 large/default/small | Number | 24 |
| color | 图标的颜色 | String | -- |
| isAsync | 是否是异步下载 | Boolean | false |
| disabled | 是否禁用。是否禁用组件，禁用后无法进行交互 | Boolean | false |
| tip | 提示信息 | String | -- |
| downloadCenterUrl | 跳转到下载中心的地址url | String | /Download |
| query | 下载时查询条件，异步下载的查询条件，如果变化则会重置下载状态 | Object | -- |
| throld | 异步下载时的间隔时间 | Number | 60 |
| isWithPauseTrigger | 是否开启暂停触发事件 | Boolean | false |
| fromEl | 异步下载的时候下载图标动画的开始对象 | String\|Dom | 默认自身 |
| downloadType | 下载组件的类型,为Button\|Icon\|Text | String | Icon |
| hideDefaultSlotWithLoading | 是否出现loading时，隐藏默认插槽（目前只针对downloadType为Button时） | String | false |
| boforeRouteEnter | 跳转路由之前的钩子 | Function({path}) | -- |
| loadingGap | loading图标与文案之间的间隔,只针对downloadType为Text时候生效 | Number | 4 |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| default | 自定义默认内容(只有downType为Button,Text生效) | -- |
| loading | 自定义加载中组件(只有downType为Button,Text生效) | -- |
| icon | 图标Button的图标插槽(只有downType为Button) | -- |

