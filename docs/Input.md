---
component: Input
category: form
tags: [输入框, 表单, 文本输入]
aliases: [Input, 输入]
version: 1.0.0
description: "Input 输入框"
---

# Input 组件文档

> Input 输入框

**分类**: form | **标签**: 输入框、表单、文本输入

## 使用示例

### 基础用法 通过 width 属性指定 input 组件宽度 默认宽度为256px

```vue
<template>
  <pacvue-input v-model="input" placeholder="Please input" />
  <div :style="{marginTop:'24px'}" />
  <pacvue-input width="400px" v-model="input1" placeholder="Please input" />
</template>
<script setup>
  import { ref } from 'vue'
  const input = ref('')
  const input1 = ref('')
</script>
```

### 输入数字的基础用法,你需要设置type为number 你可以通过设置min

```vue
<template>
  <pacvue-input v-model="input" placeholder="Please input" clearable type="number" :digitChar="['.', ',']" @input="inputChange" @change="inputChange" :digitCount="2" :min="10" :max="100">
    <template #suffix>
      <span>%</span>
    </template>
  </pacvue-input>
</template>
<script setup>
  import { ref } from 'vue'
  const input = ref('.1234555')
  var inputChange = (val) => {
    console.log('>>>>>>>val', val)
  }
</script>
```

### 通过 title 属性指定 input 组件标题

```vue
<template>
  <pacvue-input v-model="input2" title="Default" placeholder="Please input" />
</template>
<script setup>
  import { ref } from 'vue'
  const input2 = ref('')
</script>
```

### 通过 show-tip 属性指定 input 组件是否显示 提示，默认为不显示提示

```vue
<template>
  <pacvue-input v-model="input8" placeholder="Please input" :show-tip="true"></pacvue-input>
</template>
<script setup>
  import { ref } from 'vue'
  const input8 = ref('')
  const input9 = ref('')
</script>
```

### 通过 tip-icon 插槽指定 input 组件提示图标

```vue
<template>
  <pacvue-input v-model="input3" placeholder="Please input" :show-tip="true">
    <template #tip-icon><Warning /></template>
  </pacvue-input>
</template>
<script setup>
  import { ref } from 'vue'
  import { Warning } from '@pacvue/element-plus'
  const input3 = ref('')
</script>
```

### 通过 tip-text 属性指定 input 组件标题

```vue
<template>
  <pacvue-input v-model="input4" tip-text="Status message" placeholder="Please input" :show-tip="true" />
</template>
<script setup>
  import { ref } from 'vue'
  const input4 = ref('')
</script>
```

### 使用 state 属性指定 input 组件状态 :isTipAbsolute="true"

```vue
<template>
  <pacvue-input v-model="input5" state="success" tipText="Status message" placeholder="Please input" :show-tip="true"
    ><template #tip-icon><Warning /></template
  ></pacvue-input>
  <div style="margin: 20px 0;" />
  <pacvue-input v-model="input6" state="warning" tipText="Status message" placeholder="Please input" :show-tip="true"
    ><template #tip-icon><Warning /></template
  ></pacvue-input>
  <div style="margin: 20px 0;" />
  <pacvue-input v-model="input7" state="error" tipText="Status message" placeholder="Please input" :show-tip="true"
    ><template #tip-icon><Warning /></template
  ></pacvue-input>
</template>
<script setup>
  import { ref } from 'vue'
  import { Warning } from '@pacvue/element-plus'
  const input5 = ref('')
  const input6 = ref('')
  const input7 = ref('')
</script>
```

### 插槽可以满足不同的需求

```vue
<template>
  <pacvue-input v-model="input12" placeholder="Please input">
    <template #prefix>
      <span>$</span>
    </template>
  </pacvue-input>
  <div style="margin: 20px 0;" />
  <pacvue-input v-model="input13" placeholder="Please input">
    <template #suffix>
      <span>%</span>
    </template>
  </pacvue-input>
  <div style="margin: 20px 0;" />
  <pacvue-input v-model="input14" placeholder="Please input" disabled>
    <template #prefix>
      <span>$</span>
    </template>
  </pacvue-input>
  <div style="margin: 20px 0;" />
  <pacvue-input v-model="input15" placeholder="Please input" disabled>
    <template #suffix>
      <span>%</span>
    </template>
  </pacvue-input>
</template>
<script setup>
  import { ref } from 'vue'
  import { Search } from '@pacvue/element-plus'
  const input10 = ref('')
  const input11 = ref('')
  const input12 = ref('')
  const input13 = ref('')
  const input14 = ref('')
  const input15 = ref('')
</script>
```

### 输入框可以根据 节点 multiple属性 切换单值输入和多值输入 此状态下Input 标题

```vue
<template>
  <pacvue-input v-model="input16" placeholder="Please input" textAreaPlaceholder="One Keyword per line"
    :inputWithSelection="true" title="title" tipText="Status message" :removeDuplication="true" :options="options2"
    width="350px" :disableCallback="disableCallback" @selectChange="selectChange" v-model:selected="selectModel">
  </pacvue-input>
</template>
<script setup>
  import { ref } from 'vue'
  const input16 = ref([123])
  const selectModel = ref("Option3")
  const options2 = ref([])
  setTimeout(() => {
    options2.value = [
      {
        id: 'Option1',
        name: 'Option1 多值',
        multiple: 'true'
      },
      {
        id: 'Option2',
        name: 'Option2',
        disabled: true
      },
      {
        id: 'Option3',
        name: 'Option3'
      },
      {
        id: 'Option4',
        name: 'Option4 多值',
        multiple: 'true'
      },
      {
        id: 'Option5',
        name: 'Option5'
      }
    ]
  }, 4000)

  var disableCallback = (node) => {
    if (node.id == 'Option2') {
      return true
    }
  }

  const selectChange = (val) => {
    console.log('选择', val)
  }
</script>
```

### 输入框可以根据 节点 multiple属性 切换单值输入和多值输入 此状态下Input 标题

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

### 示例：input Complex

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
| v-model | 双向绑定值。双向绑定值，用于获取和设置组件的当前值 | string/number | —— |
| size | 禁用。组件尺寸大小，可选 large/default/small | —— | —— |
| title | 输入框标题 | string | —— |
| width | 输入框宽度。组件宽度，支持像素值或百分比 | string | 256px |
| tip-text | 输入框提示文案。提示文案内容 | string | —— |
| state | 输入框状态 可选值:success/warning/error | string | —— |
| show-tip | 输入框是否显示提示。是否显示提示信息 | boolean | false |
| digitChar | 小数点的类型,可选值为：./, | String\|Array | . |
| digitCount | 小数点的位数，只有type为number时才生效 | Number | -- |
| min | 限制的最小值（inputType为number，int才生效） | Number | -- |
| max | 限制的最大值（inputType为number，int才生效） | Number | -- |
| minTip | 小于min值得tip | String | -- |
| maxTip | 超过max值得tip | String | -- |
| inputWidthFilter | 开启input下拉筛选功能 | boolean | false |
| inputFilter | inputWidthFilter为true生效，筛选显示值的函数，item为下拉数组中的单个数据，text为当前输入框中的字符串，返回true则显示，false则隐藏。 | function | ({item, text}) => boolean |
| filterListRequest | inputWidthFilter为true生效，请求下拉数据的函数 | function | () => promise |
| inputFilterOption | inputWidthFilter为true生效，下拉数据的id、label取值字段的配置参数 | object | { id: "label", label: "label" } |
| filterEmptyText | inputWidthFilter为true生效，下拉数据为空时的提示文案。 | string | No Data Found! |
| filterLoading | inputWidthFilter为true生效，下拉数据请求时的loading样式 | boolean | -- |
| hasInputWithAppend | 具有append插槽是否有input事件 | boolean | true |
| showTipMode | 提示信息提示的方式,default\|inner(内置) | string | default |
| showInputOverflowTip | 是否显示input中内容溢出提示 | boolean | false |
| inputLabelInner | 输入框label的名称 | string | —— |
| inputLabelStyle | 输入框label的样式 | object | —— |
| dropdownWidth | 下拉内容的宽度 | string | —— |
| selectionOptions | inputWidthFilter为true生效,select选择器的配置,具体配置见PacvueSelect文档 | object | —— |
| v-model | 双向绑定值。双向绑定值，用于获取和设置组件的当前值 | array | —— |
| size | 禁用。组件尺寸大小，可选 large/default/small | —— | —— |
| width | 输入框宽度。组件宽度，支持像素值或百分比 | string | 256px |
| state | 输入框状态 可选值:success/warning/error | string | —— |
| inputWithSelection | 带选择器的输入框 | boolean | false |
| multipleOnly | 不带选择器时可以使用文本域 | boolean | false |
| textAreaPlaceholder | 带选择器的输入框 textarea的占位符 | string | —— |
| removeDuplication | 带选择器的输入框 modelValue 是否去重 | boolean | false |
| filterable | 选择器是否显示过滤框。是否支持筛选/搜索功能 | boolean | true |
| disableCallback | select选择器 判断节点是否可用，参数为当前节点信息node,需要返回boolean | Function | function(node) |
| options | 数据列表,具体类型看下表 | array | [] |
| defaultSelection | select 选择器默认选中的值 | string | -- |
| id | 选项的值（必填） | string | —— |
| name | 选项的标签（必填） | string | —— |
| disable | 选项是否禁用 | boolean | false |
| multiple | input是否可以多输入。是否支持多选模式 | boolean | false |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| tip-icon | 输入框提示图标 | svg |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/input.html#input-%E5%B1%9E%E6%80%A7)

