---
component: DocDemo
category: other
tags: [DocDemo]
aliases: [DocDemo]
version: 1.0.0
description: "1、根容器组件 DocBox"
---

# DocDemo 组件文档

> 1、根容器组件 DocBox

## 使用示例

### 组件文档页面必须使用 DocBox 标签作为根标签

```vue
<template>
  <DocBox> ...文档内容 </DocBox>
</template>
```

### 作为每个组件展示模块的标题，并且用于生成右侧导航栏

```vue
<template>
  <DocBox>
    <HPoint id="Button" :title="'Button xxx'" />
  </DocBox>
</template>
```

### 用于展示 一组 组件样式或 props、function、event、slot 的配置参数信息，

```vue
<template>
  <DocBox>
    <DocCard :describe="'展示 一组 组件样式'" :codeFile="'/DocDemo/DocDemo4'">
      <el-row>
        <el-col :sm="12" :lg="6">
          <el-result icon="success" title="成功提示" subTitle="请根据提示进行操作">
            <template slot="extra">
              <el-button type="primary" size="medium">返回</el-button>
            </template>
          </el-result>
        </el-col>
        <el-col :sm="12" :lg="6">
          <el-result icon="warning" title="警告提示" subTitle="请根据提示进行操作">
            <template slot="extra">
              <el-button type="primary" size="medium">返回</el-button>
            </template>
          </el-result>
        </el-col>
      </el-row>
    </DocCard>
    <DocCard :describe="'props-属性展示'" :infoType="'props'" :infoData="infoData"></DocCard>
    <DocCard :describe="'event-属性展示'" :infoType="'event'" :infoData="infoData"></DocCard>
    <DocCard :describe="'function-属性展'" :infoType="'function'" :infoData="infoData"></DocCard>
    <DocCard :describe="'slot-属性展示'" :infoType="'slots'" :infoData="infoData"></DocCard>
  </DocBox>
</template>

<script>
  import { reactive, ref } from 'vue'
  export default {
    name: 'DocDemo',
    setup(props, ctx) {
      const infoData = [
        ['111111', 'fgdsg飒飒', '所发放的', '撒旦发顺丰'],
        ['2222', '撒旦发顺丰', '撒发顺丰', '啊额我让'],
        ['333333', '撒旦发射点范德萨分', '撒打发说法萨芬', '发发大师傅撒法']
      ]
      return {
        infoData
      }
    }
  }
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| 111111 | fgdsg飒飒 | 所发放的 | 撒旦发顺丰 |
| 2222 | 撒旦发顺丰 | 撒发顺丰 | 啊额我让 |
| 333333 | 撒旦发射点范德萨分 | 撒打发说法萨芬 | 发发大师傅撒法 |
| id | 必填值，标签的原生 id 属性 ，用于锚点定位功能，必须不可重复。如果为空则不生成右侧锚点定位 tab | String | -- |
| title | 标题的文字内容 | String | -- |
| outlink | 此项需要提供一个有效的网页地址，设置此值后标题会渲染为一个超链接，用于标题点击后打开相应的网页 | String | -- |
| describe | 卡片头部的自定义描述文字，不设置或设置了 describe 插槽则隐藏 | String | -- |
| codeFile | 查看源码功能 的 源码内容文件 的 带文件路径的全称，源码文件必须放置于 src/code/ 路径中，所以路径全名只用设置 src/code/ 后的部分，不设置则隐藏源码展示功能 | String | -- |
| infoType | 用于判断卡片的展示类型，共有5中展示类型：1、props 2、function 3、event 4、slots 5、default 的配置参数信息 | String | -- |
| infoData | 配置了 infoType 后，用于展示相应 infoType 信息的数据，格式为一个二维数组，子数组根据 infoType 不同按照索引位置设置展示文字，详情请看 infoData 配置参数 | Array | -- |

## 方法 Methods

组件暴露的方法，可通过 ref 调用。

| 方法名 | 说明 | 参数 |
| --- | --- | --- |
| 111111 | fgdsg飒飒 | 所发放的 |
| 2222 | 撒旦发顺丰 | 撒发顺丰 |
| 333333 | 撒旦发射点范德萨分 | 撒打发说法萨芬 |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| 111111 | fgdsg飒飒 | 所发放的 |
| 2222 | 撒旦发顺丰 | 撒发顺丰 |
| 333333 | 撒旦发射点范德萨分 | 撒打发说法萨芬 |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| 111111 | fgdsg飒飒 | 所发放的 |
| 2222 | 撒旦发顺丰 | 撒发顺丰 |
| 333333 | 撒旦发射点范德萨分 | 撒打发说法萨芬 |
| default | 所有 default 都会作为展示内容在卡片中显示 | -- |
| describe | 描述内容插槽，当需要显示复杂的自定义描述文字时使用， 使用此插槽会使 props 中的 describe 属性失效 | -- |

## 其他信息

| 参数名 | 说明 | 配置方式展示 |
| --- | --- | --- |
| props | 二维数组中的子数组各索引代表的值为 [属性, 说明, 类型, 默认值] | [[1,2,3,4], [1,2,3,4]] |
| function | 二维数组中的子数组各索引代表的值为 [方法名, 说明, 参数] | [[1,2,3], [1,2,3]] |
| event | 二维数组中的子数组各索引代表的值为 [事件名, 说明, 回调参数] | [[1,2,3], [1,2,3]] |
| slots | 二维数组中的子数组各索引代表的值为 [插槽名, 说明, 子标签] | [[1,2,3], [1,2,3]] |
| default | 二维数组中的第一个 子数组 用于定义数据每列的标题，之后子数组各索引代表 自定义列的展示内容 | [[标题1, 标题2, ...], [内容1, 内容2, ...]] |

