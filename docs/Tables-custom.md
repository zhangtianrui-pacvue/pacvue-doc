---
component: Tables
submodule: custom
category: data
tags: [表格, 数据展示, 列表, custom]
aliases: [Table, Tables, 表格]
version: 1.0.0
---

# Tables - 自定义配置

> Table 表格基础使用

## 使用示例

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

