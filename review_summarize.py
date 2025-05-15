import asyncio
from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("bragme")


@fast.agent(
    "review_submitter",
    "Given a github pull request, read the input_*_comments*.json from the new_comments_s3_* folder related to the PR and combine them to a single file without redundant comments.\
        Check the merged comments, and makes sure the lines commented on are valid. Fix it if not. \
        Then submit the comments to the pull request via create_pull_request_review.",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem"],
)
async def main():
    async with fast.run() as agent:
        pull_requests = await agent.review_submitter("https://github.com/awslabs/aws-c-s3/pull/519")


if __name__ == "__main__":
    asyncio.run(main())
