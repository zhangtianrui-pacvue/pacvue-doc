---
component: Guide
category: feedback
tags: [引导, 新手引导, 教程]
aliases: [Guide, 引导]
version: 1.0.0
description: "页面中使用"
---

# Guide 组件文档

> 页面中使用

**分类**: feedback | **标签**: 引导、新手引导、教程

## 使用示例

### 页面中使用

```vue
<template>
  <PacvueButton :plain="true" @click="startGuide">开启新手指南</PacvueButton>
  <PacvueButton :plain="true" id="Step1">success</PacvueButton>
  <PacvueButton :plain="true" id="Step2">warning</PacvueButton>
  <PacvueButton :plain="true" id="Step3">error</PacvueButton>
</template>

<script setup>
  import { ref, defineComponent, h, onMounted, nextTick } from 'vue'
  import { PacvueMessage } from '../components/pacvue-message/index.js'
  import PacvueGuide from '../components/pacvue-guide/index.js'

  const defineSteps = [
    {
      element: '#Step1',
      popover: {
        title: '',
        description:
          'All metrics can be filtered, here. In this section you can select metrics and establish data ranges for filtering and sorting.',
        position: 'top-left'
      }
    },
    {
      element: '#Step2',
      popover: {
        title: '',
        description:
          'Pre-set filters are stored in this section. You can apply a Saved filter, edit, or delete Saved plans.',
        position: 'top-left'
      }
    },
    {
      element: '#Step3',
      popover: {
        title: '',
        description:
          'If you’d like, you can switch back to the old filter, which will be available for a limited time. You’re free to switch back and forth between old and new. ',
        position: 'bottom-left'
      }
    }
  ]
  var guideHandler = null
  onMounted(() => {
    guideHandler = acvueGuide({ steps: defineSteps })P
  })
  var startGuide = () => {
    guideHandler?.start()
  }
</script>
<style>
  .el-message {
    height: 40px;
  }

  .el-message--info .el-message__content {
    color: #66666c;
  }

  .pacvue-message-success {
    color: var(--el-color-success);
  }

  .pacvue-message-warning {
    color: var(--project-orange);
  }

  .pacvue-message-error {
    color: var(--el-color-danger);
  }

  .el-message {
    border-radius: 6px;
  }

  .el-message img {
    width: 20px;
    height: 20px;
  }
</style>
```

### Dialog中使用

```vue
<template>
  <PacvueButton @click="openDialog">Open Dialog</PacvueButton>
  <!-- 弹窗 -->
  <pacvue-dialog v-model="dialogVisible1" title="I am the title1" pacSize="sm" @opened="dialogOpened">
    <span>Hi, there11111!</span>
    <PacvueButton :plain="true" id="Step1_1">Step 1</PacvueButton>
    <PacvueButton :plain="true" id="Step2_2">Step 2</PacvueButton>
    <PacvueButton :plain="true" id="Step3_3">Step 3</PacvueButton>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogVisible1 = false">Cancel</el-button>
        <el-button type="primary" @click="dialogVisible1 = false">Confirm</el-button>
      </span>
    </template>
  </pacvue-dialog>
  <!-- 弹窗 -->
</template>

<script setup>
  import { ref, defineComponent, h, onMounted, nextTick } from 'vue'
  import PacvueGuide from '../components/pacvue-guide/index.js'
  //弹窗新手指南使用
  var dialogVisible1 = ref(false)
  var openDialog = () => {
    dialogVisible1.value = true
  }
  const defineSteps2 = [
    {
      element: '#Step1_1',
      popover: {
        title: '',
        description:
          'All metrics can be filtered, here. In this section you can select metrics and establish data ranges for filtering and sorting.',
        position: 'top-left'
      }
    },
    {
      element: '#Step2_2',
      popover: {
        title: '',
        description:
          'Pre-set filters are stored in this section. You can apply a Saved filter, edit, or delete Saved plans.',
        position: 'top-left'
      }
    },
    {
      element: '#Step3_3',
      popover: {
        title: '',
        description:
          'If you’d like, you can switch back to the old filter, which will be available for a limited time. You’re free to switch back and forth between old and new. ',
        position: 'bottom-left'
      }
    }
  ]
  var dialogOpened = () => {
    PacvueGuide({ steps: defineSteps2 })
  }
</script>
<style>
  .el-message {
    height: 40px;
  }

  .el-message--info .el-message__content {
    color: #66666c;
  }

  .pacvue-message-success {
    color: var(--el-color-success);
  }

  .pacvue-message-warning {
    color: var(--project-orange);
  }

  .pacvue-message-error {
    color: var(--el-color-danger);
  }

  .el-message {
    border-radius: 6px;
  }

  .el-message img {
    width: 20px;
    height: 20px;
  }
</style>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| steps | 新手指南的步骤,Array<StepInfo>,StepInfo具体参考如下 | Array | [] |
| autoStart | 是否自动运行 | Boolean | true |
| stageBackGround | mask背景色 | String | rgba(0,0,0,0.50) |
| onReset | 重置的回调事件 | Function | -- |
| extraOptions | 组件其他的额外配置,注意extraOptios中配置优先级高,包含自定义按钮配置(customBtns:Array<{label:String,onClick:Function<{event,reset}>,classList:Array<String>}>) | Object | -- |
| skipBtnText | Skip按钮的文案 | String | Skip |
| showSkipBtn | 是否显示Skip按钮 | Boolean | false |
| start | 开启新手指南 | Function | -- |
| element | 触发新手指导的元素 | String | -- |
| popover | 新手指导详细的配置,具体参考PopoverInfo配置 | Object | -- |
| title | 标题 | String | -- |
| description | 描述信息 | Object | -- |
| position | popover显示的位置，bottom-left\|top-left | String | -- |

