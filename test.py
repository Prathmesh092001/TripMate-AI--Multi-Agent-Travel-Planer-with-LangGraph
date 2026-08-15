from mcp_client_test import get_all_tools, tavily_mcp_search
import asyncio

if __name__ == "__main__":
    query = "Latest news on AI technology"
    asyncio.run(tavily_mcp_search(query))