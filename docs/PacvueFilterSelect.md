---
component: PacvueFilterSelect
category: filter
tags: [筛选选择器, 过滤]
aliases: [PacvueFilterSelect]
version: 1.0.0
description: "PacvueFilterSelect基础用法"
---

# PacvueFilterSelect 组件文档

> PacvueFilterSelect基础用法

**分类**: filter | **标签**: 筛选选择器、过滤

## 使用示例

### PacvueFilterSelect 主要用来优化大数据量时的渲染性能问题。

```vue
<template>
  <pacvue-filter-select ref="homeTagOption" style="width: 400px" v-model="tagIds" :data="dataList"
    :props="{ label: 'label', value: 'id' }" :placeholder="'Cascader'" :defaultChecked="defaultChecked"
    :scrollEnd="scrollEnd" :scrollSize="scrollSize" :scrollTotal="scrollTotal" :filterChange="filterChange"
    :maxLimit="2000" @change="handleChange"></pacvue-filter-select>
  <div style="margin-top: 12px;">
    <pacvue-button @click="setValues2">重置 modelValue</pacvue-button>
    <pacvue-button @click="getSelections">getSelections</pacvue-button>
    <pacvue-button @click="getSelectionById">getSelectionById</pacvue-button>
  </div>
</template>

<script setup>
  import { onMounted, ref, shallowRef } from 'vue'

  const tagIds = ref([])
  const filterSelectRef = ref(null)
  const dataList = shallowRef([])
  const scrollTotal = ref(0)
  // 设置滚动加载数据的请求上限值为100
  const scrollSize = ref(100)

  onMounted(() => {
    // 模拟初始化请求数据
    initData().then(list => {
      dataList.value = list
      scrollTotal.value = 205
    })
  })
  // 创建假数据
  function initData() {
    return new Promise((resolve) => {
      setTimeout(() => {
        const list = []
        for (let i = 0; i < scrollSize.value; i++) {
          list.push({
            label: `nosearch-${i}`,
            id: `nosearch-${i}`,
          })
        }
        resolve(list)
      }, 1000)
    })
  }
  // 模拟滚动到底部时请求下一部分数据
  function scrollEnd(args) {
    console.log('scrollEnd', args)
    return new Promise((resolve) => {
      setTimeout(() => {
        const list = []
        const key = args.keyword
        const before = (args.scrollInfo.current - 1) * scrollSize.value
        // 模拟最后一页数据不足 scrollSize 时的情况
        if (args.scrollInfo.current === 3) {
          for (let i = 0; i < 5; i++) {
            const index = i + before
            list.push({
              label: key ? `filter-${key}-${index}` : `nosearch-${index}`,
              id: key ? `filter-${key}-${index}` : `nosearch-${index}`,
            })
          }
        } else {
          for (let i = 0; i < scrollSize.value; i++) {
            const index = i + before
            list.push({
              label: key ? `filter-${key}-${index}` : `nosearch-${index}`,
              id: key ? `filter-${key}-${index}` : `nosearch-${index}`,
            })
          }
        }
        resolve(list)
      }, 1000)
    })
  }
  // 模拟关键词筛选时请求数据
  function filterChange(args) {
    console.log('filterChange', args)
    return new Promise((resolve) => {
      if (args.keyword) {
        setTimeout(() => {
          const list = []
          const key = args.keyword
          for (let i = 0; i < scrollSize.value; i++) {
            list.push({
              label: `filter-${key}-${i}`,
              id: `filter-${key}-${i}`,
            })
          }
          resolve(list)
        }, 1000)
      } else {
        initData().then(resolve)
      }
    })
  }
  function handleChange(modelValue) {
    console.log('handleChange', modelValue)
  }
  function getSelections() {
    console.log(filterSelectRef.value.getSelections())
  }
  function getSelectionById() {
    console.log(filterSelectRef.value.getSelectionById('nosearch-0'))
  }
  function setValues2() {
    tagIds.value = ["nosearch-1", "nosearch-0", "filter-12-0", "filter-12-1"]
  }
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| modelValue/v-model | 选中项绑定值 | Array | [] |
| data | 下拉列表数据。数据源，用于渲染组件内容 | Array | -- |
| props | data 中 value label 的取值字段。 | Object | { value: 'value', label: 'label' } |
| placeholder | placeholder文字。占位提示文字，在无输入时显示 | String | Select All |
| scrollSize | 每次滚动加载数据的请求上限值，相当于分页的pageSize。 | Number | 500 |
| scrollTotal | 下拉列的总数据量。 | Number | -- |
| filterChange | 关键词筛选触发时的回调函数。 | Funciton | ({keyword, scrollInfo}) => [] |
| scrollEnd | 下拉列滚动到底部时触发的回调函数。 | Funciton | ({keyword, scrollInfo}) => [] |
| maxLimit | 数据勾选的上限值。 | Number | 2000 |
| labelInner | 显示的Label名称。 | String | -- |
| tooltip | 下拉列表搜索框中提示图标的提示文字，如果不设置则图标也一并隐藏。 | String | -- |
| selectedNameList | 选中数据的 name 值，用于在 回显默认值 但是 当前页数据中没有默认值时，展示选中数据的 name。 | Array | -- |
| hasBorder | 是否有border | Boolean | true |
| referenceStyle | 显示的Input框的触发器样式 | Object | -- |
| isUseValNoLabel | 否当当选中值没有匹配到label时,使用value对应的值 | Boolean | true |
| createCustomUUId | 下拉列表中每一项自定义唯一值 | Function | ({id, item}) => String |

## 方法 Methods

组件暴露的方法，可通过 ref 调用。

| 方法名 | 说明 | 参数 |
| --- | --- | --- |
| clearAll | 清除所有选中数据。 | () => void 0 |
| getSelections | 获取当前选中的信息，返回值中包含节点的所有信息。 | () => [] |
| getSelectionById | 根据节点的 id 获取节点信息。 | (id) => nodeInfo |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| change | 绑定值变化触发事件 | Function(value) |

