---
component: DatePicker
category: form
tags: [日期选择, 表单, 时间]
aliases: [DatePicker, 日期]
version: 1.0.0
description: "Day展示方式"
---

# DatePicker 组件文档

> Day展示方式

**分类**: form | **标签**: 日期选择、表单、时间

## 使用示例

### 示例：day Model

```vue
<template>
  <PacvueDatePicker v-model="value1" @change="changeFn" placeholder="Pick a day" />
</template>
<script setup>
  import { ref } from 'vue'

  const value1 = ref('')
  const dateChange = (e) => {
    console.log(e)
  }
</script>
```

### 示例：week Model

```vue
<template>
  <PacvueDatePicker v-model="value2" :type="typetype" placeholder="Pick a week" @change="weekChange"
    :is-show-val-capitalize="true" :weekWithDays="4" />
</template>
<script setup>
  import { ref } from 'vue'

  const value2 = ref('')
  const weekChange = (e) => {
    console.log(e)
  }
</script>
```

### 示例：month Model

```vue
<template>
  <PacvueDatePicker v-model="value3" type="month" prefix-position="left" :prefix-icon="customPrefix"
    placeholder="Pick a month" @change="monthChange" />
</template>
<script setup>
  import { h, ref, shallowRef } from 'vue'

  const value3 = ref('')
  const monthChange = (e) => {
    console.log(e)
  }
  // 自定义前缀图标
  const customPrefix = shallowRef({
    render() {
      return h('span', 'time123123123123')
    }
  })
</script>
```

### 示例：date Range

```vue
<template>
  <PacvueDatePicker :shortcuts="shortcuts" v-model="value4" type="daterange" start-placeholder="Start date"
    end-placeholder="End date" />
</template>
<script setup>
  import { ref } from 'vue'
  import { dayjs } from '@pacvue/element-plus'

  const value4 = ref('')
  // 快捷选项配置数组，不需要的话可以不设置
  const shortcuts = [
    {
      text: 'Next 30 days',
      value: () => {
        const start = dayjs().add(1, 'day')
        const end = dayjs().add(30, 'day')
        return [start.toDate(), end.toDate()]
      },
    },
    {
      text: 'Next month',
      value: () => {
        const start = dayjs().add(1, 'month').startOf('month');
        const end = dayjs().add(1, 'month').endOf('month');
        return [start.toDate(), end.toDate()]
      },
    },
    {
      text: 'Next 90 days',
      value: () => {
        const start = dayjs().add(1, 'day')
        const end = dayjs().add(90, 'day')
        return [start.toDate(), end.toDate()]
      },
    },
    {
      text: 'Next quarter',
      value: () => {
        const start = dayjs().add(1, 'quarter').startOf('quarter');
        const end = dayjs().add(1, 'quarter').endOf('quarter');
        return [start.toDate(), end.toDate()]
      },
    }
  ]
</script>
```

### 示例：month Range

```vue
<template>
  <PacvueDatePicker v-model="value6" type="monthrange" start-placeholder="Start date" end-placeholder="End date" />
</template>
<script setup>
  import { ref } from 'vue'

  const value6 = ref('')
</script>
```

### 示例：quarter Model

```vue
<template>
  <PacvueDatePicker :yearNum="8" v-model="value5" :type="dateType" :disabled="false" placeholder="Pick a Quarter"
    @change="quarterChange" />
</template>
<script setup>
  import { ref } from 'vue'

  const value5 = ref('2021-05-1')
  const dateType = ref('quarter')
  const quarterChange = (e) => {
    console.log(e)
  }
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| prefix-icon | 前缀图标，已替换新日历SVG | String \| Component | NewDate |
| prefix-position | 前缀图标位置 | String | right |
| format | 日期格式化 | String | MM/DD/YYYY |
| type | 显示类型: year / month / date / dates / datetime / week / datetimerange / daterange / monthrange / quarter | String | date |
| yearNum | 季度的专属配置：年份（表示从此刻向前x年份的季度） | Number | 2 |
| weekStartDate | 周开始的日期，如果传了值，则会从当前日期所在周作为第一周,需要是完整的日期 | String\|Object | -- |
| weekStartDateFormat | 周开始的日期格式 | String | -- |
| weekWithDays | 那年的一周中的天数>=weekWithDays,就属于该年的周 | Number | 1 |
| isBlurAsyncInput | 是否失去焦点选中日期同步到input输入框 | Boolean | false |
| inputReadOnly | 是否输入框只读 | Boolean | false |
| shortcuts | 设置左侧快捷选项，需要传入数组对象 | Array<{ text: string, value: Date \| Function }> | -- |
| error | 是否显示异常提示 | Boolean | -- |
| errorText | 异常提示文字 | String | -- |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| customCase | 自定义数据展示区域样式 | -- |
| shortcuts | 设置左侧快捷选项，需要传入数组对象 | Array<{ text: string, value: Date \| Function }> |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/date-picker.html)

