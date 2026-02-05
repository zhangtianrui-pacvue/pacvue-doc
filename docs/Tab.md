---
component: Tab
category: navigation
tags: [标签页, 导航, 切换]
aliases: [Tab, Tabs, 标签页]
version: 1.0.0
description: "Tab默认用法"
---

# Tab 组件文档

> Tab默认用法

**分类**: navigation | **标签**: 标签页、导航、切换

## 使用示例

### Tab

```vue
<template>
  <pacvue-radio-group v-model="tabPosition" style="margin-bottom: 30px">
    <pacvue-radio-button label="top">top</pacvue-radio-button>
    <pacvue-radio-button label="right">right</pacvue-radio-button>
    <pacvue-radio-button label="bottom">bottom</pacvue-radio-button>
    <pacvue-radio-button label="left">left</pacvue-radio-button>
  </pacvue-radio-group>
  <PacvueTab :tab-position="tabPosition" style="height: 200px; width: 500px" class="demo-tabs">
    <pacvue-tab-pane label="User">User</pacvue-tab-pane>
    <pacvue-tab-pane label="Config">Config</pacvue-tab-pane>
    <pacvue-tab-pane label="Role">Role</pacvue-tab-pane>
    <pacvue-tab-pane label="Task">Task</pacvue-tab-pane>
  </PacvueTab>
</template>
```

### Tab

```vue
<template>
  <PacvueTab style="width: 500px" class="demo-tabs" :type="'custom-default'" :tabItemMinWidth="'200px'">
    <pacvue-tab-pane label="User">
      <div style="height: 400px; width: 300px">User</div>
    </pacvue-tab-pane>
    <pacvue-tab-pane label="Config">Config</pacvue-tab-pane>
    <pacvue-tab-pane label="Role">Role</pacvue-tab-pane>
    <pacvue-tab-pane label="Task">Task</pacvue-tab-pane>
  </PacvueTab>
</template>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| type | 风格类型,可选值card/border-card/custom-default/custom-card,如果设置为custom-defualt，tab-position强制为left | String | -- |
| tabItemMinWidth | tab激活项的最小宽度 | String | 0px |
| tab-position | 选项卡所在位置:top/right/bottom/left | string | top |
| tabHeaderOffset | type 为 custom-default 时生效，tab项的顶部偏移量。 | string | 24px |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/tabs.html)

