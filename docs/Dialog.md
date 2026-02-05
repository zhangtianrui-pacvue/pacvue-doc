---
component: Dialog
category: feedback
tags: [对话框, 弹窗, 模态]
aliases: [Dialog, 对话框, 弹窗]
version: 1.0.0
description: "Dialog"
---

# Dialog 组件文档

> Dialog

**分类**: feedback | **标签**: 对话框、弹窗、模态

## 使用示例

### 3个尺寸和自定义

```vue
<template>
  <pacvue-button type="primary" style="margin-left: 16px" @click="dialogVisible1 = true">small Dialog</pacvue-button>
  <pacvue-button type="primary" style="margin-left: 16px" @click="dialogVisible2 = true">middle Dialog</pacvue-button>
  <pacvue-button type="primary" style="margin-left: 16px" @click="dialogVisible3 = true">big Dialog</pacvue-button>

  <pacvue-dialog
      v-model="dialogVisible1"
      title="I am the title1"
      pacSize="sm"
      ref="dialogRef"
      id="pacvue-dialog-Wrapper"
      :closeOptions="{
        dataCy: 'auto-2133333333999'
      }"
    >
      <span>Hi, there11111!</span>
      <div id="test"></div>
      <div :data-cy="'auto_component_00114'">{{ selectedProfileList }}</div>
      <PacvueSelect
        v-model="selectedProfileList"
        :data="marketUnBindingProfileObj"
        placeholder="Please Select"
        class="operate-item-content"
        style="width: 290px; margin-bottom: 20px"
        clearable
        :collapse-tags="false"
        :dataCy="'auto_component_00102'"
        :dataCyValue="'auto_component_00103'"
        :dataCyFilter="'auto_component_00104'"
      />
      <div :data-cy="'auto_component_00115'">{{ input }}</div>
      <pacvue-input :data-cy="'auto_component_00105'" v-model="input" placeholder="Please input" clearable type="number" :digitChar="['.', ',']" :digitCount="2" :min="10" :max="100">
        <template #suffix>
          <span>%</span>
        </template>
      </pacvue-input>
      <template #footer>
        <pacvue-button @click="dialogVisible1 = false" :data-cy="'auto_component_00106'">Cancel</pacvue-button>
        <pacvue-button type="primary" @click="dialogVisible1 = false" :data-cy="'auto_component_00107'">Confirm</pacvue-button>
      </template>
    </pacvue-dialog>
  <pacvue-dialog v-model="dialogVisible2" title="I am the title2" pacSize="md">
    <span>Hi, there1222222!</span>
    <template #footer>
      <pacvue-button @click="dialogVisible2 = false">Cancel</pacvue-button>
      <pacvue-button type="primary" @click="dialogVisible2 = false">Confirm</pacvue-button>
    </template>
  </pacvue-dialog>
  <pacvue-dialog v-model="dialogVisible3" title="I am the title3" pacSize="lg">
    <span>Hi, there33333!</span>
    <template #footer>
      <pacvue-button @click="dialogVisible3 = false">Cancel</pacvue-button>
      <pacvue-button type="primary" @click="dialogVisible3 = false">Confirm</pacvue-button>
    </template>
  </pacvue-dialog>
</template>
<script>
  import { ref, computed, reactive } from 'vue'
  import SvgComponent from '@pacvue/svg-icon'
  import { PacvueDownloadAnimation } from '@/components/pacvue-download-animation/index.js'
  export default {
    setup(props, ctx) {
      const rateVal = ref(2)
      const dialogVisible1 = ref(false)
      const dialogVisible2 = ref(false)
      const dialogVisible3 = ref(false)
      const input = ref('.1234555')

      const dialogProps = [
        ['pacSize', '弹框宽度 sm / md / lg, sm : 480px, md : 720px, lg : 940px', 'String', 'md'],
        ['draggable', '为 Dialog 启用可拖拽功能', 'boolean', 'false'],
        ['isKeepPrevFocus', '开启后，输入焦点从 Dialog 内容失焦时，使当前页面聚焦的元素失去焦点。', 'boolean', 'false'],
        ['closeOptions', 'close图标组件自定义配置', 'Object', '--'],
        ['closeIcon', 'close图标自定义', 'String | VueElement', '--'],
        ['innerDialog', '弹窗作为父容器的内部弹窗定位和显示，innerDialog 使用 absolute 定位，所以父容器需要显示设置 position。', 'boolean', 'false']
      ]
      const selectedProfileList = ref([])
      const marketUnBindingProfileObj = [
        {
          amazonAccountUserId: 'amzn1.account.AGK4P5B533QCYN5MOHFUPLEGGMNA',
          countryCode: 'US',
          profileId: '3070798222221384',
          profileName: 'Henkel Consumer Goods Canada, Inc',
          label: 'Henkel Consumer Goods Canada, Inc (3070798222221384)',
          value: '3070798222221384'
        },
        {
          amazonAccountUserId: 'amzn1.account.AGK4P5B533QCYN5MOHFUPLEGGMNB',
          countryCode: 'UK',
          profileId: '3070798222221385',
          profileName: 'Amazon Test Account',
          label: 'Amazon Test Account',
          value: 'Amazon Test Account'
        },
        {
          amazonAccountUserId: 'amzn1.account.AGK4P5B533QCYN5MOHFUPLEGGMNC',
          countryCode: 'CN',
          profileId: '3070798222221386',
          profileName: 'Walmart Test Account',
          label: 'Walmart Test Account',
          value: 'Walmart Test Account'
        }
      ]
      const dialogRef = ref(null)
      var scanDialogRef = () => {
        console.log('>>>>>>>>>dialogRef', dialogRef)
      }
      var PacvueIconStarfill = SvgComponent.PacvueIconStarfill
      var icons = [SvgComponent.PacvueIconStarfill, SvgComponent.PacvueIconStarfill, SvgComponent.PacvueIconStarfill]
      var voidIcon = SvgComponent.PacvueIconUnStarred
      var toEl = ref(null)
      var setToEl = () => {
        toEl.value = '#pacvue-dialog-Wrapper'
      }
      var testFn = () => {}
      return {
        dialogVisible1,
        dialogVisible2,
        dialogVisible3,
        dialogProps,
        selectedProfileList,
        marketUnBindingProfileObj,
        dialogRef,
        scanDialogRef,
        rateVal,
        icons,
        voidIcon,
        setToEl,
        toEl,
        testFn,
        PacvueIconStarfill,
        input
      }
    }
  }
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| pacSize | 弹框宽度 sm / md / lg, sm : 480px, md : 720px, lg : 940px | String | md |
| draggable | 为 Dialog 启用可拖拽功能 | boolean | false |
| isKeepPrevFocus | 开启后，输入焦点从 Dialog 内容失焦时，使当前页面聚焦的元素失去焦点。 | boolean | false |
| closeOptions | close图标组件自定义配置 | Object | -- |
| closeIcon | close图标自定义 | String \| VueElement | -- |
| innerDialog | 弹窗作为父容器的内部弹窗定位和显示,innerDialog 使用 absolute 定位，所以父容器需要显示设置 position。 | boolean | false |
| isBulkDialog | 是否是批量操作的弹窗 | Boolean | false |
| bulkTitleTemplate | 批量操作弹窗的标题模板 | String | Bulk {0} |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/dialog.html)

