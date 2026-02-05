---
component: pagination
category: navigation
tags: [分页, 导航, 翻页]
aliases: [Pagination, 分页]
version: 1.0.0
description: "PacvuePagination 分页器"
---

# pagination 组件文档

> PacvuePagination 分页器

**分类**: navigation | **标签**: 分页、导航、翻页

## 使用示例

### PacvuePagination 的一般使用

```vue
<template>
  <PacvuePagination v-model:pagination="pagination"></PacvuePagination>
</template>
<script setup>
  import { reactive } from 'vue'
  function dataChange(current, pageSize) {
    console.log(current, pageSize)
  }
  const pagination = reactive({
    current: 1,
    pageSize: 20,
    total: 50,
    showQuickJumper: true,
    showSizeChanger: true,
    onPageChange: dataChange,
    onPageSizeChange: dataChange,
    small: false
  })
</script>
```

### PacvuePaginationNew 只可以进行前后页的跳转，不可以进行间隔跳转，也没有

```vue
<template>
  <PacvuePaginationNew v-model:pagination="pagination1" :customMode="!true" :hideOnSinglePage="false"
    :hideOnEmpty="false"></PacvuePaginationNew>
</template>
<script setup>
  import { reactive } from 'vue'
  // 翻页至最后一页不可再往后翻
  function dataChange1(current, pageSize) {
    pagination1.canJump = Math.ceil(pagination1.total / pageSize) > current
  }
  const pagination1 = reactive({
    current: 1,
    pageSize: 50,
    total: 120,
    showSizeChanger: true,
    onPageChange: dataChange1,
    onPageSizeChange: dataChange1,
    canJump: true,
    showTotalNumber: true,
    showJump: true
  })
</script>
```

### PacvueBlockPagination 页面信息展示跳转范围，没有 pageSize 切换

```vue
<template>
  <PacvueBlockPagination :pagination="pagination3"></PacvueBlockPagination>
</template>
<script setup>
  const pagination3 = reactive({
    total: 101,
    pageSize: 5,
    pagerCount: 5,
    current: 1,
    showTotalNumber: true,
    onPageChange: (current, pageSize) => {
      console.log('onPageChange', current, pageSize)
    },
  })
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| v-model:pagination | 分页器配置参数 | Object | 查看 PacvuePagination 属性配置参数 |
| min | pageSize 切换最小值 | Number | 1 |
| max | pageSize 切换最大值 | Number | 50 |
| small | 当为「small」时，是小尺寸分页 | Boolean | false |
| pageSelectData | 分页器 pageSize 切换下拉菜单自定义属性 | Array | `           [             { value: 10, label: '10/page' },             { value: 20, label: '20/page' },             { value: 50, label: '50/page' },             { value: 100, label: '100/page' }           ]         ` |
| hideOnSinglePage | 当分页只有一页时是否隐藏分页器 | Boolean | false |
| hideOnEmpty | 当 pagination.total 为 0 时是否隐藏分页器 | Boolean | true |
| hidePageRightOnSinglePage | 单独控制 是否一页的时候，隐藏右侧分页选择器 | Boolean | true |
| current | 当前页数 | Number | -- |
| pageSize | 每页条数 | Number | -- |
| total | 数据总数 | Number | -- |
| showQuickJumper | 是否显式 快速跳转至某页功能 | Boolean | false |
| showSizeChanger | 是否显式 改变 pageSize 功能 | Boolean | true |
| showGotoPage | 是否显式 page 输入数字跳转 功能，small模式下默认值为false，default模式下默认值为true | Boolean | true\|false |
| onPageChange | 页码改变的回调，参数是改变后的页码及每页条数 | Function(current, pageSize) | -- |
| onPageSizeChange | pageSize 变化的回调 | Function(current, pageSize) | -- |
| canJump | 外部控制分页器 是否可以进行下一页的跳转，当判断不可跳转下一页时设置为false | Boolean | true |
| current | 当前页数 | Number | -- |
| pageSize | 每页条数 | Number | -- |
| total | 数据总数 | Number | -- |
| showSizeChanger | 是否显式 改变 pageSize 功能 | Boolean | false |
| onPageChange | 页码改变的回调，参数是改变后的页码及每页条数 | Function(current, pageSize) | -- |
| onPageSizeChange | pageSize 变化的回调 | Function(current, pageSize) | -- |
| showPage | 是否显示页数信息，默认不显示 | Boolean | false |
| showTotalNumber | 是否显示总页数信息，默认显示 | Boolean | true |
| showJump | 是否显示右侧跳转按钮，默认显示 | Boolean | true |
| current | 当前页数 | Number | -- |
| pageSize | 每页条数 | Number | 5 |
| total | 数据总数 | Number | -- |
| onPageChange | 页码改变的回调，参数是改变后的页码及每页条数 | Function(current, pageSize) | -- |
| showTotalNumber | 是否显示总页数信息，默认显示 | Boolean | true |
| pagerCount | 页码按钮的数量，当总页数超过该值时会折叠 | Number | 5 |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| pagetip | 分页器左侧分页信息中的提示信息 | -- |
| customLeft | 分页器最左侧位置自定义内容展示插槽 | -- |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/pagination.html)

