# Pacvue Doc Helper

Pacvue 内部文档搜索 MCP Server，支持本地 Markdown 文档和 Confluence 文档的语义搜索。

## 目录结构

```
pacvue-doc/
├── server.py          # MCP Server 入口
├── index.py           # FastAPI 文档搜索服务（后端）
├── doc_loader.py      # 文档加载和向量搜索核心
├── confluence_get.py  # Confluence 文档获取
├── constant.py        # 常量配置（Confluence 文件夹 ID）
├── requirements.txt   # Python 依赖
├── .env.example       # 环境变量模板
└── docs/              # 本地 Markdown 文档目录
```

## 安装

### 1. 创建 Python 虚拟环境

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

复制环境变量模板文件：

```bash
copy .env.example .env
```

编辑 `.env` 文件，填入实际的配置值：

```ini
CONFLUENCE_BASE_URL=https://pacvue-enterprise.atlassian.net/
CONFLUENCE_EMAIL=你的邮箱
CONFLUENCE_API_TOKEN=你的API Token
```

> **注意**：`.env.example` 只是模板文件，不会被自动加载。必须创建 `.env` 文件并填入真实值。

**获取 Confluence API Token**：[https://id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens)

## 使用方法

### 步骤 1：启动后端服务

MCP Server 依赖 FastAPI 后端服务，需先启动：

```bash
uvicorn index:app --reload
```

服务启动后运行在 `http://127.0.0.1:8000`

### 步骤 2：在 Cursor 中配置 MCP Server

打开 Cursor 设置，添加 MCP Server 配置：

```json
"Pacvue Doc Helper": {
  "name": "Pacvue Doc Helper",
  "type": "stdio",
  "command": "<你的虚拟环境路径>/python.exe <你的项目路径>/server.py"
}
```

> 将路径替换为实际值，例如：
>
> - 虚拟环境路径：`D:\projects\pacvue-doc\.venv\Scripts`
> - 项目路径：`D:\projects\pacvue-doc`

### 步骤 3：使用

配置完成后，在 Cursor 中直接询问 Pacvue 相关问题：

- "TablePro 组件怎么用？"
- "登录流程是什么？"
- "Pacvue 的表单校验规范"

AI 助手会自动调用 `search_pacvue_docs` 工具搜索文档并返回结果。

## MCP 工具

| 工具名称             | 描述                              |
| -------------------- | --------------------------------- |
| `ping`               | 测试连接，返回 "pong"             |
| `search_pacvue_docs` | 搜索 Pacvue 内部文档和 Confluence |

## 添加文档

### 组件文档

从 Pacvue 组件库生成文档：

1. 克隆组件库代码：

```bash
git clone https://github.com/Pacvue/elementPlus-vue3.git
```

2. 使用 AI 工具（如 Cursor）基于源码生成 Markdown 文档

3. 将生成的 Markdown 文件放入 `docs/` 目录，重启服务后自动加载

### Confluence 文档

在 `constant.py` 中配置 Confluence 文件夹 ID：

```python
confluence_folder_ids = ["2196631", "其他文件夹ID"]
```

服务启动时自动从 Confluence 拉取指定文件夹下的所有文档。

## Cursor Skills 配置（推荐）

在 Cursor 中添加以下 Skill，可以让 AI 助手更智能地调用文档搜索：

```markdown
---
name: pacvue-front-end-doc
description: 当用户询问 Pacvue 内部前端组件、规范或 Confluence 文档时使用。
---

# Pacvue Front-end Knowledge Assistant

## When to use

当用户的问题包含以下关键词或意图时：

- "Pacvue"
- "公司组件" / "业务组件"
- "前端文档" / "Confluence"
- 询问特定内部组件

## Instructions

你是一个专家级的前端助手，但你没有内置公司内部的私有文档数据。你需要通过调用内部搜索 API 来获取准确信息。
当用户询问内部文档时，**必须使用 `search_pacvue_docs` 工具**来获取信息。

## Response Style

- 风格：简洁、专业。
- 格式：如果是组件文档，请使用 Markdown 表格展示 Props，并提供代码示例。
```
