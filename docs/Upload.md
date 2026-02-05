---
component: Upload
category: form
tags: [上传, 表单, 文件]
aliases: [Upload, 上传]
version: 1.0.0
description: "基础用法"
---

# Upload 组件文档

> 基础用法

**分类**: form | **标签**: 上传、表单、文件

## 使用示例

### 通过 slot 你可以传入自定义的上传按钮类型和文字提示。 可通过设置 limit 和

```vue
<template>
  <p class="mb-4">default</p>
  <el-row class="mb-4">
    <pacvue-upload
      class="upload-demo"
      style="width: 460px"
      action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
    >
    </pacvue-upload>
  </el-row>
</template>
<script setup></script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### 你可以将看到图片缩略图，以及当前进度和状态

```vue
<template>
  <el-row class="mb-4">
    <pacvue-upload
      v-model:file-list="fileList"
      class="upload-demo"
      style="width: 460px"
      action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
      :on-preview="handlePreview"
      :on-remove="handleRemove"
      list-type="picture-list"
      :auto-upload="true"
      :before-upload="beforeUpload"
      :on-change="onChange"
    ></pacvue-upload>
  </el-row>
</template>

<script setup>
  import { ref } from 'vue'
  import { ElMessage, ElMessageBox } from 'element-plus'
  const fileList = ref([])
  const uploadFileList = ref([]) //上传文件列表
  const handleRemove = (file, uploadFiles) => {
    console.log(file, uploadFiles)
  }

  const handlePreview = (uploadFile) => {
    console.log(uploadFile)
  }
  const onChange = (uploadFile, uploadFiles) => {
    console.log('>>>>onChange', uploadFile, uploadFiles)
    var isExist = uploadFileList.value.find((fileItem) => {
      return fileItem.uid == uploadFile.uid
    })
    if (!isExist) {
      uploadFileList.value.push(uploadFile)
    }
  }
  const beforeUpload = (rawFile) => {
    return rawFile
  }
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### 你可以将看到图片缩略图，以及当前进度和状态

```vue
<template>
  <el-row class="mb-4">
    <pacvue-upload
      v-model:file-list="fileList"
      class="upload-demo"
      style="width: 460px"
      action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
      :on-preview="handlePreview"
      :on-remove="handleRemove"
      list-type="picture-card"
      :auto-upload="true"
      :before-upload="beforeUpload"
      :on-change="onChange"
    ></pacvue-upload>
  </el-row>
</template>

<script setup>
  import { ref } from 'vue'
  import { ElMessage, ElMessageBox } from 'element-plus'
  const fileList = ref([])
  const uploadFileList = ref([]) //上传文件列表
  const handleRemove = (file, uploadFiles) => {
    console.log(file, uploadFiles)
  }

  const handlePreview = (uploadFile) => {
    console.log(uploadFile)
  }
  const onChange = (uploadFile, uploadFiles) => {
    console.log('>>>>onChange', uploadFile, uploadFiles)
    var isExist = uploadFileList.value.find((fileItem) => {
      return fileItem.uid == uploadFile.uid
    })
    if (!isExist) {
      uploadFileList.value.push(uploadFile)
    }
  }
  const beforeUpload = (rawFile) => {
    return rawFile
  }
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### 你可以将文件拖拽到特定区域以进行上传。

```vue
<template>
  <el-row class="mb-4">
    <pacvue-upload
      v-model:file-list="fileList"
      class="upload-demo"
      style="width: 460px"
      action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
      :on-preview="handlePreview"
      :on-remove="handleRemove"
      list-type="picture"
      drag
      :auto-upload="true"
      :before-upload="beforeUpload"
      :on-change="onChange"
    ></pacvue-upload>
  </el-row>
</template>

<script setup>
  import { ref } from 'vue'
  import { ElMessage, ElMessageBox } from 'element-plus'
  const fileList = ref([])
  const uploadFileList = ref([]) //上传文件列表
  const handleRemove = (file, uploadFiles) => {
    console.log(file, uploadFiles)
  }

  const handlePreview = (uploadFile) => {
    console.log(uploadFile)
  }
  const onChange = (uploadFile, uploadFiles) => {
    console.log('>>>>onChange', uploadFile, uploadFiles)
    var isExist = uploadFileList.value.find((fileItem) => {
      return fileItem.uid == uploadFile.uid
    })
    if (!isExist) {
      uploadFileList.value.push(uploadFile)
    }
  }
  const beforeUpload = (rawFile) => {
    return rawFile
  }
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### 你可以配置listType为picture-self来实现单个文件替换上传。

```vue
<template>
  <el-row class="mb-4">
    <pacvue-upload
      v-model:file-list="fileList"
      class="upload-demo"
      style="width: 460px"
      action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
      :on-preview="handlePreview"
      :on-remove="handleRemove"
      list-type="picture"
      drag
      :auto-upload="true"
      :before-upload="beforeUpload"
      :on-change="onChange"
    ></pacvue-upload>
  </el-row>
</template>

<script setup>
  import { ref } from 'vue'
  import { ElMessage, ElMessageBox } from 'element-plus'
  const fileList = ref([])
  const uploadFileList = ref([]) //上传文件列表
  const handleRemove = (file, uploadFiles) => {
    console.log(file, uploadFiles)
  }

  const handlePreview = (uploadFile) => {
    console.log(uploadFile)
  }
  const onChange = (uploadFile, uploadFiles) => {
    console.log('>>>>onChange', uploadFile, uploadFiles)
    var isExist = uploadFileList.value.find((fileItem) => {
      return fileItem.uid == uploadFile.uid
    })
    if (!isExist) {
      uploadFileList.value.push(uploadFile)
    }
  }
  const beforeUpload = (rawFile) => {
    return rawFile
  }
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### 你可以配置listType为picture-self来实现单个文件替换上传。

```vue
<template>
  <el-row class="mb-4">
    <pacvue-upload
      v-model:file-list="fileList"
      class="upload-demo"
      style="width: 460px"
      action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
      :on-preview="handlePreview"
      :on-remove="handleRemove"
      list-type="picture"
      drag
      :auto-upload="true"
      :before-upload="beforeUpload"
      :on-change="onChange"
    ></pacvue-upload>
  </el-row>
</template>

<script setup>
  import { ref } from 'vue'
  import { ElMessage, ElMessageBox } from 'element-plus'
  const fileList = ref([])
  const uploadFileList = ref([]) //上传文件列表
  const handleRemove = (file, uploadFiles) => {
    console.log(file, uploadFiles)
  }

  const handlePreview = (uploadFile) => {
    console.log(uploadFile)
  }
  const onChange = (uploadFile, uploadFiles) => {
    console.log('>>>>onChange', uploadFile, uploadFiles)
    var isExist = uploadFileList.value.find((fileItem) => {
      return fileItem.uid == uploadFile.uid
    })
    if (!isExist) {
      uploadFileList.value.push(uploadFile)
    }
  }
  const beforeUpload = (rawFile) => {
    return rawFile
  }
</script>
<style scoped>
  .mb-4 {
    margin-bottom: 12px;
  }
</style>
```

### 默认使用统一上传路径，若自定义action或者设置auto-upload为false

```vue
<template>
  <el-row class="mb-4">
    <pacvue-upload class="upload-demo" ref="uploadRef" expiration="3d">
    </pacvue-upload>
  </el-row>
</template>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| action | 上传路径 | String | https://file.pacvue.com/upload |
| public | 是否公开 | Boolean | true |
| expiration | 有效期，默认永久，支持3d,7d,1y | String | -- |
| showFileList | 是否显示文件列表 | Boolean | true |
| limit | 限制文件的数量 | Number | 0 |
| listType | 文件列表的类型，可选项"text" \| "picture" \| "picture-card"\|"picture-list"\|"picture-self"\|"picture-custom" | String | text |
| isFileListInner | 是否显示的文件列表展示在上传文件框内部 | Boolean | false |
| isReplace | 是否上传覆盖前一个文件（只作用于limit为1) | Boolean | true |
| useInnerTriggerOpenFile | 是否使用内部的触发图标 | Boolean | false |
| uploadFileSize | 上传文件展示的样式style对象 | Object | {} |
| layout | 布局,取值为vertical \| horizontal，只对listType为picture-custom有效 | String | horizontal |
| rule | 上传文件验证规则 | Function(rawFile, { blob: base64, width, height }) | -- |
| ruleOperationTiming | 上传文件验证规则运行时机 | Array | ['on-change', 'before-upload'] |
| replaceBtnText | Replace按钮文本 | String | Replace |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| beforeUploadStateChange | 上传文件状态变化时触发 | Function({ status: "success" \| "error", message: string }) |
| submit | 手动触发提交 | Function() |
| remove | 手动移除文件。 file 和rawFile 已被合并。 rawFile 将在 v2.2.0 中移除 | (file: UploadFile \| UploadRawFile, rawFile?: UploadRawFile) => void |

## 相关链接

- [Element Plus 文档](https://element-plus.org/zh-CN/component/upload.html)

