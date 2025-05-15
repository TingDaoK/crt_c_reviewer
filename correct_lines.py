import asyncio
from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("bragme")


@fast.agent(
    "correct_lines",
    "Given a file name as the input to be submitted to create_pull_request_review, check the `line` field in the input file and verify if the line matches the context of the PR of https://github.com/awslabs/aws-c-s3/pull/517. If not, correct the line to match the context.",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem"],
)
async def main():
    async with fast.run() as agent:
        pull_requests = await agent.correct_lines("/Users/dengket/project/hackthon/fast-agent/new_comments_s3_PR517_saved/input_PR517_comments_naming.json")


if __name__ == "__main__":
    asyncio.run(main())
