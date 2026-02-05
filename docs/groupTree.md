---
component: groupTree
category: other
tags: [groupTree]
aliases: [groupTree]
version: 1.0.0
description: "PacvueGroupTree组件一般使用"
---

# groupTree 组件文档

> PacvueGroupTree组件一般使用

## 使用示例

### 示例：index

```vue
<template>
  <PacvueGroupTree :data="dataList2" v-model="treeVals" style="width: 300px" @change="grouptreeChange"></PacvueGroupTree>
</template>
<script setup>
  var dataList2 = ref([
    {
      groupName: 'amazon',
      label: 'Contextual',
      value: 'Contextual',
      disableLastPeriods: false,
      hasChildren: false,
      children: []
    },
    {
      groupName: 'amazon',
      label: 'Custom-built',
      value: 'Custom-built',
      disableLastPeriods: false,
      hasChildren: true,
      children: [
        {
          label: 'AMC',
          value: 'AMC'
        },
        {
          label: 'Brand',
          value: 'Brand'
        },
        {
          label: 'OTT remarketing',
          value: 'OTT remarketing'
        },
        {
          label: 'Product',
          value: 'Product'
        }
      ]
    },
    {
      groupName: 'amazon',
      label: 'Demographic',
      value: 'Demographic',
      disableLastPeriods: false,
      hasChildren: true,
      children: [
        {
          label: 'AMC',
          value: 'AMC'
        },
        {
          label: 'Age',
          value: 'Age'
        },
        {
          label: 'Assets',
          value: 'Assets'
        },
        {
          label: 'Education',
          value: 'Education'
        },
        {
          label: 'Gender',
          value: 'Gender'
        },
        {
          label: 'Home Ownership',
          value: 'Home Ownership'
        },
        {
          label: 'Household',
          value: 'Household'
        },
        {
          label: 'Income',
          value: 'Income'
        },
        {
          label: 'Language',
          value: 'Language'
        },
        {
          label: 'Occupation',
          value: 'Occupation'
        },
        {
          label: 'Relationship',
          value: 'Relationship'
        }
      ]
    },
    {
      groupName: 'amazon',
      label: 'Device',
      value: 'Device',
      disableLastPeriods: false,
      hasChildren: true,
      children: [
        {
          label: 'IP Carrier',
          value: 'IP Carrier'
        },
        {
          label: 'Mobile Device',
          value: 'Mobile Device'
        },
        {
          label: 'User Agent',
          value: 'User Agent'
        }
      ]
    },
    {
      groupName: 'amazon',
      label: 'In-market',
      value: 'In-market',
      disableLastPeriods: false,
      hasChildren: true,
      children: [
        {
          label: 'Arts & Crafts',
          value: 'Arts & Crafts'
        },
        {
          label: 'Baby Products',
          value: 'Baby Products'
        },
        {
          label: 'Beauty & Personal Care',
          value: 'Beauty & Personal Care'
        },
        {
          label: 'Books & Magazines',
          value: 'Books & Magazines'
        },
        {
          label: 'Business & Industrial',
          value: 'Business & Industrial'
        },
        {
          label: 'Collectibles & Fine Art',
          value: 'Collectibles & Fine Art'
        },
        {
          label: 'Credit & Payment Cards',
          value: 'Credit & Payment Cards'
        },
        {
          label: 'Education',
          value: 'Education'
        },
        {
          label: 'Electronics',
          value: 'Electronics'
        },
        {
          label: 'Entertainment',
          value: 'Entertainment'
        },
        {
          label: 'Fashion',
          value: 'Fashion'
        },
        {
          label: 'Gift Cards',
          value: 'Gift Cards'
        },
        {
          label: 'Home & Garden',
          value: 'Home & Garden'
        },
        {
          label: 'Household & Grocery',
          value: 'Household & Grocery'
        },
        {
          label: 'Music',
          value: 'Music'
        },
        {
          label: 'Pet Supplies',
          value: 'Pet Supplies'
        },
        {
          label: 'Services',
          value: 'Services'
        },
        {
          label: 'Software & Apps',
          value: 'Software & Apps'
        },
        {
          label: 'Sporting Goods',
          value: 'Sporting Goods'
        },
        {
          label: 'Toys & Games',
          value: 'Toys & Games'
        },
        {
          label: 'Vehicles & Automotive',
          value: 'Vehicles & Automotive'
        }
      ]
    },
    {
      groupName: 'amazon',
      label: 'Interest',
      value: 'Interest',
      disableLastPeriods: false,
      hasChildren: true,
      children: [
        {
          label: 'Art & Design',
          value: 'Art & Design'
        },
        {
          label: 'Automotive & Vehicles',
          value: 'Automotive & Vehicles'
        },
        {
          label: 'Beauty & Grooming',
          value: 'Beauty & Grooming'
        },
        {
          label: 'Books',
          value: 'Books'
        },
        {
          label: 'Business & Careers',
          value: 'Business & Careers'
        },
        {
          label: 'Education & Learning',
          value: 'Education & Learning'
        },
        {
          label: 'Entertainment',
          value: 'Entertainment'
        },
        {
          label: 'Events',
          value: 'Events'
        },
        {
          label: 'Food & Drinks',
          value: 'Food & Drinks'
        },
        {
          label: 'Fun & Hobbies',
          value: 'Fun & Hobbies'
        },
        {
          label: 'Health & Wellness',
          value: 'Health & Wellness'
        },
        {
          label: 'History',
          value: 'History'
        },
        {
          label: 'Home & Garden',
          value: 'Home & Garden'
        },
        {
          label: 'News & Periodicals',
          value: 'News & Periodicals'
        },
        {
          label: 'Office & School',
          value: 'Office & School'
        },
        {
          label: 'Outdoors',
          value: 'Outdoors'
        },
        {
          label: 'Pets & Animals',
          value: 'Pets & Animals'
        },
        {
          label: 'Region & Country',
          value: 'Region & Country'
        },
        {
          label: 'Religion & Spirituality',
          value: 'Religion & Spirituality'
        },
        {
          label: 'Science',
          value: 'Science'
        },
        {
          label: 'Social Science',
          value: 'Social Science'
        },
        {
          label: 'Sports & Fitness',
          value: 'Sports & Fitness'
        },
        {
          label: 'Style & Fashion',
          value: 'Style & Fashion'
        },
        {
          label: 'Technology',
          value: 'Technology'
        },
        {
          label: 'Toys & Games',
          value: 'Toys & Games'
        },
        {
          label: 'Travel & Tourism',
          value: 'Travel & Tourism'
        }
      ]
    },
    {
      groupName: 'amazon',
      label: 'Life event',
      value: 'Life event',
      disableLastPeriods: false,
      hasChildren: false,
      children: []
    },
    {
      groupName: 'amazon',
      label: 'Lifestyle',
      value: 'Lifestyle',
      disableLastPeriods: false,
      hasChildren: true,
      children: [
        {
          label: 'Automotive Ownership',
          value: 'Automotive Ownership'
        },
        {
          label: 'Business & Industry',
          value: 'Business & Industry'
        },
        {
          label: 'Characteristics',
          value: 'Characteristics'
        },
        {
          label: 'Conscious Consumption',
          value: 'Conscious Consumption'
        },
        {
          label: 'Entertainment',
          value: 'Entertainment'
        },
        {
          label: 'Family',
          value: 'Family'
        },
        {
          label: 'New to Category',
          value: 'New to Category'
        },
        {
          label: 'Shoppers',
          value: 'Shoppers'
        },
        {
          label: 'Students & Professionals',
          value: 'Students & Professionals'
        },
        {
          label: 'Subscriptions',
          value: 'Subscriptions'
        },
        {
          label: 'Technology',
          value: 'Technology'
        },
        {
          label: 'Telecommunications',
          value: 'Telecommunications'
        },
        {
          label: 'Travel & Commute',
          value: 'Travel & Commute'
        }
      ]
    },
    {
      groupName: 'other',
      label: 'Advertiser audiences',
      value: 'Advertiser audiences',
      disableLastPeriods: false,
      hasChildren: false,
      children: []
    },
    {
      groupName: 'other',
      label: 'Lookalike',
      value: 'Lookalike',
      disableLastPeriods: false,
      hasChildren: false,
      children: []
    }
  ])
  var treeVals = ref(['Custom-built_AMC', 'Custom-built_Brand', 'Custom-built_OTT remarketing'])
  var grouptreeChange = (values, treeValues) => {
    console.log(values, treeValues)
  }
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| data | 显示的列表数据Array<DataConfig> | Array | [] |
| props | 配置选项，具体看下表ProsConfig | Object | { value: 'value', label: 'label', children: 'children' } |
| height | 元素的高度。组件高度，支持像素值或百分比 | String | 300px |
| v-model/modelValue | 绑定选中的值 | Object | -- |
| filterable | 是否有过滤框功能。是否支持筛选/搜索功能 | Boolean | -- |
| showCheckall | 是否显示全选功能 | Boolean | false |
| itemHeight | 显示tree中的每一列的高度 | Number | 48 |
| load | 异步加载子列表的回调函数 | loadNode(item, resolve:Function) | -- |
| isUseVirtualId | 是否使用自动生成的虚拟id作为唯一键 | Boolean | true |
| label | 指定节点标签为节点对象的某个属性值 | String | -- |
| value | 指定节点value为节点对象的某个属性值 | String | -- |
| children | 指定子树为节点对象的某个属性值 | String | -- |
| groupName | 分组名称 | String | -- |
| label | 显示数据节点名称 | String | -- |
| value | 数据的id | String | -- |
| children | 子列表数据 | Array<{label,value}> | [] |
| hasChildren | 异步下载的需要判断是否需要异步加载数据 | Boolean | -- |

