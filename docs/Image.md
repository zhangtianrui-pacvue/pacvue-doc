---
component: Image
category: data
tags: [图片, 媒体, 展示]
aliases: [Image, 图片]
version: 1.0.0
description: "PacvueImage组件的简单应用"
---

# Image 组件文档

> PacvueImage组件的简单应用

**分类**: data | **标签**: 图片、媒体、展示

## 使用示例

### 示例：Image1

```vue
<template>
  <div>
    <PacvueImage style="width: 100px; height: 100px" :src="url" :zoom-rate="1.2" fit="cover" :previewSrcList="srcList" :previewType="'simple'"></PacvueImage>
  </div>
</template>

<script setup>
  import { PacvueImage } from '@pacvue/element-plus'
  import { ref } from 'vue'

  const srcList = [
    'https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg',
    'https://fuss10.elemecdn.com/1/34/19aa98b1fcb2781c4fba33d850549jpeg.jpeg',
    'https://fuss10.elemecdn.com/0/6f/e35ff375812e6b0020b6b4e8f9583jpeg.jpeg',
    'https://fuss10.elemecdn.com/9/bb/e27858e973f5d7d3904835f46abbdjpeg.jpeg',
    'https://fuss10.elemecdn.com/d/e6/c4d93a3805b3ce3f323f7974e6f78jpeg.jpeg',
    'https://fuss10.elemecdn.com/3/28/bbf893f792f03a54408b3b7a7ebf0jpeg.jpeg',
    'https://fuss10.elemecdn.com/2/11/6535bcfb26e4c79b48ddde44f4b6fjpeg.jpeg'
  ]
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| previewType | 预览的类型，simple(简单模式)或者default(element组件的样式) | String | simple |
| zIndex | 需要指定预览视图的层级 | Number | -- |
| infinite | 是否循环展示 | Boolean | true |
| previewSrcList | 预览的图片列表 | Array<String> | [] |
| hideOnClickModal | 是否点击mask隐藏图片预览 | Boolean | true |
| initialIndex | 初始预览的图片下标，默认第一张 | Number | 0 |
| closeOnPressEscape | 是否按esc关闭预览窗口 | Boolean | true |
| previewTeleported | 预览图是否添加body上 | Boolean | true |
| customDownload | 自定义的下载功能 | Function({ href }) | -- |
| hasDownLoad | 是否有下载功能 | Boolean | true |
| src | 当前显示的图片路径 | String | -- |
| type | 预览的类型，simple(简单模式)或者default(element组件的样式) | String | simple |
| showCustomLoading | 是否显示自定义loading，会在图片加载完成后，关闭 | Boolean | false |
| loadingBgColor | 自定义加载的mask背景色 | String | hsla(0deg, 0%, 100%, 0.4) |
| placeholderImg | 占位图片 | String | https://cdn-pacvue-public-doc.pacvue.com/oss/pacvue-cdn/vue3/Image+placeholder.svg |
| errorImg | 图片加载错误的图片 | String | https://cdn-pacvue-public-doc.pacvue.com/oss/pacvue-cdn/vue3/Image+placeholder.svg |
| label | 指定节点标签为节点对象的某个属性值 | String | -- |
| value | 指定节点value为节点对象的某个属性值 | String | -- |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| close | 关闭事件 | Function() |
| swith | 切换图片时回调事件 | Function(index) |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/image.html)

