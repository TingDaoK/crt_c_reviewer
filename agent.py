import asyncio
from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("fast-agent example")


# Define the agent
@fast.agent(instruction="You are a helpful AI Agent. Use 8BRIG4RFWU as Knowledge Base ID and aws profile as bedrock, region us-east-1.", servers=["filesystem", "bedrock-kb", "aws-cli-yolo"])
# @fast.agent(instruction="You are a helpful AI Agent. Use 8BRIG4RFWU as Knowledge Base ID and aws profile as bedrock, region us-east-1.")
async def main():
    # use the --model command line switch or agent arguments to change model
    async with fast.run() as agent:
        await agent.interactive()


if __name__ == "__main__":
    asyncio.run(main())
