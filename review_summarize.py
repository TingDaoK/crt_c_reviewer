import asyncio
from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("bragme")


@fast.agent(
    "review_submitter",
    "Given a github pull request, read the input_*_comments*.json from the new_comments_s3_* folder related to the PR and combine them to a single file.\
        Summary the repeated comments.\
        Check the merged comments, and makes sure the lines commented on are valid. Fix it if not. \
        Save the merged comments to the same folder.\
        But don't actually submit the comments to the pull request via create_pull_request_review.",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem"],
)
async def main():
    async with fast.run() as agent:
        await agent.interactive()


if __name__ == "__main__":
    asyncio.run(main())
