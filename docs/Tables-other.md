---
component: Tables
submodule: other
category: data
tags: [表格, 数据展示, 列表, other]
aliases: [Table, Tables, 表格]
version: 1.0.0
---

# Tables - 其他示例

> Table 表格基础使用

## 使用示例

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

