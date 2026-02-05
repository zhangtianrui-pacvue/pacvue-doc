---
component: Steps
category: navigation
tags: [步骤条, 导航, 流程]
aliases: [Steps, 步骤]
version: 1.0.0
description: "默认成功状态的步骤条"
---

# Steps 组件文档

> 默认成功状态的步骤条

**分类**: navigation | **标签**: 步骤条、导航、流程

## 使用示例

### 默认 finish-status 属性为success 可以改变已经完成的步骤的状态为成功。

```vue
<template>
  <pacvue-steps :active="active1" type="movement" @stepClick="stepClick">
    <pacvue-step :data-cy="'auto_component_00125'">
      <template #title>Campaign Setting</template>
      <template #subtitle>
        <el-icon>
          <PacvueIconTipsExclamation />
        </el-icon>
      </template>
    </pacvue-step>
    <pacvue-step title="AdGroup Setting" descrTooltip="testwww" :data-cy="'auto_component_00126'" />
    <pacvue-step title="Target Setting" :data-cy="'auto_component_00127'" />
    <pacvue-step title="Negative Target Setting" :data-cy="'auto_component_00128'" />
  </pacvue-steps>
  <el-button style="margin-top: 20px" @click="next1">Next step</el-button>
</template>
<script setup>
  import { ref } from 'vue'
  const active1 = ref(0)
  const next1 = () => {
    if (active1.value++ > 3) active1.value = 0
  }
  const stepClick = (index) => {
    console.log({ index })
  }
</script>
```

### 每一步都有描述。

```vue
<template>
  <pacvue-steps :active="active2">
    <pacvue-step title="Campaign Setting" descrTooltip="sdfdsfdsf">
      <template #description>
        辅助描述辅助描述辅助描述
        12321321321
      </template>
    </pacvue-step>
    <pacvue-step title="AdGroup Setting" description="辅助描述辅助描述辅助描述" />
    <pacvue-step title="Target Setting" description="辅助描述辅助描述辅助描述" />
    <pacvue-step title="Negative Target Setting" description="辅助描述辅助描述辅助描述" />
  </pacvue-steps>
  <el-button style="margin-top: 20px;" @click="next2">Next step</el-button>
</template>
<script setup>
  import { ref } from 'vue'
  const active2 = ref(0)
  const next = () => {
    if (active2.value++ > 3) active2.value = 0
  }
</script>
```

### 只需要在 pacvue-steps 元素中设置 direction 属性为 vertical 即可。

```vue
<template>
  <div style="height: 300px;">
    <pacvue-steps :active="active3" direction="vertical">
      <pacvue-step title="Step 1" description="Some description" />
      <pacvue-step title="Step 2" description="Some description" />
      <pacvue-step title="Step 3" description="Some description" />
    </pacvue-steps>
  </div>
  <el-button style="margin-top: 20px;" @click="next3">Next step</el-button>
</template>
<script setup>
  import { ref } from 'vue'
  const active3 = ref(0)
  const next = () => {
    if (active3.value++ > 2) active3.value = 0
  }
</script>
```

### 可以在步骤栏中使用各种自定义图标。 通过 icon 属性来设置图标， 图标的类型可以参考 Icon

```vue
<template>
  <pacvue-steps :active="active4">
    <pacvue-step title="Step 1" :icon="Edit" />
    <pacvue-step title="Step 2"
      ><template #icon
        ><el-icon><Edit /></el-icon
      ></template>
    </pacvue-step>
    <pacvue-step title="Step 3" />
  </pacvue-steps>
  <el-button style="margin-top: 20px;" @click="next4">Next step</el-button>
</template>
<script setup>
  import { ref } from 'vue'
  const active4 = ref(0)
  const next = () => {
    if (active4.value++ > 2) active4.value = 0
  }
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| active | 设置当前激活步骤 | number | 0 |
| direction | 显示方向 | 'vertical' \| 'horizontal' | horizontal |
| type | 步骤条类型（default：默认类型；movement：可点击类型） | 'default' \| 'movement' | default |
| beforeStepClick | type 为 movement 时生效，点击 step 元素时触发，如果返回 false 则阻止 stepClick 事件触发及步进逻辑执行。 | Function | () => boolean |
| title | 标题 | string | -- |
| descrTooltip | 配置了该属性，则在step后增加 注意图标，并悬停显示 tooltip 文字 | string | -- |
| description | 描述文案 | string | -- |

## 方法 Methods

组件暴露的方法，可通过 ref 调用。

| 方法名 | 说明 | 参数 |
| --- | --- | --- |
| stepClick | type 为 movement 时生效，触发 step 元素 click 事件。 | (index) => {} |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| stepClick | type 为 movement 时生效，点击 step 元素时触发。 | (index) => {} |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| title | 自定义标题 | -- |
| description | 自定义描述文案 | -- |
| icon | 自定义图标 | -- |
| subtitle | title 插槽右侧自定义插槽 | -- |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/steps.html#steps-%E5%B1%9E%E6%80%A7)

