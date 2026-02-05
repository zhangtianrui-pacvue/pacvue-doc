---
component: PacvueDataTable
category: data
tags: [数据表格, 表格]
aliases: [PacvueDataTable]
version: 1.0.0
description: "Table 使用组件自带fetchData以及fetchTotalData的服务端分页"
---

# PacvueDataTable 组件文档

> Table 使用组件自带fetchData以及fetchTotalData的服务端分页

**分类**: data | **标签**: 数据表格、表格

## 使用示例

### 注意 1.fetchData返回的数据的结构Promise&lt;{Data:Array

```vue
<template>
  <PacvueDataTable sticky v-model:columns="columns1" :isServer="true" :fetchData="fetchData" :requestId="requestId"
    :useAction="useAction" :showAction="true" :actionType="'auto'">
    <template #headerItem="headerCell">{{ headerCell.title }}</template>
    <template #headerCellTip="headerCell">
      <el-icon>
        <ElemeFilled />
      </el-icon>
    </template>
    <template #cellItem="bodyCell">{{ '-' + bodyCell.text }}</template>
  </PacvueDataTable>
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

  var fetchData = (query) => {
    return new Promise(async (resolve) => {
      const report = await mockDate('report')
      var Data = dataFormat(report.data)
      resolve({
        Data,
        PageInfo: {
          OrderAsc: false,
          OrderByField: 'Spend',
          OrderString: 'spend desc',
          PageCount: 199,
          PageIndex: 1,
          PageSize: 25,
          TotalDataCount: Data.length
        }
      })
    })
  }
  var useAction = (rowData) => {
    return [
      {
        label: 'detail',
        value: 'Detail',
        icon: 'ElemeFilled',
        tip: 'Detail',
        onClick: function ({ rowData, column }) { }
      },
      {
        label: 'budget',
        value: 'Budget',
        icon: 'PacvueIconBudgetSchedule',
        tip: 'Budget',
        onClick: function ({ rowData, column }) { }
      }
    ]
  }
  var requestId = ref(0)
  setTimeout(() => {
    requestId.value = new Date().getTime()
  }, 1000)
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| isServer | 是否是服务器端渲染 | Array | -- |
| loading | 是否开启loading功能。是否显示加载状态 | Boolean | false |
| data | 表格列的配置描述。数据源，用于渲染组件内容 | Array | -- |
| totalData | total 数据对象 | object | -- |
| fetchData | 服务器端渲染时，获取列表数据 | Promise | -- |
| fetchTotalData | 服务器端渲染时，获取total数据 | Promise | -- |
| useAction | 获取action列表, | (rowData) => array | -- |
| isShowChildren | 是否显示行子列表,返回布尔值 | ({rowData:object, dim, query:object}) => boolean | -- |
| multiSort | 排序字段, | Array<{sortType:String,sortData:String}> | [{ sortType: "desc", sortData: "Spend" }] |
| requestId | 是否发起请求的唯一标志, | [Number, String] | -- |
| selectAllType | 全选类型，current \|\| all | String | current |
| query | 查询参数 | Object | {} |
| formatQuery | 查询参数的格式化方法 | (query)=>object | (query)=>query |
| isChildrenDate | 是否date列在children中 | boolean | false |
| showCheckbox | 是否显示checkbox框 | boolean | false |
| checkboxPausedHidden | 隐藏禁用的勾选框 | Boolean | true |
| disableCheckbox | 选择框的默认属性配置，可用于设置行是否不设置 checkbox，返回 true 表示不设置。例子：(record) => { return true } | Function(record) { return boolean } | -- |
| columnDiffKeys | 判断当 column 的哪些属性发生 变化时触发 table 重绘。 | Array | ["widthUniqueId"] |
| useTopCurrency | 是否使用最顶级数据的currentSymbol | boolean | false |
| fnServerRepsonse | 格式化请求数据 | Function | -- |
| isHasLastOrder | 是否最后一个order字段的排序方向是否放在排序字段后面 | boolean | false |
| orderByName | pageInfo中排序字段的属性名称 | String | orderByField |
| isKeepExpand | 是否支持刷新页面保持展开状态 | Boolean | true |
| mulOrderSplit | multiSort中一个字段按多字段排序分隔符 | String | -_- |
| isStoreWidth | 是否开启存储宽度功能 | Boolean | false |
| storeSortKey | 存储宽度的唯一键 | String\|Number | -- |
| actionType | table中action的类型，auto\|default | String | default |
| isActionExpand | action类型auto的时候，是否是展开 | Boolean | false |
| smallPagination | 是否是小页码 | Boolean | false |
| showQuickJumper | 是否显式 快速跳转至某页功能 | Boolean | true |
| showSizeChanger | 是否显式 改变 pageSize 功能 | Boolean | true |
| actionToggleThrold | actionType类型为auto时,有展开功能的阀值 | Number | 2 |
| formatRow | 格式化行数据 | (rowData)=>Object | -- |
| formatTotalRow | 格式化total行数据 | (totalData)=>Object | -- |
| isFirstClientFetch | 是否客服端分页但需要使用组件中请求接口 | Boolean | false |
| keepSelectAll | 是否开启selectall中的反选功能 | Boolean | false |
| customUUId | 行数据的唯一性标志 | ({ rowData, rowIndex, parentRowIndex, parentRowData, pageInfo })=>String\|Number | -- |
| defaultMultiSort | 默认的排序字段, | Array<{sortType:String,sortData:String}> | [] |
| originColumns | 所有column列表(为了方便对排序字段进行过滤), | Array | [] |
| isMultiSortFilterByVisibleColumn | 是否通过当前可显的columns字段进行过滤, | Boolean | false |
| formatMultiSort | 对排序字段进行过滤, | Function(multiSort:Array<{sortType:String,sortData:String}>) | -- |
| pageSize/v-model:pageSize | 一页显示多少条数据 | Number | 25 |
| hideOnSinglePage | 是否一页的时候，隐藏页码选择器 | Boolean | false |
| hidePageRightOnSinglePage | 单独控制 是否一页的时候，隐藏右侧分页选择器 | Boolean | true |
| rowHeight | 配置行高，组件内部默认会根据 size 自动调整高度，如果需要自定义高度可使用该属性 | number \| ((p: Record<any, any>, isExpandRow: boolean, baseHeight: number) => number | -- |
| rowHeightType | 表格行高的三种模式:compact(40px) \| standard(52px) \| wide(72px) | String | standard |
| oneScreenBlank | 列宽自适应时，列宽不足一屏时，多余的宽度在最后一列留白，其余列不动。 | Boolean | false |
| pageSizeList | 分页器pageSize列表 | Array | [25, 50, 100] |
| toggleWidthCellConfig | 可以动态改变切换cell宽度的配置, | Object<isFold:Boolean,computeWidth:Function({ record, rowIndex, isFold }) | -- |
| visibleAsync | table 容器不可见时是否对 table 内容的渲染进行阻塞，默认阻塞。 | Boolean | true |
| selectedMode | 选中项模式,CrossPage(跨页存储)\|Default(之前默认模式),注意开启跨页存储模式的时候,需要配置needClearRowSelect为false,以及配置customUUId | String | -- |
| isHighUseWidthCache | 是否优先使用缓存中的宽度 | Boolean | false |
| customStoreWidth | 自定义存储以及获取宽度缓存 | ({key: string, value: any, type: set\|get})=>Promise | false |
| createCheckboxTip | 自定义checkbox提示 | (node,{isPaused:Boolean, selectionMode:String})=>String | -- |
| totalTextConfig | total显示的标题配置 | {[index]:String} | -- |
| tableSummarySize | total显示的行数 | Number | 1 |
| paginationStickyBottom | 分页器粘性布局时底部位置 | String | -1px |
| beforeFetch | 请求数据前回调函数 | ({query: object, visibleColumns: array}) => void | -- |
| totalAutoColumnWidth | 是否开启total列自动宽度计算 | Boolean | true |
| tip | 数据列单元格中自定义tip的内容 | String\|Number | -- |
| showTooltip | 数据列单元格是否显示 tooltip | Boolean | false |
| sorter | 前端排序配置对象 { compare: 一个用于排序的函数，不设置则使用默认排序方式 } | { compare: Function } | -- |
| sortDirections | 支持的排序顺序，取值为 'descend' 'ascend' | Array | ['descend', 'ascend'] |
| textwrap | 自适应列宽计算时按照单词换行的规则来进行宽度计算。默认不开启 | boolean | false |
| headerTextwrap | 表头文字换行按照单词换行的规则来进行换行。默认不开启 | boolean | false |
| isDynamicWidth | 可以拖拽的列 是否使用 表头最小宽度 来限制 推拽的最小限值，默认按照内容的最大宽度进行限制。 | boolean | false |
| columnWidthQuery | 自适应列宽计算后,需要动态修改计算结果时的回调函数，将需要修改成的 width 返回即可，其中入参 type 为当前回调的触发类型，分为：1、header（表头计算）；2、column（单元格计算）；3、screen（一屏分配计算）； | ({ width, column, type }) => return number | -- |
| autoWidthContrast | 该属性用于判断 是否要对当前列使用 自定义的 单元格内容宽度比较规则。table 配置了 autoWidthContrast（同名属性）后才生效 | Boolean | false |
| widthType | `定义 column 的列宽自动计算类型。info：信息类，固定宽度，不根据内容调整宽度，不设置width时默认280（手动设置则覆盖）。props：属性类，根据单元格内容自动计算宽度，不需要设置width。number：数值类，内容默认居右，根据单元格内容自动计算宽度，但是会限制最大宽度，不设置 maxWidth 时默认280（手动设置则覆盖）。` | "info" \| "props" \| "number" | -- |
| iconWidth | 设置 widthType 后生效，设置列中图标占位的宽度，用于给当前列宽计算追加图标的宽度。 | Number | -- |
| compareWidth | 配置该属性则开启定制的 compare 列宽自适应计算规则，对比数据时上下行文字取较长的参与列宽计算。对比行的第二行长度需加上图标宽度，如果 compareWidth 为 Number 则使用设置值作为图标宽度，如果 compareWidth 为 Boolean 值则图标宽度为 12。 | Number | -- |
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
| setDefaultSelect | 用于指定表格初始化渲染时默认的选中行，返回值：需要选中的行的索引数组 [...rowIndex] \| "all" \| "current"，例子：(dataSource) => [...rowIndex] | (dataSource) => { return [...rowIndex] \| "current" \| "all" } | -- |
| pausedHidden | 隐藏禁用的勾选框 | Boolean | false |
| fixed | 把选择框列固定在左边 | boolean | true |
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
| stopIconLoading | expandLoadingEffect 设置为 true 时有效，用于关闭子行展开按钮的loading样式。 | () => {} |
| refreshData | expandLoadingEffect 设置为 true 时有效，用于关闭子行展开按钮的loading样式。 | () => {} |
| updateCell | 指定行下标，更新对应的行数据中prop值。 | ({ rowIndex, prop, value, isRefreshWidth = true }):void |
| updateRow | 更新行数，其中：rowIndex 可以当前的行数据，也可以是当前的行下标数组，value 更新的map对象，isRefreshTotal 是否刷新行数据，默认为false，isRowIndex rowIndex是否是行下标，isSet 是否rowData中一个字段值赋值给另一个字段 | ({ rowIndex, value = {}, isRowIndex = true, isSet = false })=>void |
| updateTotal | 更新total数据。 | (totalData) =>void |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| actionClick | 当 showAction 为 true 时有效，点击 action 图标时点击事件 | (action, row, column) => {} |
| rowEnter | 鼠标移入 table 行时触发 | ({ event, record, index }) => {} |
| rowLeave | 鼠标移出 table 行时触发 | ({ event, record, index }) => {} |
| loadCompleted | 表格 dataSource 重新渲染完成时触发事件 | () => {} |
| pageSizeChange | pageSize改变事件 | ({pageIndex,pageSize,orderAsc,orderByField}) => {} |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| headItem | v-slot:headItem="{title, column}"：个性化头部单元格 | -- |
| headerCellTip | v-slot:headerCellTip="{title, column}"：个性化头部单元格 | -- |
| cellItem | v-slot:cellItem="{text, record, index, column, key}"：个性化单元格 | -- |
| actionItem | v-slot:actionItem="{text, record, index, column, key}"：个性化单元格 | -- |
| summaryItem | v-slot:summaryItem="{total, column, index}: 个性化总结栏， | -- |
| pagetip | 分页器左侧分页信息中的提示信息 | -- |
| emptyText | 自定义空数据时的显示内容 v-slot:emptyText | -- |

## 相关链接

- [Element Plus 文档](https://www.surely.cool/doc/api)

