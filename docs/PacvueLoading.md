---
component: PacvueLoading
category: feedback
tags: [加载, 等待, 反馈]
aliases: [PacvueLoading, 加载]
version: 1.0.0
description: "PacvueLoading 加载"
---

# PacvueLoading 组件文档

> PacvueLoading 加载

**分类**: feedback | **标签**: 加载、等待、反馈

## 使用示例

### PacvueLoading 加载指令的一般使用

```vue
<template>
  <PacvueTree
    v-pacvueLoading="showLoading"
    @nodeChange="allEvents"
    @expandedChange="allEvents"
    @keywordChange="allEvents"
    @selectAll="allEvents"
    :data="tdata"
    :option="option"
    :clearable="true"
  >
  </PacvueTree>
</template>
<script>
  import { ref } from 'vue'
  import { ElMessage, ElMessageBox } from 'element-plus'
  export default {
    setup(props, ctx) {
      var showLoading = ref(true)
      const allEvents = (type, ...args) => {
        console.log(args)
      }
      const tdata = ref([])
      setTimeout(() => {
        tdata.value = mockData('key', 5, 3)
      }, 1000)
      const option = {
        propsList: [null, { id: 'id1', label: 'label1', children: 'children1' }, { id: 'id2', label: 'label2' }],
        propDefaultCheck: ['key-0-1-3-1'],
        pausedFn: (node) => {
          if (node.source.id === 'key-0-2') return 'Is Paused!!'
        }
      }
      return {
        event,
        tdata,
        option,
        showLoading
      }
    }
  }

  function mockData(key, length, l2) {
    const list = []
    for (let i = 0; i < length; i++) {
      var node = {
        label: `${key}-${i}`,
        id: `${key}-${i}`,
        custom: 'custom' + i,
        children: [
          {
            label1: `${key}-${i}-1-p-公文`,
            id1: `${key}-${i}-1`,
            custom: 'custom' + i,
            children1: [
              {
                label2: `${key}-${i}-1-1-uo`,
                id2: `${key}-${i}-1-1`,
                custom: 'custom' + i
              },
              {
                label2: `${key}-${i}-1-2-u`,
                id2: `${key}-${i}-1-2`,
                custom: 'custom' + i
              },
              {
                label2: `${key}-${i}-1-3-io`,
                id2: `${key}-${i}-1-3`,
                custom: 'custom' + i,
                children: [
                  {
                    label: `${key}-${i}-1-3-1-o-enable`,
                    id: `${key}-${i}-1-3-1`,
                    custom: 'custom' + i,
                    customVal: 'enable'
                  },
                  {
                    label: `${key}-${i}-1-3-2disable`,
                    id: `${key}-${i}-1-3-2`,
                    custom: 'custom' + i,
                    customVal: 'disable'
                  }
                ]
              }
            ]
          }
        ]
      }
      for (let j = 0; j < l2; j++) {
        node.children.push({
          label1: `${key}-${i}-${j + 2}disable`,
          id1: `${key}-${i}-${j + 2}`,
          custom: 'custom' + j,
          apply1: 'dddddddddd1',
          customVal: 'disable'
        })
      }
      list.push(node)
    }
    return list
  }
</script>
```

### PacvueLoading 加载指令的一般使用

```vue
<template>
  <PacvueTree
    v-pacvueLoading="showLoading"
    @nodeChange="allEvents"
    @expandedChange="allEvents"
    @keywordChange="allEvents"
    @selectAll="allEvents"
    pacvue-loading-text="拼命加载中"
    pacvue-loading-spinner="Loading"
    pacvue-loading-background="rgba(0, 0, 0, 0.8)"
    :data="tdata"
    :option="option"
    :clearable="true"
  >
  </PacvueTree>
</template>
<script>
  import { ref } from 'vue'
  import { ElMessage, ElMessageBox } from 'element-plus'
  export default {
    setup(props, ctx) {
      var showLoading = ref(true)
      const allEvents = (type, ...args) => {
        console.log(args)
      }
      const tdata = ref([])
      setTimeout(() => {
        tdata.value = mockData('key', 5, 3)
      }, 1000)
      const option = {
        propsList: [null, { id: 'id1', label: 'label1', children: 'children1' }, { id: 'id2', label: 'label2' }],
        propDefaultCheck: ['key-0-1-3-1'],
        pausedFn: (node) => {
          if (node.source.id === 'key-0-2') return 'Is Paused!!'
        }
      }
      return {
        event,
        tdata,
        option,
        showLoading
      }
    }
  }

  function mockData(key, length, l2) {
    const list = []
    for (let i = 0; i < length; i++) {
      var node = {
        label: `${key}-${i}`,
        id: `${key}-${i}`,
        custom: 'custom' + i,
        children: [
          {
            label1: `${key}-${i}-1-p-公文`,
            id1: `${key}-${i}-1`,
            custom: 'custom' + i,
            children1: [
              {
                label2: `${key}-${i}-1-1-uo`,
                id2: `${key}-${i}-1-1`,
                custom: 'custom' + i
              },
              {
                label2: `${key}-${i}-1-2-u`,
                id2: `${key}-${i}-1-2`,
                custom: 'custom' + i
              },
              {
                label2: `${key}-${i}-1-3-io`,
                id2: `${key}-${i}-1-3`,
                custom: 'custom' + i,
                children: [
                  {
                    label: `${key}-${i}-1-3-1-o-enable`,
                    id: `${key}-${i}-1-3-1`,
                    custom: 'custom' + i,
                    customVal: 'enable'
                  },
                  {
                    label: `${key}-${i}-1-3-2disable`,
                    id: `${key}-${i}-1-3-2`,
                    custom: 'custom' + i,
                    customVal: 'disable'
                  }
                ]
              }
            ]
          }
        ]
      }
      for (let j = 0; j < l2; j++) {
        node.children.push({
          label1: `${key}-${i}-${j + 2}disable`,
          id1: `${key}-${i}-${j + 2}`,
          custom: 'custom' + j,
          apply1: 'dddddddddd1',
          customVal: 'disable'
        })
      }
      list.push(node)
    }
    return list
  }
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| target | Loading 需要覆盖的 DOM 节点。可传入一个 DOM 对象或字符串；若传入字符串，则会将其作为参数传入 document.querySelector以获取到对应 DOM 节点 | object/string | document.body |
| body | 同 v-loading 指令中的 body 修饰符 | Boolean | false |
| fullscreen | 同 v-loading 指令中的 fullscreen 修饰符 | Boolean | true |
| lock | 同 v-loading 指令中的 lock 修饰符	boolean | Boolean | false |
| text | 显示在加载图标下方的加载文案 | string | -- |
| spinner | 自定义加载图标类名 | String | —	— |
| background | 遮罩背景色 | String | —	— |
| customClass | Loading 的自定义类名 | String | false |

