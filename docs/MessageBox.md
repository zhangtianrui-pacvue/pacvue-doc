---
component: MessageBox
category: feedback
tags: [消息弹框, 确认, 对话]
aliases: [MessageBox, 消息框]
version: 1.0.0
description: "PacvueMessageBox一般使用"
---

# MessageBox 组件文档

> PacvueMessageBox一般使用

**分类**: feedback | **标签**: 消息弹框、确认、对话

## 使用示例

### 从设计上来说，MessageBox 的作用是美化系统自带的 alert、confirm 和

```vue
<template>
  <PacvueButton @click="open1">message</PacvueButton>
  <PacvueButton :plain="true" @click="open2">success</PacvueButton>
  <PacvueButton :plain="true" @click="open3">warning</PacvueButton>
  <PacvueButton :plain="true" @click="open4">error</PacvueButton>
  <PacvueButton :plain="true" @click="open5">info</PacvueButton>
</template>

<script setup>
  import { PacvueMessageBox } from '@pacvue/element-plus'

  const open1 = () => {
    PacvueMessageBox({
      title: 'Title',
      message: 'Congrats, this is a success message.',
      confirmButtonText: 'OK',
      cancelButtonText: 'Cancel'
    })
  }
  const open2 = () => {
    PacvueMessageBox({
      title: 'Title',
      message: 'Congrats, this is a success message.',
      type: 'success'
    })
  }
  const open3 = () => {
    PacvueMessageBox({
      title: 'Title',
      message: 'Warning, this is a warning message.',
      type: 'warning'
    })
  }
  const open4 = () => {
    PacvueMessageBox({
      title: 'Title',
      message: 'Oops, this is a error message.',
      type: 'error'
    })
  }
  const open5 = () => {
    PacvueMessageBox({
      title: 'Title',
      message: 'Oops, this is a info message.',
      type: 'info'
    })
  }
</script>
```

### 调用 PacvueMessageBox.alert 方法以打开 alert 框。 它模拟了系统的

```vue
<template>
  <PacvueButton @click="open6">PacvueMessageBox.alert</PacvueButton>
</template>

<script setup>
  import { PacvueMessageBox, PacvueMessage } from '@pacvue/element-plus'

  const open6 = () => {
    PacvueMessageBox.alert('this is a message.', 'Title', {
      confirmButtonText: 'OK',
      cancelButtonText: 'Cancel',
      callback: (action) => {
        PacvueMessage({
          type: 'info',
          message: `action: ${action}`
        })
      }
    })
  }
</script>
```

### 提示用户确认其已经触发的动作，并询问是否进行此操作时会用到此对话框。 值得一提的是，窗口被关闭后

```vue
<template>
  <PacvueButton @click="open7">PacvueMessageBox.confirm</PacvueButton>
</template>

<script setup>
  import { PacvueMessageBox, PacvueMessage } from '@pacvue/element-plus'

  const open7 = () => {
    PacvueMessageBox.confirm('this is a message.', 'Title', {
      confirmButtonText: 'OK',
      cancelButtonText: 'Cancel',
      type: 'warning'
    })
      .then(() => {
        PacvueMessage({
          type: 'success',
          message: 'Delete completed'
        })
      })
      .catch(() => {
        PacvueMessage({
          type: 'info',
          message: 'Delete canceled'
        })
      })
  }
</script>
```

### 当需要用户输入内容时，可以使用 Prompt 类型的消息框。 可以用 inputPattern

```vue
<template>
  <PacvueButton @click="open8">PacvueMessageBox.prompt</PacvueButton>
</template>

<script setup>
  import { PacvueMessageBox, PacvueMessage } from '@pacvue/element-plus'

  const open8 = () => {
    PacvueMessageBox.prompt('Please input your e-mail', 'Tip', {
      confirmButtonText: 'OK',
      cancelButtonText: 'Cancel',
      inputPattern: /[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?/,
      inputErrorMessage: 'Invalid Email'
    })
      .then(({ value }) => {
        PacvueMessage({
          type: 'success',
          message: `Your email is:${value}`
        })
      })
      .catch(() => {
        PacvueMessage({
          type: 'info',
          message: 'Input canceled'
        })
      })
  }
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| title | 标题 | string | -- |
| message | 通知栏正文内容 | string\|VNode\|() => VNode | -- |
| type | 通知类型 success / warning / info / error | string | -- |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/message-box.html)

