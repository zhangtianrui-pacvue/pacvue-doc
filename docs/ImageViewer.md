---
component: ImageViewer
category: data
tags: [图片查看器, 预览, 放大]
aliases: [ImageViewer, 图片查看]
version: 1.0.0
description: "PacvueImageViewer组件的简单应用"
---

# ImageViewer 组件文档

> PacvueImageViewer组件的简单应用

**分类**: data | **标签**: 图片查看器、预览、放大

## 使用示例

### 示例：Image Viewer1

```vue
<template>
  <div>
    <PacvueImage style="width: 100px; height: 100px" :src="url" fit="cover" @click="toggle"></PacvueImage>
    <PacvueImageViewer :urlList="srcList" v-if="isShowPreview" @close="closeImageViewer"></PacvueImageViewer>
  </div>
</template>

<script setup>
  import { PacvueImageViewer } from '@pacvue/element-plus'
  import { ref } from 'vue'
  const url = 'https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg'
  const isShowPreview = ref(false)
  var itemList = ref([
    {
      id: 'enabled',
      name: 'Enabled'
    },
    {
      id: 'paused',
      name: 'Paused'
    },
    {
      id: 'archived',
      name: 'Archived'
    }
  ])
  const srcList = [
    'https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg',
    'https://fuss10.elemecdn.com/1/34/19aa98b1fcb2781c4fba33d850549jpeg.jpeg',
    'https://fuss10.elemecdn.com/0/6f/e35ff375812e6b0020b6b4e8f9583jpeg.jpeg',
    'https://fuss10.elemecdn.com/9/bb/e27858e973f5d7d3904835f46abbdjpeg.jpeg',
    'https://fuss10.elemecdn.com/d/e6/c4d93a3805b3ce3f323f7974e6f78jpeg.jpeg',
    'https://fuss10.elemecdn.com/3/28/bbf893f792f03a54408b3b7a7ebf0jpeg.jpeg',
    'https://fuss10.elemecdn.com/2/11/6535bcfb26e4c79b48ddde44f4b6fjpeg.jpeg'
  ]
  var toggle = () => {
    isShowPreview.value = !isShowPreview.value
  }
  var closeImageViewer = () => {
    isShowPreview.value = false
  }
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| urlList | 预览的图片列表 | Array<String> | [] |
| zIndex | 需要指定预览视图的层级 | Number | -- |
| initialIndex | 初始预览的图片下标，默认第一张 | Number | 0 |
| infinite | 是否循环展示 | Boolean | true |
| hideOnClickModal | 是否点击mask隐藏 | Boolean | true |
| teleported | 是否添加body上。是否将弹出层添加到 body 中，避免定位问题 | Boolean | true |
| closeOnPressEscape | 是否按esc关闭预览窗口 | Boolean | true |
| type | 预览的类型，simple(简单模式)或者default(element组件的样式) | String | simple |
| hasDownLoad | 是否有下载功能 | Boolean | true |
| customDownload | 自定义的下载功能 | Function({ href }) | -- |
| hasTogglePage | 是否有切换页码功能 | Boolean | true |
| label | 指定节点标签为节点对象的某个属性值 | String | -- |
| value | 指定节点value为节点对象的某个属性值 | String | -- |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| close | 关闭事件 | Function() |
| swith | 切换图片时回调事件 | Function(index) |

