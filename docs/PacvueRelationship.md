---
component: PacvueRelationship
category: form
tags: [关系选择, 逻辑, 表单]
aliases: [PacvueRelationship]
version: 1.0.0
description: "复杂的的特殊输入框"
---

# PacvueRelationship 组件文档

> 复杂的的特殊输入框

**分类**: form | **标签**: 关系选择、逻辑、表单

## 使用示例

### select 固定为单选

```vue
<template>
  <PacvueComplexInput
    v-model="complexVal"
    style="width:300px"
    class="pacvue-filterItem-hasClose"
    :labelInner="'Label'"
    :placeholder="'Please Select '"
    :multiple="false"
    :hasRelationshipLine="true"
    @inputFocus="inputBindEvent('focus')"
    @input-blur="inputBindEvent('blur')"
    @input-enter="inputBindEvent('enter')"
    :inputOption="{maxlength:10}"
    @clear="handleClear"
>
  <template #relationship>
    <PacvueRelationship
    class="pacvue-filter-noHpadding"
    v-model="complexRealtionVal"
    :selectLabelQuote="false"
    :selectLabelColor="'#66666c'"
    :props="{ value: 'value', label: 'label' }"
    :data="[
      { value: 1, label: 'And' },
      { value: 2, label: 'Or' }
    ]"
  ></PacvueRelationship>
  </template>
  <template #input-suffix>
    <span style="color: var(--pac-filter-label-color)">CPC %</span>
  </template>
</PacvueComplexInput>
</template>
<script setup>
  import { ref } from 'vue'
  const complexVal = ref([])  
  const complexRealtionVal = ref(1)
  var inputBindEvent = (type) => {
  console.log('>>>>>>>>inputType', type)
}
var inputChange = (val) => {
  console.log('>>>>>>>val', val)
}
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| v-model | 双向绑定值。双向绑定值，用于获取和设置组件的当前值 | string/number | -- |
| showLabelTip | 鼠标悬停时tooltip提示文案 | sting | -- |
| data | select中的数据。数据源，用于渲染组件内容 | array | -- |
| props | 配置选项，具体看下表 | Object | { value: 'value', label: 'label', children: 'children' } |
| selectLabelQuote | 选中值的文案是否使用双引号包裹 | boolean | true |
| selectLabelColor | 选中值的文案颜色 | string | var(--el-color-primary) |

## 相关链接

- [Element Plus 文档](/#/pacvue-select)

