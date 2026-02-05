---
component: DatePickerCustomV2
category: form
tags: [自定义日期, 表单, V2]
aliases: [DatePickerCustomV2]
version: 1.0.0
description: "PacvueDatePickerCustomV2 定制日期选择"
---

# DatePickerCustomV2 组件文档

> PacvueDatePickerCustomV2 定制日期选择

**分类**: form | **标签**: 自定义日期、表单、V2

## 使用示例

### 定制日期选择

```vue
<template>
  <div class="customContainer">
    <pacvue-button @click="changeRealTime">切换RealTime</pacvue-button>
    <div style="display: none">{{ dateRange }}</div>
    <PacvueDatePickerCustom :opens="'center'" :dateRange="dateRange" :minDate="minDate" :maxDate="maxDate"
      :isCompare="true" :compareSummary="false" :showCompareCheck="true" :showSummaryCheck="false"
      :alwaysShowCalendars="false" :compareDate="compareDate" :realTimeClient="realTimeClient" :lifeTimeMode="true"
      :hasDayBeforeYesterday="true" :homeMode="true" @update="updateValues" @toggle="checkOpen" :isRealTimeByPST="false"
      :isIsolateRealTime="true" :isStrictIsolate="false" :latestDateMode="'Real Time'" :isCompareCustom="compareMode" />
  </div>
</template>

<script setup>
  import { ref, reactive } from 'vue'
  import { dayjs } from '@pacvue/element-plus'
  var realTimeClient = ref(true)
  const changeFn = (e) => {
    console.log(e)
  }
  const changeRealTime = () => {
    realTimeClient.value = !realTimeClient.value
  }

  const compareMode = ref(true)

  // v2版本升级定义数据
  const compareDate = ref({
    start: '2022-06-01',
    end: '2022-06-30'
  })

  const dateRange = ref({
    startDate: '2023-07-24',
    endDate: '2023-08-14'
  })

  // v2版本升级定义方法
  const change = () => {
    this.compareDate = {
      start: '2022-07-01',
      end: '2022-07-30'
    }
  }
  // 点击Apply按钮时候生效
  const updateValues = (values) => {
    console.log('updateValues', values)
    dateRange.value = {
      startDate: dayjs(values.startDate).format('YYYY-MM-DD'),
      endDate: dayjs(values.endDate).format('YYYY-MM-DD')
    }
    compareDate.value = {
      start: dayjs(values.start).format('YYYY-MM-DD'),
      end: dayjs(values.end).format('YYYY-MM-DD')
    }
    compareMode.value = values.isCompareCustom
  }

  // 点击input时候出发，显示日期弹出框状态
  const checkOpen = (open) => {
    console.log('checkOpen', open)
  }
</script>

<style scoped>
  .customContainer {
    text-align: center;
    height: 900px;
    /* background-color: black; */
  }

  small.form-text {
    display: initial;

    &::before {
      content: ' - ';
    }
  }
</style>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| dateRange | 默认日期 | Object | {startDate:null,endDate:null} |
| opens | 打开方向 | String | left |
| minDate | 配置可选最小日期 | String \| Date | null |
| maxDate | 配置可选最大日期 | String \| Date | null |
| showCompareCheck | Compare check是否可见 | Boolean | true |
| isCompare | Compare check是否默认选中(开启compare模式) | Boolean | false |
| showSummaryCheck | Summary check是否可见 | Boolean | true |
| compareSummary | summary check是否默认选中 | Boolean | false |
| alwaysShowCalendars | 默认日历展示(false即开启Custom Range) | Boolean | false |
| compareDate | 自定义比较日期 | Object | {start:null,end:null} |
| linkedCalendars | 日历左右月份切换联动 | Boolean | true |
| timePicker | 时间相关设置，本次暂未生效 | Boolean | false |
| timePickerIncrement | 时间相关设置，本次暂未生效 | Number | 5 |
| timePicker24Hour | 时间相关设置，本次暂未生效 | Boolean | false |
| timePickerSeconds | 时间相关设置，本次暂未生效 | Boolean | false |
| autoApply | 是否自动确认日期选择操作 | Boolean | false |
| realTimeClient | realtimeclient有的realtime选项 | Boolean | false |
| localeData | 国际化日期配置，本次暂未生效 | Object | {} |
| homeMode | home页专属文案调整 | Boolean | false |
| dateFormatText | 显示时间格式化字符串，优先级高于本地缓存中根据平台差异判断的日期格式。 | String | -- |
| sidebarExpand | 控制右侧展开状态（不影响当前交互设置） | Boolean | true |
| extraOptions | datepicker中dateRange转换的额外配置,格式为{startFormat:String,endFormat:undefined,formatType:Date\|dayjs},其中formatType为日期的格式化方式，默认使用Date | Object | {startFormat:undefined,endFormat:undefined,formatType:"Date"}} |
| lifeTimeMode | 配置commerce平台lifeTime模式是否开启 | Boolean | false |
| isRealTimeByPST | 是否realtime根据PST时间来 | Boolean | false |
| hasDayBeforeYesterday | 是否有前天的快捷键 | Boolean | false |
| isIsolateRealTime | 是否将realTime和custom Range区别开 | Boolean | false |
| isCompareCustom | 是否默认为Custom模式（可切换并记住为YoY模式） | Boolean | true |
| last24h | 范围选择中是否需要 Last 24H | Boolean | false |
| rangesFilter | 用于筛选出需要的时间范围选择项，不设置则全展示，入参为范围选择项对应的 key ，返回 true 的项展示，返回 false 的项不展示。 | (rangeKey) => Boolean | -- |
| defaultExtraRanges | 用于配置补充的时间范围选择项 | Object<{[key]:Array}> | -- |
| customRangeShowLabel | 用于配置时间范围选择项名称的国际化 | Object<{[key]:string}> | -- |
| customRangeConfig | 用于配置时间范围选择项的配置,目前仅支持isIsolate,以及showCompareCheck两个配置 | Object<{[key]:Object}> | -- |
| commerceCustomDateMode | commerce专属配置，开启后会区分左右选择的lastMode | Boolean | false |
| delayDateGroup | 数据延迟展示 | Object<{[key]:Array}> | [] |
| delayDateText | 数据延迟文案展示 | String | -- |
| yoyCustomRanges | YoY模式时生效，用于自定义不同时间模式下同比日期的时间跨度。如果未设置该函数或 return [],则取当前时间范围的前一年相同时间段作为对比时间。 | Function | function(rangeMode,start,end) { return [start,end]\|[] } |
| isComparePop | 初始化时是否默认为PoP模式 | Boolean | false |
| showComparePop | 是否在compare中显示PoP模式 | Boolean | false |
| popCustomRanges | PoP模式时生效，用于自定义不同时间模式下对比日期的时间跨度。如果未设置该函数或 return [],则取当前时间范围的前一周相同时间段作为对比时间。 | Function | function({type,start,end}) { return [start,end]\|[] } |
| beforeApply | 在 apply 操作生效前执行此方法，return true \| resolve 则执行 apply 逻辑，return false \| reject 终止 apply 逻辑。 | function (DateInfo) { return Boolean\|Promise } | -- |
| checkingTwoYears | 是否只允许选择开始日期两年的时间范围 | Boolean | false |
| currentDateRangeTitleTip | 当前title的tip | String | -- |
| compareDateRangeTitleTip | 对比时间title的tip | String | -- |
| disabledCurrentDateRange | 是否禁用当前日期 | Boolean | false |
| nextTimeMode | commerce、Next Month/Next Quarter/Next Year/This Month/This Quarter/This Year | Boolean | false |
| filterSettingsEnabled | 启用完全自定义的 date rages 配置，包含新增、编辑和排序功能。 | Boolean | false |
| filterSettings | 自定义 date rages 功能配置数组。filterSettingsEnabled 为 true 生效。 | Array | -- |
| settingsEditErrorTips | 自定义 date rages 编辑时异常提示文字生成函数。 | ({ min, max, type }) => return "error tips" | () => "Input error." |
| customDashboardMode | 此模式默认关闭，开启则会增加四种快速选中模式(Last 90 Days, Last 90 Days (Exclude latest 2 days), Last quarter, This quarter) | Boolean | false |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| update | 数据更新方法（最全） | DateInfo |
| toggle | 日期弹窗显示状态 | Boolean |
| pickerMouseenter | 鼠标移入日期展示框时触发 | MouseEvent |
| pickerMouseleave | 鼠标移出日期展示框时触发 | MouseEvent |

## 其他信息

| 属性 | 类型 | 说明 |
| --- | --- | --- |
| compare | Boolean | 是否开启了compare |
| compareSummary | Boolean | 是否开启了compareSummary |
| start | Date | compare 数据的 start date |
| end | Date | compare 数据的 end date |
| startDate | Date | 当前的 start date |
| endDate | Date | 当前的 end date |
| isCompareCustom | Boolean | 是否是 custom 模式 |
| isComparePop | Boolean | 是否是 PoP 模式 |
| isCompareYoy | Boolean | 是否是 YoY 模式 |
| latestDateMode | String | 日期范围的类型 |

