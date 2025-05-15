import asyncio
from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("bragme")


@fast.agent(
    "trainer_8",
    "Read every file in /Users/dengket/project/hackthon/fast-agent/summarization/ and learn from the comments and why the comments are made in the way.\
        Summarize it as detail as you can so that next time you will make comments like it. Save your summarization to ./summarization comments_styles.md",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem"],
)
async def main():
    async with fast.run() as agent:
        pull_requests = await agent.trainer_8("fetch")


if __name__ == "__main__":
    asyncio.run(main())
