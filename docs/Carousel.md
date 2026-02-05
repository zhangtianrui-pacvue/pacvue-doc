---
component: Carousel
category: data
tags: [走马灯, 轮播, 图片展示]
aliases: [Carousel, 轮播]
version: 1.0.0
description: "PacvueCarousel 走马灯"
---

# Carousel 组件文档

> PacvueCarousel 走马灯

**分类**: data | **标签**: 走马灯、轮播、图片展示

## 使用示例

### 在有限空间内，循环播放同一类型的图片、文字等内容

```vue
<template>
  <PacvueCarousel indicator-position="outside" style="width: 800px" :indicatorPosition="'none'" v-model="initialIndex">
    <template #default>
      <PacvueCarouselItem v-for="item in srcList" :key="item">
        <PacvueImage :src="item" style="border-radius: 6px"></PacvueImage>
      </PacvueCarouselItem>
    </template>

    <template #aside>
      <ul class="pacvue-image-list"
        style="display: flex; margin-left: 0px; padding: 0px; margin: 0px 40px; margin-top: 36px;padding-bottom: 2px;">
        <li v-for="(item, index) in srcList" @click="initialIndex = index" style="flex: 1"
          :style="{ 'margin-left': index > 0 ? '16px' : '0px', padding: '2px', cursor: 'pointer' }" :class="{
            'pacvue-img-active': initialIndex == index
          }">
          <PacvueImage :src="item" style="border-radius: 6px"></PacvueImage>
        </li>
      </ul>
    </template>
  </PacvueCarousel>
</template>

<script setup>
  import testImg from '@/assets/testImg.png'
  import { ref } from 'vue'
  const srcList = [
    'https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg',
    'https://fuss10.elemecdn.com/0/6f/e35ff375812e6b0020b6b4e8f9583jpeg.jpeg',
    'https://fuss10.elemecdn.com/9/bb/e27858e973f5d7d3904835f46abbdjpeg.jpeg',
    'https://fuss10.elemecdn.com/d/e6/c4d93a3805b3ce3f323f7974e6f78jpeg.jpeg',
    'https://fuss10.elemecdn.com/3/28/bbf893f792f03a54408b3b7a7ebf0jpeg.jpeg',
    'https://fuss10.elemecdn.com/2/11/6535bcfb26e4c79b48ddde44f4b6fjpeg.jpeg'
  ]
  var initialIndex = ref(0)
</script>
<style>
  .pacvue-img-active {
    outline: 2px solid var(--el-color-primary);
    border-radius: 6px;
  }
</style>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| modelValue | 幻灯片索引的双向绑定值,优先级高于initialIndex | Number | -- |
| height | carousel 的高度。组件高度，支持像素值或百分比 | String | -- |
| initialIndex | 初始状态激活的幻灯片的索引，从 0 开始 | Number | 0 |
| trigger | 指示器的触发方式,可选值为hover/click | String | hover |
| autoplay | 是否自动切换 | Boolean | false |
| interval | 自动切换的时间间隔，单位为毫秒 | Number | 3000 |
| indicatorPosition | 复指示器的位置,可选值为outside/none | String | visible |
| arrow | 切换箭头的显示时机,可选值为always/hover/never | String | always |
| type | carousel 的类型,可选值为card | String | -- |
| loop | 是否循环显示 | boolean | false |
| direction | 展示的方向 | horizontal/vertical | horizontal |
| pauseOnHover | 鼠标悬浮时暂停自动切换 | visible\|hover | true |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| default | 自定义默认内容 | -- |
| aside | 跑马灯的辅助信息 | -- |
| left-arrow | 左边切换箭头,slotOptions为{activeIndex,isFirst,isLast} | -- |
| right-arrow | 右边切换箭头,slotOptions为{activeIndex,isFirst,isLast} | -- |

