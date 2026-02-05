---
component: Drawer
category: feedback
tags: [抽屉, 侧边栏, 面板]
aliases: [Drawer, 抽屉]
version: 1.0.0
description: "Drawer"
---

# Drawer 组件文档

> Drawer

**分类**: feedback | **标签**: 抽屉、侧边栏、面板

## 使用示例

### 大小两个尺寸

```vue
<template>
    <el-button type="primary" style="margin-left: 16px" @click="drawer = true"> small </el-button>
    <el-button type="primary" style="margin-left: 16px" @click="drawer2 = true"> big modal </el-button>

    <pacvue-drawer v-model="drawer" title="I am the title1" pacSize="sm" :modal="false">
        <span>Hi, there1222222!</span>
    </pacvue-drawer>
    <pacvue-drawer v-model="drawer2" title="I am the title23" pacSize="lg">
        <span>Hi, there2!</span>
    </pacvue-drawer>
</template>
<script>
import { ref} from 'vue'
export default {
	setup(props, ctx) {
		const drawer = ref(false)
		const drawer2 = ref(false)
		return { drawer, drawer2}
    }
}
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| pacSize | 抽屉尺寸 sm / lg,sm:360px,lg:1080px | String | sm |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/drawer.html)

