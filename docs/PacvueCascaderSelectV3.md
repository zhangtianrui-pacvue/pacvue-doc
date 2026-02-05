---
component: PacvueCascaderSelectV3
category: form
tags: [级联选择V3, 表单]
aliases: [PacvueCascaderSelectV3]
version: 1.0.0
description: "Cascader Select V3 懒加载树"
---

# PacvueCascaderSelectV3 组件文档

> Cascader Select V3 懒加载树

**分类**: form | **标签**: 级联选择V3、表单

## 使用示例

### v-model:selectData 为单向绑定值，只可以在初始化时设置一次值，之后

```vue
<template>
  <PacvueCascaderSelectV3 :useSelectData="true" v-model:selectData="selectData" :startLevel="1" :data="dataList"
    :labelInner="'Cascader'" :props="cascaderProps" placeholder="Campaign tag" :collapseTags="true"
    :isValRecusion="true" :loading="loadingCom" @change="selectChange" @clear="selectClear" @expand="onExpand">
  </PacvueCascaderSelectV3>
</template>
<script setup>
  import { ref, shallowRef, shallowReactive, computed, watch, triggerRef } from 'vue'

  /** 生成假数据 */
  function mockData(long, length, node) {
    const list = []
    const parent = node?.tagId
    for (let i = 0; i < length; i++) {
      const id = parent ? `${parent}*${long}|${i}` : `${long}|${i}`
      const node = { tagName: id, tagId: id }
      list.push(node)
    }
    return list
  }
  const loadingCom = ref(false)
  const selectData = ref([])
  const cascaderProps = shallowReactive({ label: 'tagName', value: 'tagId', children: 'subTags' })
  const list = mockData(1, 10)
  const dataList = shallowRef([])
  const cascaderTree = shallowRef({})
  const dataSource = shallowRef([])
  loadingCom.value = true
  setTimeout(() => {
    // 有子tree的节点需要设置 hasChildren = true
    list[0].hasChildren = true
    list[2].hasChildren = true
    dataList.value = list
    loadingCom.value = false
  }, 10)
  function selectChange(val) {
    console.log(val)
  }
  function selectClear() {
    console.log('clear')
  }
  /**
  * 节点展开事件
  *
  * 在事件回调中请求子节点数据
  * 然后调用 next 函数将数据传入并生成子节点树
  * 懒加载过的节点不会重复触发此事件。
  **/
  function onExpand(node, next) {
    const level = node.level
    // 请求子节点数据
    const list = mockData(level + 2, 10, node)
    if (level < 5) {
      // 有子tree的节点需要设置 hasChildren = true
      list[2].hasChildren = true
      list[0].hasChildren = true
    }
    // 请求子节点数据
    next(list)
  }
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| v-model:selectData | 使用 object 管理选中数据，存储所有层级的全选状态节点，结构为一维数组。 | Array | [] |
| width | 组件宽度。组件宽度，支持像素值或百分比 | String | 100% |
| labelInner | 内连显示label | String | -- |
| data | 数据列表。数据源，用于渲染组件内容 | Array | [] |
| props | 配置选项，具体看下表 | Object | { value: 'value', label: 'label', children: 'children' } |
| placeholder | Select提示信息。占位提示文字，在无输入时显示 | String | -- |
| collapseTags | 是否折叠tag显示 | Boolean | false |
| showPlaceholder | 是否显示提示信息 | Boolean | true |
| clearable | 是否可以清空选项。是否显示清除按钮，点击可清空当前值 | Boolean | false |
| disabled | 是否禁用。是否禁用组件，禁用后无法进行交互 | Boolean | false |
| teleported | 下拉列表是否添加到body中,默认true | Boolean | true |
| dropdownMaxWidth | 下拉框的最大宽度，最小为200px | String | 800px |
| dropdownMaxHeight | 下拉框的最大高度 | String | 300px |
| hasSelectAll | 是否有全选功能 | Boolean | false |
| startLevel | level的起始值 | Number | 0 |
| scrollIntoView | 级联数据出现横向滚动条时，是否自动将最新展开的数据滚动到可视区。默认开启。 | Boolean | true |
| modelValueAll | v-model:selectData 数据是否存入节点的全部原始数据。默认只存储精简数据 | Boolean | false |
| loading | 用于控制组件下拉框的loading样式显隐。 | Boolean | false |
| createSelectLabelStyle | 生成选中项样式 | ({value})=>Object | -- |
| createItemStyle | 生成下拉列表中每一项的样式 | ({item})=>Object | -- |
| disableCallback | 下拉列表中checkbox禁用回调 | Function({item})=>Boolean | ()=>false |
| label | 指定节点标签为节点对象的某个属性值 | String | label |
| value | 指定节点value为节点对象的某个属性值 | String | value |
| children | 指定子树为节点对象的某个属性值 | String | children |

## 方法 Methods

组件暴露的方法，可通过 ref 调用。

| 方法名 | 说明 | 参数 |
| --- | --- | --- |
| clear | 清空选中数据 | () => {} |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| change | 绑定值变化触发事件 | Function(value) |
| clear | 可清空的单选模式下用户点击清空按钮时触发 | Function() |
| expand | 节点展开事件，用于懒加载生成子数，懒加载过的节点不会重复触发此事件。事件入参为：node（当前展开节点信息）next（用于懒加载子树，在请求到子树数据后调用，并将数据传入该函数中。） | (node, next) => {} |

