---
component: Notification
category: feedback
tags: [通知, 反馈, 提醒]
aliases: [Notification, 通知]
version: 1.0.0
description: "Notification"
---

# Notification 组件文档

> Notification

**分类**: feedback | **标签**: 通知、反馈、提醒

## 使用示例

### 基础用法

```vue
<template>
	<el-button type="primary" style="margin-left: 16px" @click="showNotify">基础</el-button>
	<el-button type="primary" style="margin-left: 16px" @click="showNotify1">带时间</el-button>
</template>
<script>
	import { PacvueNotify } from '@pacvue/element-plus'
	export default {
		setup(props, ctx) {
			const showNotify = () => {
				PacvueNotify({
					title: 'Notification',
          duration: 30000,
					message: 'Fruitcake chocolate bar tootsie roll gummies jelly beans cake gummies.'
				})
			}
			const showNotify1 = () => {
				PacvueNotify({
					title: 'Notification',
					showTime: true,
					duration: 0,
					message: 'Fruitcake chocolate bar tootsie roll gummies jelly beans cake gummies.'
				})
			}
			return { showNotify, showNotify1 }
		}
	}
</script>
```

### 带图标

```vue
<template>
	<el-button type="primary" style="margin-left: 16px" @click="showNotify2">Success</el-button>
	<el-button type="primary" style="margin-left: 16px" @click="showNotify3">Warning</el-button>
	<el-button type="primary" style="margin-left: 16px" @click="showNotify4">Info</el-button>
	<el-button type="primary" style="margin-left: 16px" @click="showNotify5">Error</el-button>
</template>
<script>
	import { PacvueNotify } from '@pacvue/element-plus'
	export default {
		setup(props, ctx) {

			const showNotify2 = () => {
				PacvueNotify({
					title: 'Notification',
					message: 'Fruitcake chocolate bar tootsie roll gummies jelly beans cake gummies.',
					pacType: 'success'
				})
			}

			const showNotify3 = () => {
				PacvueNotify({
					title: 'Notification',
					message: 'Fruitcake chocolate bar tootsie roll gummies jelly beans cake gummies.',
					pacType: 'warning'
				})
			}

			const showNotify4 = () => {
				PacvueNotify({
					title: 'Notification',
					message: 'Fruitcake chocolate bar tootsie roll gummies jelly beans cake gummies.',
					pacType: 'info'
				})
			}

			const showNotify5 = () => {
				PacvueNotify({
					title: 'Notification',
					message: 'Fruitcake chocolate bar tootsie roll gummies jelly beans cake gummies.',
					pacType: 'error'
				})
			}

			return { showNotify2, showNotify3, showNotify4, showNotify5 }
		}
	}
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| title | 标题 | string | -- |
| message | 通知栏正文内容 | string\|VNode | -- |
| duration | 显示时间, 单位为毫秒。 值为 0 则不会自动关闭 | number | 4500 |
| showTime | 是否展示倒计时 | Boolean | false |
| pacType | 通知类型 success / warning / info / error | string | -- |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/notification.html)

