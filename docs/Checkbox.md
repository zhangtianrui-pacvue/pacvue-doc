---
component: Checkbox
category: form
tags: [复选框, 表单, 多选]
aliases: [Checkbox, 复选]
version: 1.0.0
description: "基础用法"
---

# Checkbox 组件文档

> 基础用法

**分类**: form | **标签**: 复选框、表单、多选

## 使用示例

### 单独使用可以表示两种状态之间的切换，写在标签中的内容为 checkbox 按钮后的介绍。

```vue
<template>
  <p class="mb-4">default</p>
  <el-row class="mb-4">
    <PacvueCheckbox v-model="checkboxVal2" :disabled="false"> Uncheck </PacvueCheckbox>
    <PacvueCheckbox v-model="checkboxVal"  isDynamicTooltip>
      <template #default>
        Check 1`2`2 Check 1`2`2 Check 1`2`2 Check 1`2`2 Check 1`2`2 Check 1`2`2 Check 1`2`2 Check 1`2`2 Check 1`2`2 Check 1`2`2 Check 1`2`2 Check 1`2`2 Check 1`2`2 Check 1`2`2 Check 1`2`2 Check
        1`2`2 Check 1`2`2 Check 1`2`2 Check 1`2`2 Check 1`2`2 Check 1`2`2 Check 1`2`2 Check 1`2`2 Check 1`2`2 Check 1`2`2 Check 1`2`2
      </template>
      <template #tooltip>1321123131</template>
      <template #aside>aside</template>
    </PacvueCheckbox>
  </el-row>
</template>
<script setup>
  import { Check, Delete, Edit, Message, Search, Star } from '@pacvue/element-plus'
  const checkboxVal2 = ref(false)
  const checkboxVal = ref(true)
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### 多选框不可用状态。 使用 disabled 属性来控制是否为禁用状态。 该属性接受一个

```vue
<template>
  <el-row class="mb-4">
    <el-checkbox v-model="checked3" disabled>Disabled</el-checkbox>
    <el-checkbox v-model="checked4">Not disabled</el-checkbox>
  </el-row>
</template>

<script setup>
  const checked3 = ref(false)
  const checked4 = ref(true)
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### 多选框组 适用于多个勾选框绑定到同一个数组的情景，通过是否勾选来表示这一组选项中选中的项

```vue
<template>
  <el-row class="mb-4">
    <PacvueCheckboxGroup v-model="selectedValue">
      <template #allLabel> Select All </template>
      <PacvueCheckbox label="default1"> Checkbox1 </PacvueCheckbox>
      <PacvueCheckbox label="default2"> Checkbox2 </PacvueCheckbox>
      <PacvueCheckbox label="default3"> Checkbox3 </PacvueCheckbox>
    </PacvueCheckboxGroup>
    <div style="padding-left: 40px">
      <PacvueCheckboxGroup v-model="selectedValue3" direction="vertical">
        <PacvueCheckbox label="default1"> Checkbox1 </PacvueCheckbox>
        <PacvueCheckbox label="default2"> Checkbox2 </PacvueCheckbox>
        <PacvueCheckbox label="default3"> Checkbox3 </PacvueCheckbox>
      </PacvueCheckboxGroup>
    </div>
  </el-row>
</template>

<script setup>
  const selectedValue = ref(['default1', 'default2'])
  const selectedValue3 = ref(['default1', 'default2'])
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### 使用hasCheckAll控制是否有checkAll功能

```vue
<template>
  <el-row class="mb-4">
    <PacvueCheckboxGroup v-model="selectedValue2" :hasCheckAll="false">
      <PacvueCheckbox label="default1"> Checkbox1 </PacvueCheckbox>
      <PacvueCheckbox label="default2"> Checkbox2 </PacvueCheckbox>
      <PacvueCheckbox label="default3"> Checkbox3 </PacvueCheckbox>
    </PacvueCheckboxGroup>
  </el-row>
</template>

<script setup>
  const selectedValue2 = ref(['default1', 'default2'])
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| showCheckbox | 是否显示checkbox | Boolean | true |
| showLabel | 是否显示Label值 | Boolean | true |
| square | 选中框的形状square, circle | String | square |
| fontSize | 字体大小 | String | 14px |
| isDynamicTooltip | 是否开启动态tip(内容超出宽度显示tooltip) | Boolean | false |
| verticalAlign | 文本跟checkbox垂直对齐方式（center或top） | String | center |
| code | checkbox的唯一标志,如果没有默认使用label（hasExtraArg开启才会起作用，作为change事件的第二个参数code） | String | -- |
| hasExtraArg | checkbox中change方法是否有code参数 | Boolean | false |
| allLabel | all多选框的label名称 | String | All |
| hasCheckAll | 是否有check all功能 | Boolean | true |
| direction | 多选框组显示的方向,默认horizontal,可选项horizontal vertical | String | horizontal |
| spacing | 多选框组显示的左偏移量 | String | 16px |
| square | 选中框的形状square, circle | String | square |
| fontSize | 字体大小 | String | 14px |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| tooltip  | checkbox中tooltip插槽（注意：只有isDynamicTooltip开启的时候，才会有作用） | -- |
| default  | checkbox具体内容的占位符） | -- |
| aside  | checkbox中右边内容的占位符（注意：只有isDynamicTooltip开启的时候，才会有作用 | -- |
| allLabel | checkbox组check All中label显示插槽 | -- |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/checkbox.html)

