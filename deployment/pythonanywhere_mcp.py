import os
import requests
from mcp.server import Server
import mcp.server.stdio
import mcp.types as types

DEPLOY_WEBHOOK_URL = "https://8210232126.pythonanywhere.com/deploy/"
DEPLOY_TOKEN = "X7k9pQ2mR4vL8nJ3wT6yB5eA1cD9fG0h"

async def main():
    server = Server("pythonanywhere-deploy")

    @server.list_tools()
    async def handle_list_tools() -> list[types.Tool]:
        return [
            types.Tool(
                name="deploy_to_pythonanywhere",
                description="触发 PythonAnywhere 部署：拉取最新代码、运行迁移并重载网站",
                inputSchema={"type": "object", "properties": {}},
            )
        ]

    @server.call_tool()
    async def handle_call_tool(name: str, arguments: dict) -> list[types.TextContent]:
        if name != "deploy_to_pythonanywhere":
            raise ValueError(f"Unknown tool: {name}")

        headers = {"Authorization": f"Token {DEPLOY_TOKEN}"}
        try:
            response = requests.post(DEPLOY_WEBHOOK_URL, headers=headers, timeout=60)
            response.raise_for_status()
            result = response.json()
            return [types.TextContent(type="text", text=f"✅ 部署成功: {result}")]
        except Exception as e:
            return [types.TextContent(type="text", text=f"❌ 部署失败: {str(e)}")]

    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())