---
component: PacvueMultipleFilter
category: filter
tags: [多重筛选, 过滤]
aliases: [PacvueMultipleFilter]
version: 1.0.0
description: "两个Select组合用法"
---

# PacvueMultipleFilter 组件文档

> 两个Select组合用法

**分类**: filter | **标签**: 多重筛选、过滤

## 使用示例

### 示例：index

```vue
<template>
  <PacvueMultipleFilter style="width: 320px" :detail="detail" :labelInner="labelInner" v-model="value2" @isChange="ischange"></PacvueMultipleFilter>
</template>

<script setup>
  import { ref, reactive } from 'vue'
  import { Search } from '@element-plus/icons-vue'
  var ischange = ($event, key) => {
    console.log('>>>>>>>$event', $event, key)
  }
  var labelInner = ref('')
  var value2 = ref({
    postClick: '',
    postView: ''
  })
  var detail = reactive({
    value: {
      postClick: '',
      postView: ''
    },
    label: '',
    extraOption: {
      postClick: {
        type: 'single',
        flex: 'initial',
        filterable: false,
        clearable: false,
        isRequire: true,
        disabled: false
      },
      postView: {
        type: 'multiple', //time multiple
        timeType: 'date'
        //disabled: true
      }
    },
    mapKeys: ['label', 'value'], // select select-tree select-cascader都需要配置这个属性
    itemList: {
      postClick: [
        {
          value: 'campaingTag',
          label: 'Campaing Tag'
        },
        {
          value: 'adgroupTag',
          label: 'Adgroup Tag'
        },
        {
          value: 'keywordTag',
          label: 'Keyword Tag'
        }
      ],
      postView: [
        {
          value: 'Contains',
          label: 'Contaiins sdfsfsaf sdfdsgsdfsd sfagsgdg sgsdgsgsdgsgsdagasg sdfwerwrw ewrewrewrewrwreqwr ewrewrqw erwqrq ewrewqrq erwr erewt tt'
        },
        {
          value: 'not',
          label: 'Not Contains'
        },
        {
          value: 'is',
          label: 'is'
        },
        {
          value: 'StartWith',
          label: 'Start With'
        }
      ]
    },

    render: null, // jsx
    placeholder: {
      postClick: 'please select',
      postView: 'please select'
    }
  })
</script>
```

### 按钮分为中号和小号，分别为 default small 最小宽高：default：88*36px

```vue
<template>
  <PacvueMultipleFilter style="width: 360px" :detail="detail2" :labelInner="''" v-model="value3" @isChange="ischange"></PacvueMultipleFilter>
</template>

<script setup>
  import { ref } from 'vue'
  var ischange = ($event, key) => {
    console.log('>>>>>>>$event', $event, key)
  }
  var value3 = ref({
    postClick: '',
    postView: ''
  })
  var detail2 = {
  value: {
    postClick: '',
    postView: '',
    complextInput:[]
  },
  label: '',
  extraOption: {
    postClick: {
      type: 'single',
      flex: 'initial',
      filterable: false,
      clearable: false,
      isRequire: true
      // disabled: true
    },
    postView: {
      type: 'time',
      timeType: 'daterange',
      //disabled: true,
      style: {
        'margin-left': '0px'
      }
    },
    complextInput:{
      type: 'complexInput',
      attrs:{
        multiple:true
      }
    }
  },
  mapKeys: ['label', 'value'], // select select-tree select-cascader都需要配置这个属性
  itemList: {
    postClick: [
      {
        value: 'campaingTag',
        label: 'Campaing Tag'
      },
      {
        value: 'adgroupTag',
        label: 'Adgroup Tag'
      },
      {
        value: 'keywordTag',
        label: 'Keyword Tag'
      }
    ],
    postView: []
  },

  render: null, // jsx
  placeholder: {
    postClick: 'please select',
    postView: 'please select'
  }
}
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| modelValue/v-model | 双向绑定的值 | Object | -- |
| labelInner | 显示的label名称 | Boolean | false |
| prefixIcon | 前缀的图标 | String | -- |
| fitWidth | 是否根据内容适应宽度 | String | false |
| detail | 详细的配置信息，具体参考下表DetailConfig | Object | {} |
| isByCascaderVal | 是否关联联动值，根据第一个select缓存对应值(只有第一个时单选select，才生效) | Boolean | false |
| cascaderKeyConfig | 关联联动值的映射配置 | Object |  {triggerKey: 'postClick',cascaderKey: 'postView'} |
| isDropdownItem | 是否在任何类似 dropdown 组件的下拉框中使用。 | Boolean | false |
| value | 默认值对象,其中postClick，postView值可以根据mapKeys来动态改变 | Object<{postClick,postView}> | -- |
| label | 显示label名称 | String | -- |
| extraOption | 相对应的组件的额外配置 | Object<{postClick,postView}> | -- |
| mapKeys | 列表数据对应的props配置 | Array<[label,value,children]>> | -- |
| itemList | 如果时select,配置相对应的下拉数据 | Object<{postClick,postView} | -- |
| labelInner | 显示的label名称 | String | -- |
| prefixIcon | 前缀的图标名称 | String | -- |
| fitWidth | 是否适应宽度,开启时最小宽度为240 | Boolean | false |
| detail | 详细配置DetailInfo，具体参考 | Object | -- |
| isByCascaderVal | 当有两个进行组件时，是否需要关联联动值 | Boolean | false |
| cascaderKeyConfig | 当关联联动值的时候联动值配置 | String | { triggerKey: 'postClick', cascaderKey: 'postView'} |
| tip-text | 输入框提示文案。提示文案内容 | string | —— |
| state | 输入框状态 可选值:success/warning/error | string | —— |
| show-tip | 输入框是否显示提示。是否显示提示信息 | boolean | false |

## 方法 Methods

组件暴露的方法，可通过 ref 调用。

| 方法名 | 说明 | 参数 |
| --- | --- | --- |
| blur | 指定特定key的元素失去焦点，如果没有传，则是整个组件 | ({key}) => void |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| isChange | 组件值变化的回调 | Function(value,triggerKey) |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/button.html)

