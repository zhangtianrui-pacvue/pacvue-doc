---
component: PacvueTreeChart
category: chart
tags: [树形图表, 可视化]
aliases: [PacvueTreeChart]
version: 1.0.0
description: "PacvueTreeChart"
---

# PacvueTreeChart 组件文档

> PacvueTreeChart

**分类**: chart | **标签**: 树形图表、可视化

## 使用示例

### 树形结构图的基础用法

```vue
<template>
  <div style="height: 392px; overflow: hidden">
    <PacvueTreeChart :data="treeChartData1" v-model="acitveTreeId" :lineWidth="2" :levelNodeStyle="levelNodeStyle"
      @change="handleTreeChart">
      <template #default="{ level, label, value }">
        <div v-if="level == 2" class="pacvue-treeChart-node-name">
          +Dev Mode simplifies handoff, speedsup inspection, and integrates with toolslike VS Code and Storybook.+Dev
          Mode simplifies handoff, speedsup inspection, and integrates with toolslike VS
          Code and Storybook.
        </div>
        <span v-else>{{ label }}+{{ value }}</span>
      </template>
    </PacvueTreeChart>
  </div>
</template>
<script setup>
  import { ref } from 'vue'
  import { isEqual, cloneDeep, debounce } from 'lodash-es'
  var acitveTreeId = ref(['Total', 'SD', undefined, 'SP', 'SB'])
  var treeChartData1 = ref([
    [{ label: 'Total', value: 100, id: 'Total' }],
    [
      {
        label: 'SB',
        value: 40,
        id: 'SB',
        percentage: 40
      },
      {
        label: 'SD',
        value: 40,
        id: 'SD',
        percentage: 40
      },
      {
        label: 'SP',
        value: 40,
        id: 'SP',
        percentage: 40
      }
    ],
    undefined,
    [
      {
        label: 'SB',
        value: 40,
        id: 'SB',
        percentage: 40
      },
      {
        label: 'SD',
        value: 40,
        id: 'SD',
        percentage: 40
      },
      {
        label: 'SP',
        value: 40,
        id: 'SP',
        percentage: 40
      }
    ],
    [
      {
        label: 'SB',
        value: 40,
        id: 'SB',
        percentage: 40
      },
      {
        label: 'SD',
        value: 40,
        id: 'SD',
        percentage: 40
      },
      {
        label: 'SP',
        value: 40,
        id: 'SP',
        percentage: 40
      }
    ],
    [
      {
        label: 'SB',
        value: 40,
        id: 'SB',
        percentage: 40
      },
      {
        label: 'SD',
        value: 40,
        id: 'SD',
        percentage: 40
      },
      {
        label: 'SP',
        value: 40,
        id: 'SP',
        percentage: 40
      }
    ]
  ])
  var levelNodeStyle = ({ level, nodes }) => {
    if (level == 2 || level == 3) {
      return { style: { flex: 1 } }
    }
  }
  var handleTreeChart = () => {
    treeChartData1.value = cloneDeep(treeChartData1.value)
  }
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| data | 数据列表,结构为Array<{label:String,id:String,value:String,percentage:Number,percentageTip:String\|Number}> | Array | [] |
| v-model | 当前选中的值。双向绑定值，用于获取和设置组件的当前值 | Array<String> | [] |
| activeColorConfig | 激活状态的样式 | Object | { borderColor: '#ffb268', bgColor: 'rgba(255, 178, 104, 0.10)' } |
| isTopCanClick | 顶级节点是否可以点击 | Boolean | false |
| lineBodyWidth | 连线容器所占的宽度 | Number | 16 |
| lineWidth | 连线的线的粗细 | Number | 2 |
| disabledClick | 一个用来判断该Node是否被禁用的函数,接受一个 Node 对象作为参数。 应该返回一个 Boolean 值。 | Function({nodeInfo,level}) | -- |
| levelNodeStyle | 设置各层级的Node样式,需要返回{style:Object\|Array,class:Object\|Array} | Function({nodes,level}) | -- |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| change | 绑定值变化触发事件 | Function(id,modelVal) |
| nodeClick | 节点点击事件 | Function(id,modelVal,nodeInfo) |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| default | 显示具体内容的插槽,slotScop为{level, label, value, percentage,id} | -- |
| aside | 显示具体内容的辅助插槽,slotScope同default一样 | -- |

