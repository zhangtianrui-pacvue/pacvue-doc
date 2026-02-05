# Pacvue Doc Helper

Pacvue 内部文档搜索 MCP Server，支持本地 Markdown 文档和 Confluence 文档的语义搜索。

## 目录结构

```
pacvue-doc/
├── server.py          # MCP Server 入口
├── index.py           # FastAPI 文档搜索服务（后端）
├── doc_loader.py      # 文档加载和向量搜索核心
├── confluence_get.py  # Confluence 文档获取
├── constant.py        # 常量配置（Confluence 页面 ID）
├── requirements.txt   # Python 依赖
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

### 3. 配置环境变量（可选）

如需拉取 Confluence 文档，配置以下环境变量：

- `CONFLUENCE_TOKEN` - Confluence API Token
  > 获取地址：[https://id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
- `CONFLUENCE_EMAIL` - Confluence 账户邮箱

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
{
  "mcpServers": {
    "pacvue-doc-helper": {
      "command": "python",
      "args": ["<你的项目路径>/server.py"]
    }
  }
}
```

> 将 `<你的项目路径>` 替换为本项目的实际路径，例如 `D:/projects/pacvue-doc`

## MCP 工具

| 工具名称             | 描述                              |
| -------------------- | --------------------------------- |
| `ping`               | 测试连接，返回 "pong"             |
| `search_pacvue_docs` | 搜索 Pacvue 内部文档和 Confluence |

## 添加文档

### 本地文档

将 Markdown 文件放入 `docs/` 目录，重启服务后自动加载。

### Confluence 文档

在 `constant.py` 中配置 Confluence 页面 ID：

```python
online_docs_Ids = ["123456", "789012"]
```

服务启动时自动从 Confluence 拉取。

### 步骤 3：使用

配置完成后，在 Cursor 中直接询问 Pacvue 相关问题：

- "TablePro 组件怎么用？"
- "登录流程是什么？"
- "Pacvue 的表单校验规范"

AI 助手会自动调用 `search_pacvue_docs` 工具搜索文档并返回结果。

## cursor 配置skills(推荐)

```
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
