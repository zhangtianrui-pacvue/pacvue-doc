---
component: Dropdown
category: navigation
tags: [下拉菜单, 导航, 菜单]
aliases: [Dropdown, 下拉菜单]
version: 1.0.0
description: "Dropdown 下拉菜单基础用法"
---

# Dropdown 组件文档

> Dropdown 下拉菜单基础用法

**分类**: navigation | **标签**: 下拉菜单、导航、菜单

## 使用示例

### 悬停或者点击在下拉菜单上以展开更多操作。

```vue
<template>
  <p class="mb-4">default</p>
  <el-row class="mb-4">
    <pacvue-dropdown :data="options" :disabled="false" @command="commandChange">
      <template #reference>
        <el-button ref="buttonRef">Click me</el-button>
      </template>
    </pacvue-dropdown>
  </el-row>
</template>
<script setup>
  var commandChange = (val) => {
    console.log('val', val)
  }
  const options = [
    {
      value: 'component',
      label: 'Component',
      children: [
        {
          value: 'basic',
          label: 'Basic',
          children: [
            {
              value: 'layout',
              label: 'Layout'
            },
            {
              value: 'color',
              label: 'Color'
            },
            {
              value: 'typography',
              label: 'Typography'
            },
            {
              value: 'icon',
              label: 'Icon'
            },
            {
              value: 'button',
              label: 'Button'
            }
          ]
        },
        {
          value: 'form',
          label: 'Form',
          children: [
            {
              value: 'radio',
              label: 'Radio'
            },
            {
              value: 'checkbox',
              label: 'Checkbox'
            },
            {
              value: 'input',
              label: 'Input'
            },
            {
              value: 'input-number',
              label: 'InputNumber'
            },
            {
              value: 'select',
              label: 'Select'
            },
            {
              value: 'cascader',
              label: 'Cascader'
            },
            {
              value: 'switch',
              label: 'Switch'
            },
            {
              value: 'slider',
              label: 'Slider'
            },
            {
              value: 'time-picker',
              label: 'TimePicker'
            },
            {
              value: 'date-picker',
              label: 'DatePicker'
            },
            {
              value: 'datetime-picker',
              label: 'DateTimePicker'
            },
            {
              value: 'upload',
              label: 'Upload'
            },
            {
              value: 'rate',
              label: 'Rate'
            },
            {
              value: 'form',
              label: 'Form'
            }
          ]
        },
        {
          value: 'data',
          label: 'Data',
          children: [
            {
              value: 'table',
              label: 'Table'
            },
            {
              value: 'tag',
              label: 'Tag'
            },
            {
              value: 'progress',
              label: 'Progress'
            },
            {
              value: 'tree',
              label: 'Tree'
            },
            {
              value: 'pagination',
              label: 'Pagination'
            },
            {
              value: 'badge',
              label: 'Badge'
            }
          ]
        },
        {
          value: 'notice',
          label: 'Notice',
          children: [
            {
              value: 'alert',
              label: 'Alert'
            },
            {
              value: 'loading',
              label: 'Loading'
            },
            {
              value: 'message',
              label: 'Message'
            },
            {
              value: 'message-box',
              label: 'MessageBox'
            },
            {
              value: 'notification',
              label: 'Notification'
            }
          ]
        },
        {
          value: 'navigation',
          label: 'Navigation',
          children: [
            {
              value: 'menu',
              label: 'Menu'
            },
            {
              value: 'tabs',
              label: 'Tabs'
            },
            {
              value: 'breadcrumb',
              label: 'Breadcrumb'
            },
            {
              value: 'dropdown',
              label: 'Dropdown'
            },
            {
              value: 'steps',
              label: 'Steps'
            }
          ]
        },
        {
          value: 'others',
          label: 'Others',
          children: [
            {
              value: 'dialog',
              label: 'Dialog'
            },
            {
              value: 'tooltip',
              label: 'Tooltip'
            },
            {
              value: 'popover',
              label: 'Popover'
            },
            {
              value: 'card',
              label: 'Card'
            },
            {
              value: 'carousel',
              label: 'Carousel'
            },
            {
              value: 'collapse',
              label: 'Collapse'
            }
          ]
        }
      ]
    },
    {
      value: 'resource',
      label: 'Resource',
      children: [
        {
          value: 'axure',
          label: 'Axure Components'
        },
        {
          value: 'sketch',
          label: 'Sketch Templates'
        },
        {
          value: 'docs',
          label: 'Design Documentation'
        }
      ]
    }
  ]
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### 你可以使用 disabled 属性来定义按钮是否被禁用。 使用 disabled

```vue
<template>
  <el-row class="mb-4">
    <pacvue-dropdown :data="options" :disabled="true" @command="commandChange">
      <template #reference>
        <el-button ref="buttonRef" :disabled="true">Click me</el-button>
      </template>
    </pacvue-dropdown>
    <div style="padding-left: 40px">
      <pacvue-dropdown :data="options" @command="commandChange">
        <template #reference>
          <el-button ref="buttonRef">Click me</el-button>
        </template>
      </pacvue-dropdown>
    </div>
  </el-row>
</template>

<script setup>
  var commandChange = (val) => {
    console.log('val', val)
  }
  const options = [
    {
      value: 'component',
      label: 'Component',
      children: [
        {
          value: 'basic',
          label: 'Basic',
          children: [
            {
              value: 'layout',
              label: 'Layout'
            },
            {
              value: 'color',
              label: 'Color'
            },
            {
              value: 'typography',
              label: 'Typography'
            },
            {
              value: 'icon',
              label: 'Icon'
            },
            {
              value: 'button',
              label: 'Button'
            }
          ]
        },
        {
          value: 'form',
          label: 'Form',
          children: [
            {
              value: 'radio',
              label: 'Radio'
            },
            {
              value: 'checkbox',
              label: 'Checkbox'
            },
            {
              value: 'input',
              label: 'Input'
            },
            {
              value: 'input-number',
              label: 'InputNumber'
            },
            {
              value: 'select',
              label: 'Select'
            },
            {
              value: 'cascader',
              label: 'Cascader'
            },
            {
              value: 'switch',
              label: 'Switch'
            },
            {
              value: 'slider',
              label: 'Slider'
            },
            {
              value: 'time-picker',
              label: 'TimePicker'
            },
            {
              value: 'date-picker',
              label: 'DatePicker'
            },
            {
              value: 'datetime-picker',
              label: 'DateTimePicker'
            },
            {
              value: 'upload',
              label: 'Upload'
            },
            {
              value: 'rate',
              label: 'Rate'
            },
            {
              value: 'form',
              label: 'Form'
            }
          ]
        },
        {
          value: 'data',
          label: 'Data',
          children: [
            {
              value: 'table',
              label: 'Table'
            },
            {
              value: 'tag',
              label: 'Tag'
            },
            {
              value: 'progress',
              label: 'Progress'
            },
            {
              value: 'tree',
              label: 'Tree'
            },
            {
              value: 'pagination',
              label: 'Pagination'
            },
            {
              value: 'badge',
              label: 'Badge'
            }
          ]
        },
        {
          value: 'notice',
          label: 'Notice',
          children: [
            {
              value: 'alert',
              label: 'Alert'
            },
            {
              value: 'loading',
              label: 'Loading'
            },
            {
              value: 'message',
              label: 'Message'
            },
            {
              value: 'message-box',
              label: 'MessageBox'
            },
            {
              value: 'notification',
              label: 'Notification'
            }
          ]
        },
        {
          value: 'navigation',
          label: 'Navigation',
          children: [
            {
              value: 'menu',
              label: 'Menu'
            },
            {
              value: 'tabs',
              label: 'Tabs'
            },
            {
              value: 'breadcrumb',
              label: 'Breadcrumb'
            },
            {
              value: 'dropdown',
              label: 'Dropdown'
            },
            {
              value: 'steps',
              label: 'Steps'
            }
          ]
        },
        {
          value: 'others',
          label: 'Others',
          children: [
            {
              value: 'dialog',
              label: 'Dialog'
            },
            {
              value: 'tooltip',
              label: 'Tooltip'
            },
            {
              value: 'popover',
              label: 'Popover'
            },
            {
              value: 'card',
              label: 'Card'
            },
            {
              value: 'carousel',
              label: 'Carousel'
            },
            {
              value: 'collapse',
              label: 'Collapse'
            }
          ]
        }
      ]
    },
    {
      value: 'resource',
      label: 'Resource',
      children: [
        {
          value: 'axure',
          label: 'Axure Components'
        },
        {
          value: 'sketch',
          label: 'Sketch Templates'
        },
        {
          value: 'docs',
          label: 'Design Documentation'
        }
      ]
    }
  ]
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### 你可以使用 default插槽去格式化显示内容。

```vue
<template>
  <el-row class="mb-4">
    <pacvue-dropdown :data="options" @command="commandChange">
      <template #reference>
        <el-button ref="buttonRef">Click me</el-button>
      </template>
      <template #default="{ data, parntData }">
        <el-icon color="#409EFC" class="no-inherit">
          <Share />
        </el-icon>
        {{ data.label }}
      </template>
    </pacvue-dropdown>
  </el-row>
</template>

<script setup>
  var commandChange = (val) => {
    console.log('val', val)
  }
  const options = [
    {
      value: 'component',
      label: 'Component',
      children: [
        {
          value: 'basic',
          label: 'Basic',
          children: [
            {
              value: 'layout',
              label: 'Layout'
            },
            {
              value: 'color',
              label: 'Color'
            },
            {
              value: 'typography',
              label: 'Typography'
            },
            {
              value: 'icon',
              label: 'Icon'
            },
            {
              value: 'button',
              label: 'Button'
            }
          ]
        },
        {
          value: 'form',
          label: 'Form',
          children: [
            {
              value: 'radio',
              label: 'Radio'
            },
            {
              value: 'checkbox',
              label: 'Checkbox'
            },
            {
              value: 'input',
              label: 'Input'
            },
            {
              value: 'input-number',
              label: 'InputNumber'
            },
            {
              value: 'select',
              label: 'Select'
            },
            {
              value: 'cascader',
              label: 'Cascader'
            },
            {
              value: 'switch',
              label: 'Switch'
            },
            {
              value: 'slider',
              label: 'Slider'
            },
            {
              value: 'time-picker',
              label: 'TimePicker'
            },
            {
              value: 'date-picker',
              label: 'DatePicker'
            },
            {
              value: 'datetime-picker',
              label: 'DateTimePicker'
            },
            {
              value: 'upload',
              label: 'Upload'
            },
            {
              value: 'rate',
              label: 'Rate'
            },
            {
              value: 'form',
              label: 'Form'
            }
          ]
        },
        {
          value: 'data',
          label: 'Data',
          children: [
            {
              value: 'table',
              label: 'Table'
            },
            {
              value: 'tag',
              label: 'Tag'
            },
            {
              value: 'progress',
              label: 'Progress'
            },
            {
              value: 'tree',
              label: 'Tree'
            },
            {
              value: 'pagination',
              label: 'Pagination'
            },
            {
              value: 'badge',
              label: 'Badge'
            }
          ]
        },
        {
          value: 'notice',
          label: 'Notice',
          children: [
            {
              value: 'alert',
              label: 'Alert'
            },
            {
              value: 'loading',
              label: 'Loading'
            },
            {
              value: 'message',
              label: 'Message'
            },
            {
              value: 'message-box',
              label: 'MessageBox'
            },
            {
              value: 'notification',
              label: 'Notification'
            }
          ]
        },
        {
          value: 'navigation',
          label: 'Navigation',
          children: [
            {
              value: 'menu',
              label: 'Menu'
            },
            {
              value: 'tabs',
              label: 'Tabs'
            },
            {
              value: 'breadcrumb',
              label: 'Breadcrumb'
            },
            {
              value: 'dropdown',
              label: 'Dropdown'
            },
            {
              value: 'steps',
              label: 'Steps'
            }
          ]
        },
        {
          value: 'others',
          label: 'Others',
          children: [
            {
              value: 'dialog',
              label: 'Dialog'
            },
            {
              value: 'tooltip',
              label: 'Tooltip'
            },
            {
              value: 'popover',
              label: 'Popover'
            },
            {
              value: 'card',
              label: 'Card'
            },
            {
              value: 'carousel',
              label: 'Carousel'
            },
            {
              value: 'collapse',
              label: 'Collapse'
            }
          ]
        }
      ]
    },
    {
      value: 'resource',
      label: 'Resource',
      children: [
        {
          value: 'axure',
          label: 'Axure Components'
        },
        {
          value: 'sketch',
          label: 'Sketch Templates'
        },
        {
          value: 'docs',
          label: 'Design Documentation'
        }
      ]
    }
  ]
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### 有时候我们想把dropdown的触发元素放在别的地方，而不需要写在一起，这时候就可以使用虚拟触发。

```vue
<template>
  <el-row class="mb-4">
    <pacvue-dropdown
      :data="options"
      @command="commandChange"
      virtual-triggering
      :virtual-ref="triggerRef"
      :offset="3"
      :offsetX="50"
      :popper-options="{
      modifiers: [
        {
          name: 'computeStyles',
          options: {
            adaptive: false,
            enabled: false
          }
        }
      ]
    }"
    >
      <template #default="{ data, parntData }">
        <el-icon color="#409EFC" class="no-inherit">
          <Share />
        </el-icon>
        {{ data.label }}
      </template>
    </pacvue-dropdown>
    <el-icon color="#409EFC" class="no-inherit" ref="triggerRef">
      <Share />
    </el-icon>
  </el-row>
</template>

<script setup>
  import { ref } from 'vue'
  var triggerRef = ref(null)
  var commandChange = (val) => {
    console.log('val', val)
  }
  const options = [
    {
      value: 'component',
      label: 'Component',
      children: [
        {
          value: 'basic',
          label: 'Basic',
          children: [
            {
              value: 'layout',
              label: 'Layout'
            },
            {
              value: 'color',
              label: 'Color'
            },
            {
              value: 'typography',
              label: 'Typography'
            },
            {
              value: 'icon',
              label: 'Icon'
            },
            {
              value: 'button',
              label: 'Button'
            }
          ]
        },
        {
          value: 'form',
          label: 'Form',
          children: [
            {
              value: 'radio',
              label: 'Radio'
            },
            {
              value: 'checkbox',
              label: 'Checkbox'
            },
            {
              value: 'input',
              label: 'Input'
            },
            {
              value: 'input-number',
              label: 'InputNumber'
            },
            {
              value: 'select',
              label: 'Select'
            },
            {
              value: 'cascader',
              label: 'Cascader'
            },
            {
              value: 'switch',
              label: 'Switch'
            },
            {
              value: 'slider',
              label: 'Slider'
            },
            {
              value: 'time-picker',
              label: 'TimePicker'
            },
            {
              value: 'date-picker',
              label: 'DatePicker'
            },
            {
              value: 'datetime-picker',
              label: 'DateTimePicker'
            },
            {
              value: 'upload',
              label: 'Upload'
            },
            {
              value: 'rate',
              label: 'Rate'
            },
            {
              value: 'form',
              label: 'Form'
            }
          ]
        },
        {
          value: 'data',
          label: 'Data',
          children: [
            {
              value: 'table',
              label: 'Table'
            },
            {
              value: 'tag',
              label: 'Tag'
            },
            {
              value: 'progress',
              label: 'Progress'
            },
            {
              value: 'tree',
              label: 'Tree'
            },
            {
              value: 'pagination',
              label: 'Pagination'
            },
            {
              value: 'badge',
              label: 'Badge'
            }
          ]
        },
        {
          value: 'notice',
          label: 'Notice',
          children: [
            {
              value: 'alert',
              label: 'Alert'
            },
            {
              value: 'loading',
              label: 'Loading'
            },
            {
              value: 'message',
              label: 'Message'
            },
            {
              value: 'message-box',
              label: 'MessageBox'
            },
            {
              value: 'notification',
              label: 'Notification'
            }
          ]
        },
        {
          value: 'navigation',
          label: 'Navigation',
          children: [
            {
              value: 'menu',
              label: 'Menu'
            },
            {
              value: 'tabs',
              label: 'Tabs'
            },
            {
              value: 'breadcrumb',
              label: 'Breadcrumb'
            },
            {
              value: 'dropdown',
              label: 'Dropdown'
            },
            {
              value: 'steps',
              label: 'Steps'
            }
          ]
        },
        {
          value: 'others',
          label: 'Others',
          children: [
            {
              value: 'dialog',
              label: 'Dialog'
            },
            {
              value: 'tooltip',
              label: 'Tooltip'
            },
            {
              value: 'popover',
              label: 'Popover'
            },
            {
              value: 'card',
              label: 'Card'
            },
            {
              value: 'carousel',
              label: 'Carousel'
            },
            {
              value: 'collapse',
              label: 'Collapse'
            }
          ]
        }
      ]
    },
    {
      value: 'resource',
      label: 'Resource',
      children: [
        {
          value: 'axure',
          label: 'Axure Components'
        },
        {
          value: 'sketch',
          label: 'Sketch Templates'
        },
        {
          value: 'docs',
          label: 'Design Documentation'
        }
      ]
    }
  ]
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| placement | dropdown 菜单显示的位置，可选项top/top-start/top-end/bottom/bottom-start/bottom-end | String | bottom-start |
| data | 数据列表。数据源，用于渲染组件内容 | Array | [] |
| props | 配置选项，具体看下表 | Object | { value: 'value', label: 'label', children: 'children' } |
| filterable | 是否可以过滤功能。是否支持筛选/搜索功能 | Boolean | true |
| filterablePlaceholder | 过滤输入框的placeholder | Array | Please input keyword |
| disabled | 是否禁用。是否禁用组件，禁用后无法进行交互 | Boolean | false |
| trigger | 触发类型，可选项click，hover | String | click |
| v-model/modelValue | 绑定的值 | String\|Number | - |
| keepActive | 是否保留选中值 | Boolean | false |
| dropdownMinHeight | 下拉列表最小的高度 | String | 0px |
| loading | 是否显示loading。是否显示加载状态 | Boolean | false |
| virtualTriggering | 用来标识虚拟触发是否被启用 | Boolean | false |
| virtualRef | 标识虚拟触发时的触发元素 | Object | -- |
| offset | 下拉框出现位置的垂直偏移量 | Number | 4 |
| offsetX | 下拉框出现位置的水平偏移量 | Number | 0 |
| popperOptions | 请参考popper.js 参数，相关链接为https://popper.js.org/docs/v2/ | Object | -- |
| dropdownMaxHeight | 下拉列表最大的高度 | String\|Function({parentNode}) | -- |
| z-index | 下拉列表层级，优先级高于isAutoCustomZIndex | Number | -- |
| isAutoCustomZIndex | 是否使用用户自定义的层级计算规则，即在body中的默认都是999,在弹框中层级会自动计算 | Boolean | false |
| isVirtual | 是否开启虚拟滚动,只支持两级 | Boolean | false |
| itemSize | 启虚拟滚动行高 | Number | 40 |
| isUseNewMode | 是否使用新模式,该模式支持多级 | Boolean | false |
| label | 指定节点标签为节点对象的某个属性值 | String | -- |
| value | 指定节点value为节点对象的某个属性值 | String | -- |
| children | 指定子树为节点对象的某个属性值 | String | -- |
| disabled | 指定节点是否可用。是否禁用组件，禁用后无法进行交互 | Boolean | -- |
| tip | 指定节点提示信息 | String | -- |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| command | 点击菜单项触发的事件回调 | (value,itemInfo) |
| referenceTrigger | 触发元素以trigger方式触发事件 | ({count}) |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/dropdown.html)

