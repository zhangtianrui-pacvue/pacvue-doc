---
component: editbox
category: other
tags: [editbox]
aliases: [editbox]
version: 1.0.0
description: "PacvueEditbox基础用法"
---

# editbox 组件文档

> PacvueEditbox基础用法

## 使用示例

### 按钮分为单行输入以及多行输入

```vue
<template>
  <div style="width:300px;">
    <p>单行输入</p>
    <PacvueEditbox
      v-model="testVal"
      :canEdit="true"
      class="pacue-tableCell-test"
      isServer
      @save="saveVal"
      :inputType="'number'"
      digitChar="."
      :min="10"
      :max="100"
      :digitCount="1"
      :rows="1"
      :labelStyle="{ color: 'red' }"
    >
      <template #input-prefix>$</template>
      <template #edit-icon>
        <el-icon class="ml-[15px] cursor-pointer align-middle" :size="24"><PacvueIconEditdetails /></el-icon>
      </template>
      <!-- <template #action>
        <el-icon class="ml-[15px] cursor-pointer align-middle" :size="24"><PacvueIconEditdetails /></el-icon>
      </template> -->
    </PacvueEditbox>
 </div>
 <div style="width:300px;">
  <p>多行输入</p>
  <PacvueEditbox v-model="testVal2" :canEdit="true" multiple required :isLabelTriggerEdit="true">
    <template #input-prefix>$</template>
  </PacvueEditbox>
</template>
<script setup>
    import { ref } from 'vue'
    var  testVal = ref('this is a test ')
    var  testVal2 = ref('this is a test ')
    var saveVal = (val, resolve) => {
      resolve(true)
      //testVal.value = val
    }
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### 你可以通过required控制是否是必须输入，也可以通过validation来控制

```vue
<template>
  <PacvueEditbox v-model="testVal" :canEdit="true" :rows="1"  multiple required>
    <template #input-prefix>$</template>
  </PacvueEditbox>
</template>

<script setup>
  import { ref } from 'vue'
  var  testVal3 = ref('this is a test ')
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### 通过配置 actionListFormat，显示自定义的 action 图标

```vue
<template>
  <PacvueEditbox v-model="datasource" :actionListFormat="actionListFormat" :canEdit="true" multiple
    @iconClick="iconClick" @iconMouseEnter="iconMouseEnter"></PacvueEditbox>
</template>

<script setup>
  import { ref } from 'vue'
  const datasource = ref('testeaa')
  const iconClick = ({ actioninfo, record, column }) => {
    console.log('iconClick', { actioninfo, record, column })
  }
  const iconMouseEnter = ({ actioninfo, record, column }) => {
    console.log('iconMouseEnter', { actioninfo, record, column })
  }
  /** 生成 action 数据数组，用于渲染 action 图标 */
  const actionListFormat = (record, column) => {
    return [
      { component: 'PacvueIconCommerceChecked', disabled: false, tooltip: 'aaaa' },
      { component: 'PacvueIconCommercePacvueTools', disabled: false, tooltip: 'bbb' },
      { component: 'PacvueIconConfirm', disabled: true, tooltip: 'ccc' }
    ]
  }
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| showValue | 编辑框显示的值，如果没有配置则显示modelValue | String\|Number | -- |
| modelValue | 输入框的值。组件绑定值，配合 v-model 使用 | String\|Number | -- |
| required | 是否是必填的 | Boolean | false |
| defaultValue | 显示的默认值 | String | -- |
| isServer | 是否是异步保持操作 | Boolean | false |
| disabled | 是否禁用编辑功能。是否禁用组件，禁用后无法进行交互 | Boolean | false |
| record | 行数据 | Object | -- |
| column | column 信息，当在 table 中使用时需要传入。 | Object | -- |
| canEdit | 是否可以编辑 | Boolean | false |
| multiple | 是否是文本域。是否支持多选模式 | Boolean | false |
| editCallBack | 编辑的回调 | Function | -- |
| isFitContent | 是否按内容自适应宽度 | Boolean | true |
| color | 字体的颜色 | String | -- |
| validation | 验证规则 | Function(value):{isSuccess:Boolean,msg:String} | -- |
| isActionInSpace | 操作图标是否占用空间,如果设置为absolute会使图标定位为绝对定位,visible会让编辑图标常显示 | Boolean\|String | absolute |
| rows | 文本域行数 | Number | 3 |
| inputType | 输入框限制的格式，支持text,number,int | String | text |
| inputDigitChar | input输入框的小数点的类型,可选值为：./, | String\|Array | . |
| digitChar | 显示的lable小数点的类型,可选值为：./, | String | . |
| digitCount | 输入框限制的格式为number类型时，小数点的位数 | Number | 3 |
| inputFormat | 输入框限制的格式化方法，注意：优先级比inputType | Function(value):String\|Number | -- |
| isLabelTriggerEdit | 是否点击文本触发编辑功能,会默认把hasLabelClick关闭 | Boolean | false |
| hasLabelClick | 是否有label点击功能,主要是为了控制label颜色 | Boolean | true |
| hasEdit | 是否有编辑功能 | Boolean | true |
| min | 限制的最小值（inputType为number，int才生效） | Number | -- |
| max | 限制的最大值（inputType为number，int才生效） | Number | -- |
| minTip | 小于min值得tip | String | -- |
| maxTip | 超过max值得tip | String | -- |
| isTwoRow | 最多两行显示省略号 | Boolean | false |
| lineClamp | 最多显示几行出现省略号,优先级高于isTwoRow | Number | -- |
| freezeEdit | 用于控制编辑按钮点击后触发的编辑操作弹窗状态是否冻结，冻结后编辑操作弹窗的将无法隐藏 | Boolean | false |
| maxlength | 最大输入长度 | Number\|String | -- |
| minlength | 最小输入长度 | Number | -- |
| actionListFormat | 用于生成 action 图标列配置对象的函数。优先级高于在 table 中使用时,table column 中配置的 actionListFormat | (record, column) => <actionOption>[] | -- |
| isStopEnter | 是否下拉输入框中阻止enter事件 | Boolean | false |
| showTipMode | 错误提示的方式,default(默认的出现在下拉框下面)\|inner(出现在input内部的tip上面) | String | default |
| cancelInterceptor | 取消拦截器 | Function({value},resolve:(isSuccess, errorMsg)=>{}) | default |
| inputPlaceholder | 输入框的placeholder | Please input | -- |
| component | action 图标组件的名称。 | string | -- |
| disabled | 是否禁用，禁用则直接不显示。。是否禁用组件，禁用后无法进行交互 | boolean | -- |
| tooltip | action 图标的 tooltip | string | -- |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| textClick | 点击文本触发 | Function(modelValue) |
| editClick | 点击编辑按钮触发 | -- |
| save | 保持时触发的点击事件 | Function(editValue,callback(isSuccess)) |
| iconClick | action 图标 click 事件 | Function({ actioninfo, record, column }) |
| iconMouseEnter | action 图标 mouseenter 事件 | Function({ actioninfo, record, column }) |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| content | 显示内容插槽 | -- |
| input-prefix | 输入框前部内容 | -- |
| input-suffix | 输入框尾部内容 | -- |
| suffix | 显示内容尾部内容 | -- |
| dropdown | 下拉框内容 | -- |
| textarea-bottom | 多行输入框底部内容 | -- |

