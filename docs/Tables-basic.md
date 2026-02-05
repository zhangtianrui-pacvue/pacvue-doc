---
component: Tables
submodule: basic
category: data
tags: [表格, 数据展示, 列表, basic]
aliases: [Table, Tables, 表格]
version: 1.0.0
---

# Tables - 基础用法

> Table 表格基础使用

## 使用示例

### 注意 columns 必须设置 dataIndex 作为唯一值（不可重复）。 性能建议

```vue
<template>
  <PacvueTable sticky v-model:columns="columns" :loading="loading" :dataSource="dataSource" />
</template>
<script setup>
  /** 由于数据过大不方便展示，所以源码展示的数据相较于真实 table 数据做了删减。 */
  const columns = ref([
    {
      dataIndex: 'query', // column 唯一标识符
      title: 'Query', // 默认展示文字，无特殊处理则单元格默认展示此文本
      minWidth: 300, // 最小宽度
      fixed: 'left' // 左侧固定
      // ... 更多配置请查看配置参数
    },
    {
      dataIndex: 'matchType',
      title: 'Bidding Strategy',
      drag: true,
      resizable: true,
      minWidth: 130
    },
    {
      dataIndex: 'Sales',
      title: 'Sales',
      sorter: {
        compare: (a, b) => a.Sales - b.Sales
      },
      drag: true,
      resizable: true,
      minWidth: 100
    }
  ])
  const data = [
    {
      title: null,
      profileId: '4149573212393813',
      CVR: 60.0,
      CTR: 0.659,
      CPC: 3.69,
      CPA: 6.15,
      CPM: 2.0,
      ACOS: 66.271,
      ROAS: 1.5
    }
  ]
  const loading = reactive({
    spinning: false
  })
  const dataSource = ref([])
  loading.spinning = true
  setTimeout(() => {
    dataSource.value = data // 模拟数据请求操作
    loading.spinning = false
  }, 1000)
</script>
```

### header 插槽的根标签必须是 TableHeaderCell 内置组件，可以使用该组件的

```vue
<template>
  <PacvueTable sticky v-model:columns="columns" :loading="loading" :dataSource="dataSource"
    v-model:pagination="pagination">
    <!-- header 表头内容自定义插槽 -->
    <template #headerCell="headerCell">
      <TableHeaderCell v-bind="headerCell">
        {{ headerCell.title + ' custom' }}
        <!-- header 插槽组件内部的 自定义图标插槽 -->
        <template #icon>
          <el-icon>
            <ElemeFilled />
          </el-icon>
        </template>
      </TableHeaderCell>
    </template>
    <!-- body 内容自定义插槽 -->
    <template #bodyCell="bodyCell">
      <TableBodyCell v-bind="bodyCell">
        <a>{{ bodyCell.text }}</a>
      </TableBodyCell>
    </template>
  </PacvueTable>
</template>
<script setup>
  import { ElemeFilled } from '@pacvue/element-plus'
  /** 由于数据过大不方便展示，所以源码展示的数据相较于真实 table 数据做了删减。 */
  const columns = ref([
    {
      dataIndex: 'query', // column 唯一标识符
      title: 'Query', // 默认展示文字，无特殊处理则单元格默认展示此文本
      minWidth: 300, // 最小宽度
      fixed: 'left' // 左侧固定
      // ... 更多配置请查看配置参数
    },
    {
      dataIndex: 'matchType',
      title: 'Bidding Strategy',
      drag: true,
      resizable: true,
      minWidth: 130
    },
    {
      dataIndex: 'Sales',
      title: 'Sales',
      sorter: {
        compare: (a, b) => a.Sales - b.Sales
      },
      drag: true,
      resizable: true,
      minWidth: 100
    }
  ])
  const data = [
    {
      title: null,
      profileId: '4149573212393813',
      CVR: 60.0,
      CTR: 0.659,
      CPC: 3.69,
      CPA: 6.15,
      CPM: 2.0,
      ACOS: 66.271,
      ROAS: 1.5
    }
  ]
  const loading = reactive({
    spinning: false
  })
  const dataSource = ref([])
  loading.spinning = true
  setTimeout(() => {
    dataSource.value = data // 模拟数据请求操作
    pagination.total = data.length // 模拟 total 设置操作
    loading.spinning = false
  }, 1000)
  const pagination = reactive({
    current: 1,
    pageSize: 20,
    total: 0,
    showQuickJumper: true,
    showSizeChanger: true,
    small: false
  })
</script>
```

