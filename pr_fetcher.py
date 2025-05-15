import asyncio
from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("bragme")


@fast.agent(
    "PullRequestFetcher",
    "Look into aws-c-s3, fetch the last 20 Pull Requests graebm made comments on and save the link to PR locally as prs-to-train.md .",
    servers=["github", "filesystem"],
)
async def main():
    async with fast.run() as agent:
        pull_requests = await agent.PullRequestFetcher("fetch")


if __name__ == "__main__":
    asyncio.run(main())
