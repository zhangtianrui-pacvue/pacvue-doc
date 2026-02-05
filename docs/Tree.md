---
component: Tree
category: data
tags: [树形控件, 层级数据, 树]
aliases: [Tree, 树]
version: 1.0.0
description: "Tree 树"
---

# Tree 组件文档

> Tree 树

**分类**: data | **标签**: 树形控件、层级数据、树

## 使用示例

### PacvueTree 树形组件的一般使用

```vue
<template>
  <PacvueTree @nodeChange="allEvents" @expandedChange="allEvents" @keywordChange="allEvents" @selectAll="allEvents"
    :useNewTextWrap="true" :autoResize="true" :data="tdata" :option="option" :clearable="true">
  </PacvueTree>
</template>
<script>
  import { ref } from 'vue'
  import { ElMessage, ElMessageBox } from 'element-plus'
  export default {
    setup(props, ctx) {
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
        tdata,
        option,
        allEvents
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
| data | tree 的数据对象, 每个数组对象结构示例：{ id, label, children }，id为节点唯一标识，label 为节点展示文字，children 表示节点的子节点 | Array | -- |
| option | 渲染 tree 时需要使用的配置对象，详情查看 option 详细配置信息 | Object | -- |
| height | 组件中树形展示部分的高度，此高度设置 不是 设置组件本身高度 | String | 300px |
| showCheckbox | 是否显示树节点的 checkbox | Boolean | true |
| showCheckall | 是否显示顶部全选 checkbox | Boolean | true |
| showItemCheckbox | 是否显示树节点的 checkbox，支持传入函数，根据节点数据返回是否显示 | Function | true |
| titleFirst | 是否全选 checkbox 显示在 关键词筛选 input 之上 | Boolean | true |
| autoResize | 当树结构高度低于 height 属性时是否需要动态调整高度 | Boolean | false |
| tooltip | 树节点文字是否显示 tooltip | Boolean | false |
| clearable | 关键词筛选 input 是否打开 清除关键词 功能 | Boolean | false |
| keeps | 视口中渲染的节点个数，不指定的话则自动计算 | Number | -- |
| showKeyword | 是否显式关键词筛选 input | Boolean | true |
| oneSize | 手动设置单个节点的行高 | Number | 38 |
| onlyLeaFCheck | 当有多个同级的叶节点时，同级叶节点只能单选，非叶节点只能展开，不能勾选。 | Boolean | false |
| onlyLeaFCheckShow | 只显示叶节点的 checkbox | Boolean | false |
| onlyOneSetCheck | 只能同时勾选一个根节点的子节点 | Boolean | false |
| defaultExpanded | 是否默认展开子节点 | Boolean | true |
| backToTop | tree 重新渲染是是否自动回到顶部 | Boolean | true |
| showHoverColor | tree 节点悬停是否显示背景色 | Boolean | true |
| sort | 实例函数 getCheckedList 返回值是否按照顺序排序 | Boolean | false |
| isDynamicTooltip | 每一个节点是否开启动态tip(内容超出宽度显示tooltip) | Boolean | false |
| pausedTooltipAlone | 节点禁用时的 tooltip 单独显示，不占用 title 的 tooltip 位置，该功能需要 tooltip 配置为 true | Boolean | false |
| treeGroupOpen | 开启分组节点显示功能，分组节点必须为根节点且没有子节点，开启后还需要设置 option.treeGroup | Boolean | false |
| transformToString | 是否要将 tree 的唯一 id 统一转换成 String 类型，默认不转换。 | Boolean | false |
| useNewTextWrap | 使用 内容在换行时 上下边距（15px）相等 的显示规则，并且支持 内容动态高度， 默认不开启。 | Boolean | false |
| emptyText | 无数据时的提示文字 | String | "No Data Found!" |
| isMathParentShowFull | 是否需要匹配父的节点显示所有子的列表 | Boolean | true |
| freezeNode | 一个回调函数，用于判断是否冻结某个节点，节点冻结后将不可改变其初始状态 | (node) => return boolean | -- |
| isEmptyShowAll | 是否当前显示的data列表为空时显示SelectAll功能 | Boolean | true |
| autoReload | data 发生变化时是否重新渲染tree组件 | Boolean | true |
| filterOutNameless | 节点关键词筛选时如果name为空，是否需要被过滤掉，默认不过滤掉。 | Boolean | false |
| isReserveSpaceForCheckbox | 用于隐藏 checkbox 时，是否保留空间给checkbox,默认不保留。 | Boolean | false |
| isLeafSingleCheck | 是否只有叶子节点可以勾选的时候只能单选 | Boolean | true |
| max | 数据可勾选的个数上限，如果 tree 为单选模式则失效。 | Number | -- |
| min | 数据可勾选的个数下限，如果 tree 为单选模式则失效。 | Number | -- |
| id | 节点唯一标识取值字段 | String | id |
| label | 节点展示文字取值字段 | String | label |
| children | 节点的子节点数组取值字段 | String | children |
| apply | 节点的 apply 属性取值字段 | String | isApplied |
| type | tree 模式：单选或多选，默认为多选。组件类型或模式 | single \| multiple | multiple |
| pausedFn | 禁用状态的过滤函数，该函数传入参数为当前循环的节点，在此函数中判断节点是否需要禁用，需要禁用则返回一个字符串，该字符串将用于禁用节点的 tooltip 提示，不许禁用则不返回 | Function(node) | -- |
| treeGroup | 如果 treeGroupOpen 为 true 生效，用于确定哪些节点为分组节点，返回 true 表示是分组节点。 | Function(node) { return Boolean } | -- |
| propsList | 当 tree 中某一层级的 id、label、children 的取值字段需要自定义时设置，设置为一个数组，哪一个层级的字段需要自定义，则在数组的哪个索引上设置相应字段，之前的层级设置为 null 即可，例子：tree 的第二层的取值字段需要自定则 props.option.propsList = [null, {id: myid, label: mylable, children: mychildren}] | Array | -- |
| titleFormat | 顶部全选的提示文字格式化函数，该函数有两个入参，当前选中节点数，总节点数 | Function | (n, t) => `${n}/${t} items` |
| propDefaultCheck | 需要在 tree 初始化时默认选中的节点 | Array | -- |
| isTrueId | tree 节点 id 是否不重复，当节点 id 可能重复时需要设置此属性。true：不重复。false：可能重复 | Boolean | true |
| singleInverseSelect | 单选模式下节点是否可以反选，默认不可反选。 | Boolean | false |
| defaultCheckKey | 将原数组中某一属性作为默认选中设置的依据。 | String | -- |
| filter | `自定义筛选功能的配置对象 {   // 自定义筛选的筛选类型   customSelect: 'xxx',   // 自定义筛选的选中状态取值字段   filterKey: 'xxx',   // 自定义选中状态设置的回调函数   initFn: (treeNode, customSelect, filterKey) => {     const filterType = /** 自定义 节点筛选状态 生成逻辑 **/     treeNode[filterKey] = filterType   } }` | Object | -- |

## 方法 Methods

组件暴露的方法，可通过 ref 调用。

| 方法名 | 说明 | 参数 |
| --- | --- | --- |
| itemClick | 调用则触发单个节点点击 | (id, checkType:Boolean) => void |
| expandedClick | 调用触发节点展开关闭 | (id, isOpen:Boolean) => void |
| keywordChange | 调用触发关键词筛选 | (keyword) => void |
| selectAllClick | 调用触发全选全不选，checkType：需要设置的选中状态。publish：是否触发事件。widthoutFilter：全选设置的结果 不受 关键词筛选影响，默认受影响。 | (checkType:Boolean, , publish:true, widthoutFilter:false) => void |
| getCheckedList | 获取当前选中的节点id数组 | () => [...ids] |
| setCheckedList | 批量设置节点选中状态 | (ids:Array, checkType) => void |
| reloadTree | 强制重新生成tree节点数据并重新渲染, callback: 可以传入一个回调函数，在重新渲染成功后调用。 | (callback) => void |
| getCheckedTree | 获取当前选中的节点数据，返回树形结构数组，入参 keys：需要取值的字段不指定则取所有值，childKey：children 数组的取值字段，不指定则使用默认设置的值 | (keys: array, childKey: string) => [...data] |
| setTreePaused | 设置节点的禁用状态: keys 需要设置状态的节点的 id, 可以为单个 id 或 id 数组 , type 节点的禁用状态(Boolean)，tooltip 提示文字 | (keys, type, tooltip) => void |
| setCustomSelect | 设置自定义筛选条件的选中值 | (selectValue) => void |
| setTreePausedPro | 设置节点禁用状态及禁用tooltip文案。 | (id, pausedType, tooltip) => void |
| refreshTree | 重新刷新 tree 数组显示样式，当某些操作使 tree 显示样式异常时可以使用。 | () => void |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| nodeChange | 单个节点点击事件 | id, checkType, { itemInfo } |
| expandedChange | 单个节点展开关闭事件 | id, isOpen |
| keywordChange | 关键词筛选事件 | keyword |
| selectAll | 全选状态改变事件 | checkType |
| treeInit | tree 创建完成事件 | -- |
| treeScroll | tree 滚动事件事件 | event |
| rightClick | tree 单行鼠标右击事件 | (event, node) => void |
| customRowClick | tree 单行鼠标左击事件 | (node) => void |
| optionChange | option 配置发生变化时触发事件 | () => void |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| header | 组件顶部添加样式插槽 | -- |
| foot | 组件底部添加样式插槽 | -- |
| empty | 组件无数据时样式插槽，不设置则使用默认样式 | -- |
| itemRender | v-slot:itemRender="node, isRight"：单个节点样式插槽，不设置则展示默认 label，isRight 是在穿梭框中使用时，用于区分左右树。 | -- |
| total | 全选 checkbox 右侧位置添加样式插槽 | -- |
| params | 在全选 checkbox 与 关键词筛选 input 之间的位置添加样式插槽 | -- |
| paramsButtom | 在关键词筛选 input 与 tree 之间的位置添加样式插槽 | -- |
| tooltip  | 节点中tooltip插槽（注意：只有isDynamicTooltip开启的时候，才会有作用） | -- |
| aside  | 节点中右边内容的占位符（注意：只有isDynamicTooltip开启的时候，才会有作用 | -- |

