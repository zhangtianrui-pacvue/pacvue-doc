---
component: Alert
category: feedback
tags: [警告, 提示, 消息]
aliases: [Alert, 警告]
version: 1.0.0
description: "Alert"
---

# Alert 组件文档

> Alert

**分类**: feedback | **标签**: 警告、提示、消息

## 使用示例

### Alert

```vue
<template>
  <DocBox>
    <PacvueAlert
      class="PacvueTemplate"
      title="success alert"
      type="success"
      :showIcon="false"
      :closable="false"
    ></PacvueAlert>
    <PacvueAlert class="PacvueTemplate" title="success alert" type="success" :closable="false" :showIcon="false" />
    <PacvueAlert class="PacvueTemplate" title="success alert" type="success" :showIcon="true" />
    <PacvueAlert class="PacvueTemplate" title="info alert" type="info" :showIcon="true" />
    <PacvueAlert class="PacvueTemplate" title="warning alert" type="warning" :showIcon="true" />
    <PacvueAlert class="PacvueTemplate" title="error alert" type="error" :showIcon="true" />
  </DocBox>
</template>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| closable | 是否可以关闭 | boolean | true |
| showIcon | 是否显示图标 | boolean | false |
| type | 通知类型 success / warning / info / error | string | info |
| tabHeaderOffset | type 为 custom-default 时生效，tab项的顶部偏移量。 | string | 24px |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/alert.html)

