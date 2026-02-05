---
component: Transfer
category: form
tags: [穿梭框, 表单, 数据转移]
aliases: [Transfer, 穿梭框]
version: 1.0.0
description: "PacvueTransfer 穿梭框"
---

# Transfer 组件文档

> PacvueTransfer 穿梭框

**分类**: form | **标签**: 穿梭框、表单、数据转移

## 使用示例

### PacvueTransfer 基础使用

```vue
<template>
  <PacvueTransfer
    @nodeChange="allEvents"
    @expandedChange="allEvents"
    @keywordChange="allEvents"
    @selectAll="allEvents"
    :data="tdata"
    :option="option"
    :clearable="true"
  ></PacvueTransfer>
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
        tdata.value = mockData('Campaign', 5, 3)
      }, 1000)
      const option = {
        propsList: [null, { id: 'id1', label: 'label1', children: 'children1' }, { id: 'id2', label: 'label2' }],
        propDefaultCheck: ['Campaign-0-1-3-1'],
        pausedFn: (node) => {
          if (node.source.id === 'Campaign-0-2') return 'Is Paused!!'
        }
      }
      return {
        event,
        tdata,
        option
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

### PacvueTransfer history 模式

```vue
<template>
  <PacvueTransfer ref="historyRef" :data="tdata" :option="option" :mode="'history'" :clearable="true"
    @nodeChange="allEvents" @expandedChange="allEvents" @keywordChange="allEvents" @selectAll="allEvents">
    <template #headerLeft>
      <PacvueTab :tab-position="'top'" class="tree-tag" v-model="tabval">
        <pacvue-tab-pane label="Campaign" name="Campaign"></pacvue-tab-pane>
        <pacvue-tab-pane label="Tag" name="Tag"></pacvue-tab-pane>
      </PacvueTab>
    </template>
    <template #headerRight>
      <PacvueTab :tab-position="'top'" class="tree-tag" v-model="tabval">
        <pacvue-tab-pane label="Campaign" name="Campaign"></pacvue-tab-pane>
        <pacvue-tab-pane label="Tag" name="Tag"></pacvue-tab-pane>
      </PacvueTab>
    </template>
    <template #totalLeft>
      <PacvueSelect @change="tab1change" :data="dataSelect1" v-model="value1" :type="'single'" width="130px" />
    </template>
    <template #paramsLeft>
      <PacvueSelect @change="tab2change" :data="dataSelect2" v-model="value2" :type="'single'" width="130px" />
    </template>
  </PacvueTransfer>
</template>
<script>
  import { ref, reactive, watch } from 'vue'
  import { ElMessage, ElMessageBox } from 'element-plus'
  export default {
    setup(props, ctx) {
      let historyValue = {}
      const dataSelect1 = reactive([
        { value: 'aaa', label: 'aaa' },
        { value: 'ccc', label: 'ccc' }
      ])
      const value1 = ref('aaa')
      const dataSelect2 = reactive([
        { value: 'bbb', label: 'bbb' },
        { value: 'ddd', label: 'ddd' }
      ])
      const value2 = ref('ddd')
      const tab1change = () => {
        console.log(123)
        historyValue[tabval.value] = mockData('aaa', 3, 2)
        tdata.value = historyValue[tabval.value]
      }
      const tab2change = () => {
        console.log(321)
        historyValue[tabval.value] = mockData('bb', 3, 2)
        tdata.value = historyValue[tabval.value]
      }
      const historyRef = ref()
      const allEvents = (...args) => {
        console.log(args)
        console.log(historyRef.value.getCheckedList())
      }
      const tabval = ref('Campaign')
      // 用于缓存右侧树的所有被节点信息，及选中信息
      const rightData = {
        Tag: {},
        Campaign: {}
      }
      // 监听 tab 切换，使用 watch 监听，用于获取 oldVal 进行信息的缓存
      watch(tabval, (newVal, oldVal) => {
        // 调用 setRightTree 设置右侧树数据，并返回右侧树的历史值
        const { tree, list, treeList } = historyRef.value.setRightTree(rightData[newVal])
        // 将历史值缓存起来
        rightData[oldVal] = { tree, list, treeList }
        // 重新设置左侧树
        if (!historyValue[tabval.value]) {
          historyValue[tabval.value] = mockData(newVal, 3, 2)
        }
        // 重绘tree之前，先将默认的选中值设置上
        option.propDefaultCheck = rightData[newVal]?.list ?? []
        tdata.value = historyValue[tabval.value]
      })

      const tdata = ref([])
      setTimeout(() => {
        historyValue[tabval.value] = mockData('Campaign', 5, 3)
        tdata.value = historyValue[tabval.value]
      }, 1000)
      const option = reactive({
        propsList: [null, { id: 'id1', label: 'label1', children: 'children1' }, { id: 'id2', label: 'label2' }],
        propDefaultCheck: ['Campaign-0-1-3-1'],
        pausedFn: (node) => {
          if (node.source.id === 'Campaign-0-2') return 'Is Paused!!'
        }
      })
      return {
        event,
        tdata,
        option
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
<style scoped lang="scss">
  .tree-tag {
    :deep(.el-tabs__header) {
      margin-bottom: 0;

      .el-tabs__item {
        height: 41px;
        line-height: 41px;
      }

      .el-tabs__nav-wrap::after {
        height: 0;
      }
    }
  }

  :deep(.pacvue-select-input) {
    width: 130px;
    height: 32px !important;
  }
</style>
```

### PacvueTransfer quarantine 模式

```vue
<template>
  <PacvueTransfer
    ref="tRef"
    :data="leftTree"
    :option="option"
    :rightData="rightTree"
    :mode="'quarantine'"
    :clearable="true"
    @nodeChange="allEvents"
    @expandedChange="allEvents"
    @keywordChange="allEvents"
    @selectAll="allEvents"
  >
    <template #totalLeft>
      <PacvueSelect @change="tab1change" :data="dataSelect1" v-model="value1" :type="'single'" width="130px" />
    </template>
  </PacvueTransfer>
</template>
<script>
  import { ref, reactive, watch } from 'vue'
  import { ElMessage, ElMessageBox } from 'element-plus'
  export default {
    setup(props, ctx) {
      const dataSelect1 = reactive([
        { value: 'aaa', label: 'aaa' },
        { value: 'ccc', label: 'ccc' }
      ])
      const value1 = ref('aaa')
      const leftTree = ref([])
      const rightTree = ref([])
      const tab1change = (val) => {
        if (val === 'ccc') {
          leftTree.value = mockData1('ccc', 3, 2)
        } else {
          leftTree.value = mockData1('Campaign1', 3, 3)
        }
      }
      const option = {
        propDefaultCheck: ['Campaign1-0-1-1']
      }
      const tRef = ref()
      const allEvents = (...args) => {
        console.log(args)
        console.log(tRef.value.getCheckedList())
      }

      setTimeout(() => {
        leftTree.value = mockData1('Campaign1', 3, 3)
      }, 1000)
      setTimeout(() => {
        rightTree.value = [...mockData1('Campaign1', 3, 3), ...mockData1('ccc', 3, 2)]
      }, 1000)

      return {
        event,
        tdata,
        option
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
<style scoped lang="scss">
  .tree-tag {
    :deep(.el-tabs__header) {
      margin-bottom: 0;
      .el-tabs__item {
        height: 41px;
        line-height: 41px;
      }
      .el-tabs__nav-wrap::after {
        height: 0;
      }
    }
  }
  :deep(.pacvue-select-input) {
    width: 130px;
    height: 32px !important;
  }
</style>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| mode | 穿梭树的模式，共有三种模式，default：穿梭树左右结构同步变化。history：右侧树会记忆左侧树所有的选中节点，当左侧树变化时不会清除历史选中节点。quarantine：左侧树结构和右侧树结构可以不一致，根据叶节点id进行匹配。 | "default" \| "history" \| "quarantine" | default |
| showKeywordLeft | 是否显示左侧关键词筛选 input | boolean | true |
| showKeywordRight | 是否显示右侧关键词筛选 input | boolean | true |
| showHoverColor | tree 节点悬停是否显示背景色 | Boolean | true |
| isDynamicTooltip | 每一个节点是否开启动态tip(内容超出宽度显示tooltip) | Boolean | false |
| isMutuallyExclusive | 是否一级互斥 | Boolean | false |
| filterOutNameless | 节点关键词筛选时如果name为空，是否需要被过滤掉，默认不过滤掉。 | Boolean | false |
| customSelect | 自定义节点筛选逻辑，与默认的name模糊筛选逻辑共同生效。只要有一种筛选命中，就显示节点。需注意在筛选过程中不可以改变node的值。 | (keyword, node, isRight) => boolean | -- |
| titleFormatLeft | 顶部全选的提示文字格式化函数，该函数有两个入参，当前选中节点数，总节点数 | Function | (n, t) => `${n}/${t} items` |
| titleFormatRight | 顶部全选的提示文字格式化函数，该函数有两个入参，当前选中节点数，总节点数 | Function | (n, t) => `${n}/${t} items` |
| filterLeft | `左侧树自定义筛选功能的配置对象 {   // 自定义筛选的筛选类型   customSelect: 'xxx',   // 自定义筛选的选中状态取值字段   filterKey: 'xxx',   // 自定义选中状态设置的回调函数   initFn: (treeNode, customSelect, filterKey) => {     const filterType = /** 自定义 节点筛选状态 生成逻辑 **/     treeNode[filterKey] = filterType   } }` | Object | -- |
| filterRight | `右侧树自定义筛选功能的配置对象 {   // 自定义筛选的筛选类型   customSelect: 'xxx',   // 自定义筛选的选中状态取值字段   filterKey: 'xxx',   // 自定义选中状态设置的回调函数   initFn: (treeNode, customSelect, filterKey) => {     const filterType = /** 自定义 节点筛选状态 生成逻辑 **/     treeNode[filterKey] = filterType   } }` | Object | -- |

## 方法 Methods

组件暴露的方法，可通过 ref 调用。

| 方法名 | 说明 | 参数 |
| --- | --- | --- |
| setRightTree | 仅 mode 为 history 时可以使用，传入新的树节点及选中项，重新渲染右侧树结构，并返回历史数据 | ({ tree, list }) => return { tree, list } |
| refreshTree | 重新刷新 tree 数组显示样式，当某些操作使 tree 显示样式异常时可以使用。 | () => {} |
| setTreePaused | 设置节点的禁用状态: keys 需要设置状态的节点的 id, 可以为单个 id 或 id 数组 , type 节点的禁用状态(Boolean)，tooltip 提示文字 | (keys, type, tooltip) => void |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| headerLeft | 左侧树组件顶部添加样式插槽 | -- |
| headerRight | 右侧树组件顶部添加样式插槽 | -- |
| footLeft | 左侧树组件底部添加样式插槽 | -- |
| footRight | 右侧树组件底部添加样式插槽 | -- |
| totalLeft | 左侧树全选 checkbox 右侧位置添加样式插槽 | -- |
| totalRight | 右侧树全选 checkbox 右侧位置添加样式插槽 | -- |
| paramsLeft | 左侧树筛选条件列添加样式插槽 | -- |
| paramsRight | 右侧树筛选条件列添加样式插槽 | -- |
| empty | 组件左侧树无数据时样式插槽，不设置则使用默认样式 | -- |
| emptyRight | 组件右侧树无数据时样式插槽，不设置则使用默认样式 | -- |
| itemRender | v-slot:itemRender="node, isRight"：单个节点样式插槽，不设置则展示默认 label，isRight 用于区分左右树。 | -- |
| tooltip  | 节点中tooltip插槽（注意：只有isDynamicTooltip开启的时候，才会有作用） | -- |
| aside  | 节点中右边内容的占位符（注意：只有isDynamicTooltip开启的时候，才会有作用 | -- |

## 相关链接

- [Element Plus 文档](outlink)

