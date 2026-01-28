from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("pacvue-doc-helper")

@mcp.tool()
def ping() -> str:
    return "pong"

@mcp.tool()
def search_pacvue_docs(query: str) -> str:
    """
    搜索 Pacvue 公司内部前端文档和 Confluence。
    当用户询问关于 Pacvue 组件、业务逻辑或内部规范时调用此工具。
    
    Args:
        query: 用户的搜索关键词，例如 "TablePro 用法" 或 "登录流程"
    """
    try:
        url = "http://127.0.0.1:8000/chat_no_agent"
        response = requests.post(url, json={"query": query})
        # print(response.json(), "response")

        if len(response.json()["results"]) > 0:
            return "\n".join([result["content"] for result in response.json()["results"]])
        else:
            return "未找到相关文档内容。请尝试使用不同的关键词搜索。"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()