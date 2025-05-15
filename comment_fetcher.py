import asyncio
from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("bragme")


list = [
    "https://github.com/awslabs/aws-c-s3/pull/504",
    "https://github.com/awslabs/aws-c-s3/pull/495",
    "https://github.com/awslabs/aws-c-s3/pull/479",
    "https://github.com/awslabs/aws-c-s3/pull/478",
    "https://github.com/awslabs/aws-c-s3/pull/476",
    "https://github.com/awslabs/aws-c-s3/pull/475",
    "https://github.com/awslabs/aws-c-s3/pull/473",
    "https://github.com/awslabs/aws-c-s3/pull/468",
    "https://github.com/awslabs/aws-c-s3/pull/463",
    "https://github.com/awslabs/aws-c-s3/pull/462",
    "https://github.com/awslabs/aws-c-s3/pull/460",
    "https://github.com/awslabs/aws-c-s3/pull/459",
    "https://github.com/awslabs/aws-c-s3/pull/458",
    "https://github.com/awslabs/aws-c-s3/pull/456",
    "https://github.com/awslabs/aws-c-s3/pull/454",
    "https://github.com/awslabs/aws-c-s3/pull/450",
    "https://github.com/awslabs/aws-c-s3/pull/449",
    "https://github.com/awslabs/aws-c-s3/pull/448",
    "https://github.com/awslabs/aws-c-s3/pull/445",
    "https://github.com/awslabs/aws-c-s3/pull/444"
]


@fast.agent(
    "comment_fetcher",
    "Given a of a github pull request, fetch the review comments on the pull requests and get the comments graebm made and save them into a local file as agent_comments with the Pull request number under raw_comments/ directory.",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem"],
)
async def main():
    # use the --model command line switch or agent arguments to change model
    async with fast.run() as agent:
        for i in list:
            comments = await agent.comment_fetcher(f"{i}")
            # summary = await agent.Summarizer(f"{comments}")
        # # Create an agent with a default name.
        # # Create an agent with the name "greeter"
        # # Send a message to an agent by name using dot notation
        # result = await agent.greeter("Good morning!")
        # # You can call 'send' explicitly
        # result = await agent.greeter.send("Hello!")

        # # If no message is specified, a chat session will open
        # await agent.greeter()
        # await agent.greeter.prompt()                    # that can be made more explicit
        # # and supports setting a default prompt
        # await agent.greeter.prompt(default_prompt="OK")

        # # Dictionary access is supported if preferred
        # await agent["greeter"].send("Good Evening!")


if __name__ == "__main__":
    asyncio.run(main())
