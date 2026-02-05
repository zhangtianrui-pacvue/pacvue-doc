---
component: TransferV2
category: form
tags: [穿梭框, 虚拟列表, V2]
aliases: [TransferV2]
version: 1.0.0
description: "PacvueTransferV2 穿梭框"
---

# TransferV2 组件文档

> PacvueTransferV2 穿梭框

**分类**: form | **标签**: 穿梭框、虚拟列表、V2

## 使用示例

### 大数据量性能优化穿梭框 左侧树使用后端分页加载，提升加载性能

```vue
<template>
  <PacvueButton @click="getTreeData">获取树数据</PacvueButton>
  <PacvueTransferV2 ref="transferRef" :option="option" :pageSizeLeft="pageSizeLeft" :pageSizeRight="20"
    @keywordChangeLeft="keywordChangeLeft" @pageChangeLeft="pageChangeLeft" @change="change" @init="init"
    :loading="!true" :loadingLeft="!true" />
</template>
<script setup>
  import { onMounted, ref } from 'vue'
  import { getPagedDataHighPerformance } from '../../components/PacvueTransferV2/mock'

  const pageSizeLeft = ref(20)
  const option = ref({
    children: 'content',
    label: 'name',
    enabled: 'enabled',
    id: 'id'
  })
  const transferRef = ref(null)

  function keywordChangeLeft(value, pagination) {
    console.log(value, pagination)
  }

  function pageChangeLeft(current, pageSize, keyword) {
    const leftData = getPagedDataHighPerformance(current, pageSize, keyword)
    transferRef.value.leftTreeChange({ leftData: JSON.parse(JSON.stringify(leftData)), leftTotal: 50 })
  }

  function change(value) {
    console.log('change', value)
  }

  function init(value) {
    console.log('init', value)
  }

  function getTreeData() {
    console.log(transferRef.value.getTreeData())
  }

  onMounted(() => {
    const pageInfo = getPagedDataHighPerformance(1, pageSizeLeft.value)
    const initData = {
      leftData: JSON.parse(JSON.stringify(pageInfo)),
      rightData: JSON.parse(JSON.stringify(getPagedDataHighPerformance(4, pageSizeLeft.value))),
      leftTotal: 50
    }
    transferRef.value.init(initData)
  })
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| option | 节点数据取值字段的key | Object | { children: 'children', label: 'label', enabled: 'enabled', id: 'id' } |
| placeholder | 搜索框提示。占位提示文字，在无输入时显示 | String | "Search" |
| pageSizeLeft | 左侧分页size | Number | 20 |
| pageSizeLeft | 右侧分页size | Number | 20 |
| loading | 组件全局loading状态。是否显示加载状态 | Boolean | false |
| loadingLeft | 左侧树组件loading状态 | Boolean | false |
| totalText | 统计信息文字 | String | 'Campaign Tags' |
| leftButtonText | 左侧按钮文案 | String | 'Add to Tag' |
| rightButtonText | 右侧按钮文案 | String | 'Remove from Tag' |
| tagText | 节点标签文案 | String | -- |
| onlyLeafId | 事件及实例方法中获取的选中值不需要拼接父节点的id | Boolean | true |

## 方法 Methods

组件暴露的方法，可通过 ref 调用。

| 方法名 | 说明 | 参数 |
| --- | --- | --- |
| init | 初始化渲染组件函数，调用后会触发init事件。 | ({ leftData, rightData, leftTotal }) => {} |
| leftTreeChange | 重新渲染左侧树组件，用于左侧筛选及翻页导致的重新渲染。 | ({ leftData, leftTotal }) => {} |
| getValue | 获取穿梭至右侧的id数据。 | () => [...ids] |
| getTreeData | 获取穿梭至右侧的数据，数据维持原始层级结构。 | () => [...nodes] |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| keywordChangeLeft | 左侧筛选事件 | (keyword, pagination) => {} |
| pageChangeLeft | 左侧翻页事件 | (current, pageSize, keyword) => {} |
| change | 穿梭数据发生变化事件 | ([...ids]) => {} |
| init | 组件初始化事件 | ([...ids]) => {} |

