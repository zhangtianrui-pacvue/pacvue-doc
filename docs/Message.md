---
component: Message
category: feedback
tags: [消息提示, 反馈, 通知]
aliases: [Message, 消息]
version: 1.0.0
description: "Message"
---

# Message 组件文档

> Message

**分类**: feedback | **标签**: 消息提示、反馈、通知

## 使用示例

### 全局通告

```vue
<template>
  <PacvueButton @click="open1">info</PacvueButton>
  <PacvueButton :plain="true" @click="open2">success</PacvueButton>
  <PacvueButton :plain="true" @click="open3">warning</PacvueButton>
  <PacvueButton :plain="true" @click="open4">error</PacvueButton>
</template>
<script setup>
  import { ref, defineComponent, h } from 'vue'
  import { PacvueMessage } from '@pacvue/element-plus'

  const open1 = () => {
    PacvueMessage({
      message: 'this is a message.'
    })
  }
  const open2 = () => {
    PacvueMessage({
      message: 'Congrats, this is a success message.',
      type: 'success'
    })
  }
  const open3 = () => {
    PacvueMessage({
      message:
        'Warning, this is a warning messageWarning, this is a warning messageWarning, this is a warning messageWarning, this is a warning messageWarning, this is a warning messageWarning, this is a warning messageWarning, this is a warning messageWarning, this is a warning messageWarning, this is a warning messageWarning, this is a warning message.',
      type: 'warning'
    })
  }
  const open4 = () => {
    PacvueMessage({
      message: 'Oops, this is a error message.',
      type: 'error'
    })
  }
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| message | 通知栏正文内容 | string\|VNode\|() => VNode | -- |
| type | 通知类型 success / warning / info / error | string | info |
| customClass | 自定义类名 | string | -- |
| duration | 显示时间，单位为毫秒。 设为 0 则不会自动关闭 | number | 3000 |
| showClose | 是否显示关闭按钮 | boolean | false |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/message.html)

