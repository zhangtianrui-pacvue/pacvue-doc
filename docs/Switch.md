---
component: Switch
category: form
tags: [开关, 表单, 切换]
aliases: [Switch, 开关]
version: 1.0.0
description: "Switch"
---

# Switch 组件文档

> Switch

**分类**: form | **标签**: 开关、表单、切换

## 使用示例

### 示例：Switch

```vue
<template>
  <PacvueSwitch
    textWidth="80px"
    v-model="value1"
    inline-prompt
    active-text="accept"
    inactive-text="ignore"
  ></PacvueSwitch>
  <PacvueSwitch v-model="value2" />
  <PacvueSwitch v-model="value3" disabled />
  <PacvueSwitch v-model="value4" disabled />
</template>

<script>
  import { ref } from 'vue'
  const value1 = ref(true)
  const value2 = ref(false)
  const value3 = ref(true)
  const value4 = ref(false)
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| inlinePrompt | 在 switch 组件内显示文本 | boolean | false |
| activeText | switch 状态为 on 时的文本 | string | -- |
| inactiveText | switch 状态为 off 时的文本 | string | -- |
| textWidth | 文本显示区域的长度 | string | 40px |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/switch.html)

