---
component: reportColumn
category: other
tags: [reportColumn]
aliases: [reportColumn]
version: 1.0.0
description: "PacvueReportColumn组件基础用法"
---

# reportColumn 组件文档

> PacvueReportColumn组件基础用法

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| data | 显示的列表数据,数据格式为DataConfig<{ groupName:String, label:String, value: String, lastPeriods: Array, disabled: Boolean, required: Boolean }> | Array | [] |
| v-model/modelValue | 绑定选中的值 | Object | -- |
| props | 配置选项，具体看下表ProsConfig | Object | { value: 'value', label: 'label', children: 'children' } |
| groupWidth | 显示分组元素的宽度 | Number\|String | -- |
| isValRecusion | 是否开启逆向匹配功能 | Boolean | false |
| showGroupNum | 是否显示group的count | Boolean | true |
| isTrueId | tree 节点 id 是否不重复，当节点 id 可能重复时需要设置此属性。true：不重复。false：可能重复 | Boolean | false |
| showType | 复制图标显示类型，visbile是常显示，hover是鼠标hover上去才显示 | visible\|hover | visible |
| label | 指定节点标签为节点对象的某个属性值 | String | -- |
| value | 指定节点value为节点对象的某个属性值 | String | -- |
| children | 指定子树为节点对象的某个属性值 | String | -- |
| groupName | 分组名称 | String | -- |
| label | 显示数据节点名称 | String | -- |
| value | 数据的id | String | -- |
| children | 子列表数据 | Array<{label,value,lastPeriods}> | [] |
| lastPeriods | 上期数据信息 | Array<DataConfig> | -- |
| disabled | 是否禁用。是否禁用组件，禁用后无法进行交互 | Boolean | false |
| required | 是否必须选中 | Boolean | false |

