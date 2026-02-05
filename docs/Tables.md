---
component: Tables
category: data
tags: [表格, 数据展示, 列表]
aliases: [Table, Tables, 表格]
version: 1.0.0
description: "Table 表格基础使用"
---

# Tables 组件文档

> Table 表格基础使用

**分类**: data | **标签**: 表格、数据展示、列表

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

### action default 模式 1、设置 showAction 属性为 true 2、设置

```vue
<template>
  <PacvueTable sticky v-model:columns="columns" :loading="loading" :dataSource="dataSource" :showAction="true"
    :actionType="'default'" v-model:pagination="pagination" @resizeColumn="onResizeColumn">
    <template #headerCell="headerCell">
      <TableHeaderCell v-bind="headerCell">
        {{ headerCell.title + '-h' }}
        <!-- header 插槽组件内部的 自定义图标插槽 -->
        <template #icon>
          <el-icon>
            <ElemeFilled />
          </el-icon>
        </template>
      </TableHeaderCell>
    </template>
    <template #bodyCell="bodyCell">
      <TableBodyCell v-bind="bodyCell">
        <a>{{ bodyCell.text }}</a>
        <!-- body 插槽组件内部的 自定义 action 中每个图标的样式 -->
        <template #listItem="{ item, index }">
          <el-icon>
            <ElemeFilled />
          </el-icon>
        </template>
      </TableBodyCell>
    </template>
  </PacvueTable>
</template>
<script setup>
  import { ElemeFilled, CirclePlus } from '@pacvue/element-plus'
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
      // 当开启 showAction 时，可以配置 pacActionlist 用于展示每行的 action 图标
      pacActionlist: [
        {},
        {},
        {},
        {},
        [
          { label: 'Add To Tag', value: 'value1' },
          { label: 'Add To Brand audit', value: 'value2' },
          {
            label: 'Delete',
            value: 'value3',
            children: [
              { label: 'sssss', value: 'sssss' },
              {
                label: 'sssssd',
                value: 'sssssd',
                children: [
                  { label: 'sssss', value: 'sssss' },
                  { label: 'sssssd', value: 'sssssd' }
                ]
              }
            ]
          }
        ]
      ], // 数组中可以是任意用于设置图标的数据
      title: null,
      profileId: '4149573212393813',
      CVR: 60.0,
      CTR: 0.659,
      CPC: 3.69,
      CPA: 6.15,
      CPM: 2.0,
      ACOS: 66.271,
      ROAS: 1.5
    },
    {
      key: 1,
      pacActionlist: [
        {},
        {},
        {},
        [
          { label: 'value1', value: 'value1' },
          { label: 'label2', value: 'value2' }
        ]
      ], // 数组中可以是任意用于设置图标的数据
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
  var onResizeColumn = (...args) => {
    console.log('onResizeColumn', ...args)
  }
</script>
```

### action small 模式 small 模式的设置参考 default 模式

```vue
<template>
  <PacvueTable sticky v-model:columns="columns1" :loading="loading" :dataSource="dataSource" :showAction="true"
    :actionType="'small'" v-model:pagination="pagination" @resizeColumn="onResizeColumn">
    <template #headerCell="headerCell">
      <TableHeaderCell v-bind="headerCell">
        {{ headerCell.title }}
        <!-- header 插槽组件内部的 自定义图标插槽 -->
        <template #icon>
          <el-icon>
            <ElemeFilled />
          </el-icon>
        </template>
      </TableHeaderCell>
    </template>
    <template #bodyCell="bodyCell">
      <TableBodyCell v-bind="bodyCell">
        <a>{{ bodyCell.text }}</a>
        <!-- body 插槽组件内部的 自定义 action 中每个图标的样式 -->
        <template #listItem="{ item, index }">
          <el-icon>
            <CirclePlus />
          </el-icon>
        </template>
      </TableBodyCell>
    </template>
  </PacvueTable>
</template>
<script setup>
  import { ElemeFilled, CirclePlus } from '@pacvue/element-plus'
  /** 由于数据过大不方便展示，所以源码展示的数据相较于真实 table 数据做了删减。 */
  const columns1 = ref([
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
      // 当开启 showAction 时，可以配置 pacActionlist 用于展示每行的 action 图标
      pacActionlist: [
        {},
        {},
        {},
        {},
        [
          { label: 'Add To Tag', value: 'value1' },
          { label: 'Add To Brand audit', value: 'value2' },
          { label: 'Add To Brand audit1', value: 'value3' }
        ]
      ], // 数组中可以是任意用于设置图标的数据
      title: null,
      profileId: '4149573212393813',
      CVR: 60.0,
      CTR: 0.659,
      CPC: 3.69,
      CPA: 6.15,
      CPM: 2.0,
      ACOS: 66.271,
      ROAS: 1.5
    },
    {
      pacActionlist: [{}, {}, {}, {}, {}, {}, {}, {}], // 数组中可以是任意用于设置图标的数据
      title: null,
      profileId: '4149573212393813',
      CVR: 60.0,
      CTR: 0.659,
      CPC: 3.69,
      CPA: 6.15,
      CPM: 2.0,
      ACOS: 66.271,
      ROAS: 1.5
    },
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
    },
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
    },
    {
      pacActionlist: [{}, {}, {}, {}, {}], // 数组中可以是任意用于设置图标的数据
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
  var onResizeColumn = (...args) => {
    console.log('onResizeColumn', ...args)
  }
</script>
```

### action showcase 模式 showcase 模式的设置参考 default 模式

```vue
<template>
  <PacvueTable sticky :columns="columns1" :loading="loading" :dataSource="dataSource" :showAction="true"
    :actionType="'showcase'" :pagination="pagination">
    <template #bodyCell="bodyCell">
      <TableBodyCell v-bind="bodyCell">
        <template #listItem>
          <el-icon>
            <ElemeFilled />
          </el-icon>
        </template>
      </TableBodyCell>
    </template>
  </PacvueTable>
</template>
<script setup>
  import { ElemeFilled, CirclePlus } from '@pacvue/element-plus'
  /** 由于数据过大不方便展示，所以源码展示的数据相较于真实 table 数据做了删减。 */
  const columns1 = ref([
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
      // 当开启 showAction 时，可以配置 pacActionlist 用于展示每行的 action 图标
      pacActionlist: [
        {},
        {},
        {},
        {},
        [
          { label: 'Add To Tag', value: 'value1' },
          { label: 'Add To Brand audit', value: 'value2' },
          { label: 'Add To Brand audit1', value: 'value3' }
        ]
      ], // 数组中可以是任意用于设置图标的数据
      title: null,
      profileId: '4149573212393813',
      CVR: 60.0,
      CTR: 0.659,
      CPC: 3.69,
      CPA: 6.15,
      CPM: 2.0,
      ACOS: 66.271,
      ROAS: 1.5
    },
    {
      pacActionlist: [{}, {}, {}, {}, {}, {}, {}, {}], // 数组中可以是任意用于设置图标的数据
      title: null,
      profileId: '4149573212393813',
      CVR: 60.0,
      CTR: 0.659,
      CPC: 3.69,
      CPA: 6.15,
      CPM: 2.0,
      ACOS: 66.271,
      ROAS: 1.5
    },
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
    },
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
    },
    {
      pacActionlist: [{}, {}, {}, {}, {}], // 数组中可以是任意用于设置图标的数据
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

### 全选及多选功能 如果只是一般全选，不需要 Select All 功能，请直接按照官方文档进行配置

```vue
<template>
  <PacvueTable sticky :summaryFixed="'bottom'" v-model:columns="columns1" :loading="loading" :rowTotalShow="true"
    :dataSource="dataSource" :rowTotalData="totalRes" :totalFormat="totalFormat" :rowSelection="rowSelection"
    v-model:pagination="pagination">
    <template #summaryCell="cellProps">
      <TableSummaryCell v-bind="cellProps">
        <i>${{ cellProps.total }}</i>
      </TableSummaryCell>
    </template>
  </PacvueTable>
</template>
<script setup>
  import { ElemeFilled, CirclePlus } from '@pacvue/element-plus'
  /** 由于数据过大不方便展示，所以源码展示的数据相较于真实 table 数据做了删减。 */
  const columns1 = ref([
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
  const totalFormat = (total, column) => {
    if (!total) return ''
    return '$' + total
  }
  const selectedRowKeys = ref([])
  const onSelectChange = (selectedRowKeys, selectedRows) => {
    console.log('selectedRowKeys changed: ', selectedRowKeys, selectedRows)
  }
  const rowSelection = reactive({
    selectedRowKeys: selectedRowKeys,
    onChange: onSelectChange,
    allSelect: true,
    rowSelectedList: [],
    allSelectType: '',
    getCheckboxProps: (record) => {
      return record.key === 2
    },
    onSelectAll: (type, allSelectType, selectedRowKeys, selectedRows) => {
      console.log('onSelectAll: ', type, allSelectType, selectedRowKeys, selectedRows)
    }
  })
  const totalRes = ref({
    keywordsCount: 445,
    Impression: 234487,
    Click: 1129,
    SaleUnits: 435,
    Spend: 2869.73,
    Sales: 6392.52,
    Conversion: 430,
    CVR: 38.086000000000006,
    CTR: 0.481,
    CPC: 2.54,
    CPA: 6.67,
    CPM: 12.23,
    ACOS: 44.891000000000005,
    ROAS: 2.22,
    OtherSales: 2497.87,
    OtherSalesPercent: 39.074,
    OrderPrice: 14.86632,
    currencySymbol: '£',
    countryAddress: 'co.uk',
    currencyCode: null,
    countryCode: 'UK'
  })
</script>
```

### 分页 1、开启分页需要设置 pagination 配置属性，详情请查看源码展示及

```vue
<template>
  <PacvueTable sticky :loading="loading" v-model:columns="columns" :dataSource="dataSource"
    v-model:pagination="pagination" v-model:serverSorter="serverSorter">
  </PacvueTable>
</template>
<script setup>
  import { reactive, ref, onMounted } from 'vue'
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
      key: 'keywordText',
      dataIndex: 'keywordText',
      title: 'Keyword',
      minWidth: 250,
      drag: true,
      resizable: true,
      align: 'right',
      orderByField: 'keywordText'
    },
    {
      key: 'matchType',
      dataIndex: 'matchType',
      title: 'Bidding Strategy',
      drag: true,
      resizable: true,
      minWidth: 130,
      orderByField: 'matchType'
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
  // 请求后端数据
  const getData = () => {
    loading.spinning = true
    setTimeout(() => {
      dataSource.value = data // 模拟数据请求操作
      pagination.total = data.length // 模拟 total 设置操作
      loading.spinning = false
    }, 1000)
  }
  const dataChange = (current, pageSize, orderAsc, orderByField) => {
    console.log(current, pageSize, orderAsc, orderByField)
    getData()
  }
  const pagination = reactive({
    current: 1,
    pageSize: 10,
    total: 0,
    showQuickJumper: true,
    showSizeChanger: true,
    small: false,
    onPageChange: dataChange,
    onPageSizeChange: dataChange
  })
  const serverSorter = reactive({
    orderAsc: false,
    orderByField: 'keywordText',
    onServerSort: dataChange
  })
  onMounted(() => getData())
</script>
```

### 前端排序步骤 前端排序不需要设置 serverSorter，只需要在 columns

```vue
<template>
  <PacvueTable sticky :loading="loading" v-model:columns="columns" :dataSource="dataSource"
    v-model:pagination="pagination">
  </PacvueTable>
</template>
<script setup>
  import { reactive, ref, onMounted } from 'vue'
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
      key: 'keywordText',
      dataIndex: 'keywordText',
      title: 'Keyword',
      minWidth: 250,
      drag: true,
      resizable: true,
      align: 'right'
    },
    {
      dataIndex: 'bid',
      title: 'Monthly Sale Units',
      align: 'right',
      sorter: {},
      sortOrder: 'ascend',
    },
    {
      dataIndex: 'Sales',
      title: 'Sales',
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
  // 请求后端数据
  const getData = () => {
    loading.spinning = true
    setTimeout(() => {
      dataSource.value = data // 模拟数据请求操作
      pagination.total = data.length // 模拟 total 设置操作
      loading.spinning = false
    }, 1000)
  }
  const dataChange = (current, pageSize, orderAsc, orderByField) => {
    console.log(current, pageSize, orderAsc, orderByField)
    getData()
  }
  const pagination = reactive({
    current: 1,
    pageSize: 10,
    total: 0,
    showQuickJumper: true,
    showSizeChanger: true,
    small: false,
    onPageChange: dataChange,
    onPageSizeChange: dataChange
  })
  const serverSorter = reactive({
    orderAsc: false,
    orderByField: 'keywordText',
    onServerSort: dataChange
  })
  onMounted(() => getData())
</script>
```

### 示例：index7

```vue
<template>
  <div style="margin-bottom: 16px">
    <PacvueButton @click="eidtclick">修改第一列第一行数据</PacvueButton>
    <PacvueButton @click="delectclick">删除第一行数据</PacvueButton>
  </div>
  <PacvueTable ref="tableRef" sticky v-model:columns="columns" :loading="loading" :dataSource="dataSource"
    v-model:pagination="pagination">
    <template #bodyCell="bodyCell">
      <TableBodyCell v-bind="bodyCell">
        <template v-if="bodyCell.column.dataIndex === 'query'">
          <template v-if="widthchange">
            <div>{{ bodyCell.text }}</div>
            <div><el-icon>
                <ElemeFilled />
              </el-icon>123456789121123456234564653456789</div>
          </template>
          <template v-else>{{ bodyCell.text }}</template>
        </template>
        <template v-else> {{ bodyCell.text }} </template>
      </TableBodyCell>
    </template>
  </PacvueTable>
</template>
<script setup>
  import { reactive, ref, onMounted } from 'vue'
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
      key: 'keywordText',
      dataIndex: 'keywordText',
      title: 'Keyword',
      minWidth: 250,
      drag: true,
      resizable: true,
      align: 'right',
      orderByField: 'keywordText'
    },
    {
      key: 'matchType',
      dataIndex: 'matchType',
      title: 'Bidding Strategy',
      drag: true,
      resizable: true,
      minWidth: 130,
      orderByField: 'matchType'
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
  const tableRef = ref()
  const dataSource = ref([])
  const widthchange = ref(true)
  /**
   * 编辑某一行数据
   */
  const eidtclick = () => {
    dataSource.value[0].query = Math.random()
    // 编辑数据后需要修改 dataSource.value 内存地址，否则修改可能不生效或延迟生效
    dataSource.value = [].concat(dataSource.value)
  }
  /** 删除行数据 */
  const delectclick = () => {
    dataSource.value.splice(0, 1)
    // 前端分页时需要手动调整 page total 值
    pagination.total--
    // 编辑数据后需要修改 dataSource.value 内存地址，否则修改不生效或延迟生效
    dataSource.value = [].concat(dataSource.value)
  }
  // 请求后端数据
  const getData = () => {
    loading.spinning = true
    setTimeout(() => {
      dataSource.value = data // 模拟数据请求操作
      pagination.total = data.length // 模拟 total 设置操作
      loading.spinning = false
    }, 1000)
  }
  const pagination = reactive({
    current: 1,
    pageSize: 10,
    total: 0,
    showQuickJumper: true,
    showSizeChanger: true,
    small: false,
    onPageChange: dataChange,
    onPageSizeChange: dataChange
  })
  onMounted(() => getData())
</script>
```

### 示例：index71

```vue
<template>
  <PacvueTable ref="tableRef" sticky :columns="columns" :loading="loading" :dataSource="dataSource">
    <template #bodyCell="bodyCell">
      <TableBodyCell v-bind="bodyCell">
        <template v-if="bodyCell.column.dataIndex === 'isPacing'">
          <PacvueEditbox class="inline-flex" :canDelete="!true" :isActionInSpace="true"
            v-model="dataSource[bodyCell.index].campaignDetialType" :column="bodyCell.column"
            :record="dataSource[bodyCell.index]" :canEdit="!true" multiple @iconMouseEnter="iconMouseEnter"
            @iconClick="iconClick"></PacvueEditbox>
        </template>
        <template v-else>
          <span>{{ bodyCell.text }}</span>
        </template>
      </TableBodyCell>
    </template>
    <template #headerCell="headerCell">
      <TableHeaderCell v-bind="headerCell">
        <template #textWarp>
          {{ headerCell.title }}
        </template>
        <template #icon="{ column }">
          <el-icon v-if="column.dataIndex === 'isPacing'">
            <ElemeFilled />
          </el-icon>
        </template>
      </TableHeaderCell>
    </template>
  </PacvueTable>
</template>
<script setup>
  import { reactive, ref, onMounted } from 'vue'
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
      dataIndex: 'isPacing',
      title: 'isPacing',
      // orderByField: 'isControl',
      actionListFormat: (record, column) => {
        if (record.key == 0) {
          return [
            { component: 'PacvueIconCommerceChecked', disabled: false, tooltip: 'aaaa' },
            { component: 'PacvueIconCommercePacvueTools', disabled: false, tooltip: 'bbb' },
            { component: 'PacvueIconConfirm', disabled: !true, tooltip: 'ccc' }
          ]
        } else if (record.key == 1) {
          return [
            { component: 'PacvueIconCommerceChecked', tooltip: 'aaaa' },
            { component: 'PacvueIconConfirm', tooltip: 'ccc' }
          ]
        } else {
          return [{ component: 'PacvueIconCommerceChecked', tooltip: 'aaaa' }]
        }
      },
      widthType: 'number'
    },
    {
      key: 'keywordText',
      dataIndex: 'keywordText',
      title: 'Keyword',
      minWidth: 250,
      drag: true,
      resizable: true,
      align: 'right',
      orderByField: 'keywordText'
    },
    {
      key: 'matchType',
      dataIndex: 'matchType',
      title: 'Bidding Strategy',
      drag: true,
      resizable: true,
      minWidth: 130,
      orderByField: 'matchType'
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
  const tableRef = ref()
  const dataSource = ref([])
  const widthchange = ref(true)
  // 请求后端数据
  const getData = () => {
    loading.spinning = true
    setTimeout(() => {
      dataSource.value = data // 模拟数据请求操作
      pagination.total = data.length // 模拟 total 设置操作
      loading.spinning = false
    }, 1000)
  }
  const pagination = reactive({
    current: 1,
    pageSize: 10,
    total: 0,
    showQuickJumper: true,
    showSizeChanger: true,
    small: false,
    onPageChange: dataChange,
    onPageSizeChange: dataChange
  })
  onMounted(() => getData())
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| pagination | 分页器，参考本页配置项及官方文档，设为 false 时不展示和进行分页 | Object \| false | false |
| scrollTop | 是否显示顶部横向滚动条 | Boolean | true |
| columns | 列信息配置参数，则开启列自适应宽度功能，其他项查看官方文档 | Array | -- |
| sticky | 设置粘性头部和滚动条 | boolean \| {offsetHeader?: number, offsetScroll?: number, getContainer?: () => HTMLElement} | false |
| dataSource | 表格列的配置描述 | Array | -- |
| loading | 表格 loading 状态对象，不配置则不显示 loading 状态 | { spinning: false } | -- |
| autoLoading | 是否开启自动 loading ，自动 loading 会和 props.loading 共同控制 loading 状态，在 table 渲染慢时或 columns 变化时自动开启或延长 loading 时间。 | Boolean | true |
| showAction | 是否开启 action 显示功能 | Boolean | false |
| actionType | action 的显示模式，一共有两种模式：default \| small \| showcase | String | default |
| showSorterTooltip | 表头显示下一次排序的 tooltip 提示, 覆盖 table 中 showSorterTooltip | boolean \| Tooltip props | false |
| rowSelection | 行勾选功能配置参是，详情请查看具体配置项 | object | -- |
| rowTotalData | total 数据对象 | object | -- |
| totalFormat | total 数据的格式化函数 | (totalVal, column) => res:String | -- |
| rowTotalShow | 是否展示 total 数据行 | Boolean | false |
| serverSorter | 后端排序配置属性，此属性与前端排序互斥，详情请查看 serverSorter 属性详细文档 | Object | -- |
| childrenColumnName | table dataSource 有子行时使用，指定树形结构的列取值字段。 | String | children |
| summaryFixed | 固定总结栏 | top \| bottom | bottom |
| expandTip | 当出现展开行时，展开图标的 tip 提示文字，不设置则不展示 | String | -- |
| widthFixedByColumns | 表格按照自适应列宽设置父容器宽度，当父容器宽度不固定时 | Boolean | false |
| innerScrollbar | 顶部滚动条是否在表格内显示，在表格 hover 时显示 | Boolean | false |
| scrollHoverShow | 顶部滚动条是否 hover 才显示 | Boolean | false |
| scrollAlwaysShow | 始终保留顶部滚动条占位高度 | Boolean | false |
| autoHeaderHeight | 是否自动表头高度，开启后会全量加载表头部分，有一定的性能损耗。 | Boolean | false |
| emptyText | 无数据时的提示文字 | String | No data found! |
| animateRows | 是否开启动画 | Boolean | true |
| pageSelectData | 分页器 pageSize 切换下拉菜单自定义属性 | Array | `     [       { value: 10, label: '10/page' },       { value: 20, label: '20/page' },       { value: 50, label: '50/page' },       { value: 100, label: '100/page' }     ]     ` |
| customCell | 设置单元格属性, column 如配置了 customCell, 优先使用 column.customCell，详细使用查看原生文档。 | Function(obj: {record: any; rowIndex: number; column: ColumnType}) | -- |
| headerHeight | 自定义表头高度 | Number | 48 |
| tableSummarySize | 当需要渲染多行 total 时需要配置，渲染的行数 | Number | 1 |
| emptyHeight | 无数据时样式的高度，可以是任意 height 的 css 属性。 | String | max-content |
| colSpanFormat | 总结栏的列合并规则函数，返回参考官方文档。 | ({ index, rowIndex, column }) => colSpan: number | () => 1 |
| autoColumnWidth | 是否开启表格的自适应列宽计算，默认开启。 | Boolean | true |
| rowHoverDelay | 表格行 hover 延时，用于性能优化 | number | 10 |
| expandedRowKeys | 当有子行或子table时，用于控制展开指定行 | string[] | -- |
| noHoverBackground | table hover 时是否有背景色，默认有背景色（false）。 | Boolean | false |
| ellipsis | 超过宽度将自动省略。 | Boolean | true |
| rowHeight | 配置行高，组件内部默认会根据 size 自动调整高度，如果需要自定义高度可使用该属性 | number \| ((p: Record<any, any>, isExpandRow: boolean, baseHeight: number) => number | 52 |
| columnDiffKeys | 判断当 column 的哪些属性发生 变化时触发 table 重绘。 | Array | -- |
| scroll | 指定滚动区域的宽、高，内容不足则高度自动收缩 | {y: string \| number,x: string \| number \| max-content} | -- |
| overflowYScroll | table Y轴滚动条展位是否常有，默认常有开启。 | Boolean | true |
| manualRowBorder | table 行边框显示过细时可以开启此属性进行兼容。 | Boolean | false |
| rightBoxShadowShow | table 有右侧固定列时是否显示滚动时的阴影 | Boolean | false |
| defaultExpandAllRows | 初始时，是否展开所有行 | Boolean | false |
| expandedRowHide | 该属性为一个回调函数，用于配合 expandedRowRender 插槽一起使用，用于指定不需要显示展开箭头的行。函数返回true则隐藏箭头，false则显示 | (record, column, index) => boolean | -- |
| customSummaryRow | 自定义添加到总结栏 行 上的属性, 可以是 calss、style等任意属性。 | function | (totalData, rowIndex) => { class: "custom-class", ... } |
| customSummaryCell | 自定义添加到总结栏 行中每一列 上的属性, 可以是 calss、style等任意属性。 | function | (totalData, column, rowIndex, cellIndex) => { class: "custom-class", ... } |
| showBorderTop | table 首行的边框是否需要显示，默认显示 | Boolean | true |
| onepScreenAuto | 列宽自适应时，部分列冻结宽度 的列宽不足一屏时分配模式，需要的 column 配置 freezeWidth 为 true | Boolean | false |
| expandIcon | 当设置了子 table 时生效，用于控制展开图标的显示，return true 则显示， 不设置此属性则全展示。 | ({ expandable, expanded, onExpand, prefixCls, record }) => boolean | -- |
| usePacvuePaginationNew | 是否使用 PacvuePaginationNew 作为 table 分页器组件，配置方式请查看 PacvuePaginationNew 相应的配置文档。 | boolean | false |
| customRow | 设置行属性，详细用法请看原生文档 | Function(record, index) | -- |
| tableRowCheck | 自定义table 行点击事件，配置此属性后，会给鼠标点击的行添加选中样式。 | (event, record) => {} | -- |
| rowClassName | 用于给表格行添加自定义类名 | Function(record, index):string | -- |
| defaultRowCheck | 设置了 tableRowCheck 后生效，使用该属性在每次table重新渲染时设置默认选中行。datalist 为table的data数组，将需要选中的行数据筛选出来并返回即可(返回值只可以是datalist中的某个对象或null)。 | (datalist) => record \|\| null | -- |
| expandLoadingEffect | 当子列展开按钮点击时是否需要展示loading样式，默认不展示。该属性需要配合 table 的实例函数 stopIconLoading 一起使用，控制loading的关闭。 | Boolean | false |
| arrowClickScroll | 滚动条左右箭头是否开启点击触发滚动功能，默认开启。 | Boolean | true |
| columnDefaultoffset | 自适应列宽计算时使用，给每一列默认增加的宽度，用于宽度计算错误时微调，不推荐业务中使用。 | Number | 0 |
| tableChangeScrollToTop | 当使用内部滚动条时，如果table数据重新渲染，是否重置y轴滚动条位置，默认重置。 | Boolean | true |
| autoWidthContrast | 列宽自动计算时，用于自定义单元格内容宽度比较规则。入参为：maxElement 当前最宽的单元格的dom；cellElement 正在对比的单元格dom；maxExpandPadding：当前最宽单元格如果在子展开行，它的位置偏移量；expandPadding：正在对比的单元格如果在子展开行，它的位置偏移量；column：当前正在对比的单元格的column信息； | ({ maxElement: HTMLElement, cellElement: HTMLElement, maxExpandPadding: number, expandPadding: number, column: object }) => Boolean | -- |
| fixColumnWidthBorder | table横向滚动时如果有固定列，阴影显示方式 是否使用 固定边框方式，默认不使用。当行数量过大，固定列横向滚动卡顿时可以开启。 | Boolean | false |
| height | 表格整体高度，内容不足高度不会自动收缩。组件高度，支持像素值或百分比 | string \| number | -- |
| checkboxDataCy | table 勾选功能 checkbox 上的自动化测试埋点属性 | string | -- |
| panigationTotalDataCy | table 分页器 total 信息上的自动化测试埋点属性 | string | -- |
| rowHeightType | 表格行高的三种模式：compact(40px) \| standard(52px) \| wide(72px) | String | standard |
| oneScreenBlank | 列宽自适应时，列宽不足一屏时，多余的宽度在最后一列留白，其余列不动。 | Boolean | false |
| autoShrink | table容器变化触发列宽自适应时，总是强制重置列宽为自适应计算后的宽度，再进行一屏分配逻辑。 | Boolean | false |
| visibleAsync | table 容器不可见时是否对 table 内容的渲染进行阻塞，默认阻塞。 | Boolean | true |
| getSelectWidthParent | 开启勾选功能时，table 如果为父子结构，是否要把父节点信息一起放入 rowSelection.rowSelectedList 中抛出。默认不抛出。 | Boolean | false |
| needAllExpand | 当 table 有子 table 时，是否启用子 table 的一键全部展开、关闭功能。默认不启用。 | Boolean | false |
| needClearRowSelect | table 重新渲染时是否清空勾选值。 | Boolean | true |
| selectCustomRender | 用于自定义勾选列 column 对象的 customRender 属性 | Function({record, index}) {} | -- |
| divisionLine | 当有折叠按钮时是否显示分割线 | Boolean | false |
| resizeColumnOnepScreenWidth | 列宽发生拖拽时，是否要重新进行一屏分配计算。默认不需要。 | Boolean | false |
| isAutoNoDragFixed | 是否自动设置固定列不可拖动 | Boolean | false |
| current | 当前页数 | Number | -- |
| pageSize | 每页条数 | Number | -- |
| total | 数据总数 | Number | -- |
| showQuickJumper | 是否显式 快速跳转至某页功能 | Boolean | false |
| showSizeChanger | 是否显式 改变 pageSize 功能 | Boolean | true |
| small | 当为「small」时，是小尺寸分页 | Boolean | false |
| showGotoPage | 是否显式 page 输入数字跳转 功能，small模式下默认值为false，default模式下默认值为true | Boolean | true\|false |
| onPageChange | 页码改变的回调，参数是改变后的页码及每页条数 | Function(current, pageSize, orderAsc, orderByField) | -- |
| onPageSizeChange | pageSize 变化的回调 | Function(current, pageSize, orderAsc, orderByField) | -- |
| hideOnSinglePage | 当分页只有一页时是否隐藏分页器 | Boolean | false |
| hidePageRightOnSinglePage | 单独控制 是否在一页显示得下的时候隐藏右侧分页选择器 | Boolean | true |
| showTooltip | 数据列单元格是否显示 tooltip | Boolean \| (text, record, column) => tooltip: string \| { isEmpth: boolean, text: string } | false |
| sorter | 前端排序配置对象 { compare: 一个用于排序的函数，不设置则使用默认排序方式 } | { compare: Function } | -- |
| sortDirections | 支持的排序顺序，取值为 'descend' 'ascend' | Array | ['descend', 'ascend'] |
| textwrap | 自适应列宽计算时按照单词换行的规则来进行宽度计算。默认不开启 | boolean | false |
| headerTextwrap | 表头文字换行按照单词换行的规则来进行换行。默认不开启 | boolean | false |
| isDynamicWidth | 可以拖拽的列 是否使用 表头最小宽度 来限制 推拽的最小限值，默认按照内容的最大宽度进行限制。 | boolean | false |
| columnWidthQuery | 自适应列宽计算后,需要动态修改计算结果时的回调函数，将需要修改成的 width 返回即可，其中入参 type 为当前回调的触发类型，分为：1、header（表头计算）；2、column（单元格计算）；3、screen（一屏分配计算）； | ({ width, column, type }) => return number | -- |
| autoWidthContrast | 该属性用于判断 是否要对当前列使用 自定义的 单元格内容宽度比较规则。table 配置了 autoWidthContrast（同名属性）后才生效 | Boolean | false |
| widthType | `定义 column 的列宽自动计算类型。info：信息类，固定宽度，不根据内容调整宽度，不设置width时默认280（手动设置则覆盖）。props：属性类，根据单元格内容自动计算宽度，不需要设置width，当列宽分配有多余空间时会自动扩充列宽，最大扩充至280px。number：数值类，内容默认居右，根据单元格内容自动计算宽度，但是会限制最大宽度，不设置 maxWidth 时默认280（手动设置则覆盖）。` | "info" \| "props" \| "number" | -- |
| iconWidth | 设置 widthType 后生效，设置列中图标占位的宽度，用于给当前列宽计算追加图标的宽度。 | Number | -- |
| compareWidth | 配置该属性则开启定制的 compare 列宽自适应计算规则，对比数据时上下行文字取较长的参与列宽计算。对比行的第二行长度需加上图标宽度，如果 compareWidth 为 Number 则使用设置值作为图标宽度，如果 compareWidth 为 Boolean 值则图标宽度为 12。 | Number | -- |
| autoWidthClass | 自适应列宽计算时如果单元格内容比较特殊，需要在计算时自定义样式规则，则使用此属性在计算时给单元格添加自定义 class，计算结束后移除。 | String | -- |
| nameEllipsis | 设置列为Name类型，在文本溢出时会遵循 Row Height 的规则进行换行。 | Boolean | false |
| actionListFormat | 当需要在当前列中使用 PacvueEditbox 渲染内部 action 时,需要配置该属性,用于生成 action 图标列配置对象的函数。优先级低于 PacvueEditbox 中配置的 actionListFormat | (record, column) => <actionOption>[] | -- |
| component | action 图标组件的名称。 | string | -- |
| disabled | 是否禁用，禁用则直接不显示。。是否禁用组件，禁用后无法进行交互 | boolean | -- |
| tooltip | action 图标的 tooltip | string | -- |
| orderAsc | 用于指定排序方式，正序或倒序 | Boolean | -- |
| orderByField | 用于指定需要排序的字段 | String | -- |
| onServerSort | 排序按钮点击回调函数 | Function(type, allSelectType, selectedRowKeys, selectedRows) | -- |
| selectedRowKeys | 指定选中项的 key 数组，需要和 onChange 进行配合 | Array | -- |
| onChange | 选中项发生变化时的回调 | Function(selectedRowKeys, selectedRows) | -- |
| onSelectAll | 全选状态发生变化时的回调 | Function(type, allSelectType, selectedRowKeys, selectedRows) | -- |
| allSelect | 是否开启 current 和 all 全选功能 | Boolean | false |
| rowSelectedList | 选中项的数据存储数组 | Array | -- |
| allSelectType | 当前的全选状态，共有三种状态，""：未全选，current 和 all | "" \| current \| all | -- |
| getCheckboxProps | 选择框的默认属性配置，可用于设置行 checkbox 是否禁用，返回 true 表示禁用，不设置则不禁用。例子：(record) => { return true } | Function(record) { return boolean } | -- |
| pausedHidden | 隐藏禁用的勾选框 | Boolean | false |
| disableFilter | 选择框的默认属性配置，可用于设置行是否不设置 checkbox，返回 true 表示不设置。例子：(record) => { return true } | Function(record) { return boolean } | -- |
| fixed | 把选择框列固定在左边 | boolean | true |
| setDefaultSelect | 用于指定表格初始化渲染时默认的选中行，返回值：需要选中的行的索引数组。 | (dataSource) => [0,1,...] | -- |
| selectedMode | 选中项模式,CrossPage(跨页存储)\|Default(之前默认模式),注意开启跨页存储模式的时候,需要配置needClearRowSelect为false,设置行数据中customId对应key作为唯一值,以及配置setDefaultSelect | String | -- |
| getCheckboxTip | 显示勾选时，tooltip文案生成函数 | (checkboxInfo) => return string \| null | -- |
| type | 勾选功能类型，默认为多选类型。。组件类型或模式 | "radio" \| "checkbox" | "checkbox" |
| column | columns 数组中当前列的对象 | Object | -- |
| title | column 中的 title 字段 | String \| Any | -- |
| record | dataSource 数组中当前行的对象 | Object | -- |
| text | 当前单元格的值 | String\|Any | -- |
| index | 当前行的索引 | Number | -- |
| column | columns 数组中当前列的对象 | Object | -- |
| key | 单元格唯一 key | String | -- |
| column | columns 中当前列的信息 | Object | -- |
| pageData | dataSource 中的数据 | Array | -- |
| total | rowTotalData 中当前列的 total 数据 | any | -- |
| rowTotalData | 存储所有 total 数据的对象 | Object | -- |
| index | 单元格所在列的索引 | Number | -- |
| rowIndex | 根据 tableSummarySize 渲染多行时，每行的索引 | Number | -- |

## 方法 Methods

组件暴露的方法，可通过 ref 调用。

| 方法名 | 说明 | 参数 |
| --- | --- | --- |
| refreshColumnsWidth | 指定一个或多个列的 dataIndex ，重新按照单元格内容自适应调整列宽，该函数为一个 Promise 函数，会在列宽调整完毕后 resolve | (columns: string \| array) => Promise |
| toggleRowSelection | 手动设置表格选中的行，rowSelection 设置后生效， 入参：需要选中的行的索引数组 [...rowIndex] \| "all" \| "current" | ([...rowIndex] \| "current" \| "all") => void |
| clearRowSelection | 清除已经选中的行，rowSelection 设置后生效 | () => void |
| refreshColumnsAndScroll | 重新按照单元格内容自适应调整所有列的列宽，该函数为一个 Promise 函数，会在列宽调整完毕后 resolve | () => Promise |
| stopIconLoading | expandLoadingEffect 设置为 true 时有效，用于关闭子行展开按钮的loading样式。可以传入行的key，用于关闭特定的行，如果不传key则关闭所有行的loading状态。 | (key) => {} |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| resizeColumn | 列宽拖动时触发、 | Function(width, column, action: 'start' \| 'move' \| 'end' ) => boolean \| void |
| actionClick | 当 showAction 为 true 时有效，点击 action 图标时点击事件 | (action, row, column) => {} |
| rowEnter | 鼠标移入 table 行时触发 | ({ event, record, index }) => {} |
| rowLeave | 鼠标移出 table 行时触发 | ({ event, record, index }) => {} |
| loadCompleted | 表格 dataSource 重新渲染完成时触发事件 | () => {} |
| change | 分页、排序、筛选变化时触发 | Function(pagination, filters, sorter, { action: 'paginate' \| 'sort' \| 'filter' }) |
| expand | 点击展开图标时触发 | Function(expanded, record) |
| expandAll | needAllExpand 开启后，点击全部展开图标时触发 | Function(expanded, expandRowKeys) |
| columnDragEnd | 拖拽列结束时触发 | (opt: DragColumnEventInfo) => boolean \| Promise \| void |
| columnsCompleted | 自适应列宽计算完成一轮时触发 | (columns) => void |
| tableScroll | table 横向滚动事件 | (e) => {} |
| tableWidthChange | tablel 列宽发生变化时触发 | () => {} |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| headerCell | v-slot:headerCell="{title, column}"：个性化头部单元格，插槽必须以 TableHeaderCell 组件作为根标签 | TableHeaderCell |
| bodyCell | v-slot:bodyCell="{text, record, index, column, key}"：个性化单元格，插槽必须以 TableBodyCell 组件作为根标签 | TableBodyCell |
| expandedRowRender | 额外的展开行(子 table 展示插槽)，v-slot:expandedRowRender="{record, index, indent, expanded}" | -- |
| summaryCell | v-slot:bodyCell="{total, column, index}: 个性化总结栏，插槽必须以 TableSummaryCell 组件作为根标签 | TableSummaryCell |
| emptyText | 自定义空数据时的显示内容 v-slot:emptyText | -- |
| pagetip | 分页器左侧分页信息中的提示信息 | -- |
| customLeft | 分页器最左侧位置自定义内容展示插槽 | -- |
| default | 用于渲染默认展示的内容 | -- |
| icon | v-slot:listItem="{title, column}"：标题列的自定义图标 | -- |
| textWarp | v-slot:listItem：表头内容中有多个空格时，只在第一个空格发生换行。 | -- |
| expandAllIcon | v-slot:expandAllIcon={isExpand}全部展开切换图标插槽 | -- |
| default | 用于渲染默认展示的内容 | -- |
| listItem | v-slot:listItem="{item, index, record, column}"：当开启了 showAction 属性后可以使用，用于定义每个 action 图标的样式；item：当前 action 配置对象，index：当前 action 在 actionlist 中的索引。 | -- |
| default | 用于渲染默认展示的内容 | -- |
| action | v-slot:action="{index, rowIndex, column}：用于渲染 action 展示的内容 | -- |

## 相关链接

- [Element Plus 文档](https://www.surely.cool/doc/api)

