import asyncio
from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("bragme")


@fast.agent(
    "trainer_1",
    "load /Users/dengket/project/hackthon/fast-agent/agent_comments_PR462.txt that is the comments made on github pull request, learn from the comments and why the comments are made in the way. Summarize it as detail as you can so that next time you will make comments like it. Save your summarization to ./summarization with name related to the Pull request like PR454_Comments_Analysis.md",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem"],
)
@fast.agent(
    "trainer_2",
    "load /Users/dengket/project/hackthon/fast-agent/agent_comments_PR463.txt that is the comments made on github pull request, learn from the comments and why the comments are made in the way. Summarize it as detail as you can so that next time you will make comments like it. Save your summarization to ./summarization with name related to the Pull request like PR454_Comments_Analysis.md",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem"],
)
@fast.agent(
    "trainer_3",
    "load /Users/dengket/project/hackthon/fast-agent/agent_comments_PR468.txt that is the comments made on github pull request, learn from the comments and why the comments are made in the way. Summarize it as detail as you can so that next time you will make comments like it. Save your summarization to ./summarization with name related to the Pull request like PR454_Comments_Analysis.md",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem"],
)
@fast.agent(
    "trainer_4",
    "load /Users/dengket/project/hackthon/fast-agent/agent_comments_PR473.txt that is the comments made on github pull request, learn from the comments and why the comments are made in the way. Summarize it as detail as you can so that next time you will make comments like it. Save your summarization to ./summarization with name related to the Pull request like PR454_Comments_Analysis.md",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem"],
)
@fast.agent(
    "trainer_5",
    "load /Users/dengket/project/hackthon/fast-agent/agent_comments_PR475.txt that is the comments made on github pull request, learn from the comments and why the comments are made in the way. Summarize it as detail as you can so that next time you will make comments like it. Save your summarization to ./summarization with name related to the Pull request like PR454_Comments_Analysis.md",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem"],
)
@fast.agent(
    "trainer_6",
    "load /Users/dengket/project/hackthon/fast-agent/agent_comments_PR476.txt that is the comments made on github pull request, learn from the comments and why the comments are made in the way. Summarize it as detail as you can so that next time you will make comments like it. Save your summarization to ./summarization with name related to the Pull request like PR454_Comments_Analysis.md",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem"],
)
@fast.agent(
    "trainer_7",
    "load /Users/dengket/project/hackthon/fast-agent/agent_comments_PR478.txt that is the comments made on github pull request, learn from the comments and why the comments are made in the way. Summarize it as detail as you can so that next time you will make comments like it. Save your summarization to ./summarization with name related to the Pull request like PR454_Comments_Analysis.md",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem"],
)
@fast.agent(
    "trainer_8",
    "load /Users/dengket/project/hackthon/fast-agent/agent_comments_PR479.txt that is the comments made on github pull request, learn from the comments and why the comments are made in the way. Summarize it as detail as you can so that next time you will make comments like it. Save your summarization to ./summarization with name related to the Pull request like PR454_Comments_Analysis.md",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem"],
)
# @fast.chain(
#     name="chain",                          # name of the chain
#     # list of agents in execution order
#     sequence=["PullRequestFetcher", "ListToURLs", "comment_fetcher"],
#     # instruction to describe the chain for other workflows
#     instruction="use /Users/dengket/project/hackthon as the local directory to save the comments",
#     # whether to accumulate messages through the chain
#     cumulative=False
# )
@fast.agent(
    "aggregator",
    "Summarize it and save it to a file called test_summary.md.",
    servers=["github", "filesystem"],
)
@fast.parallel(
    name="parallel",                       # name of the parallel workflow
    # list of agents to run in parallel
    fan_out=["trainer_1", "trainer_2", "trainer_3", "trainer_4",
             "trainer_5", "trainer_6", "trainer_7", "trainer_8"],
    # instruction to describe the parallel for other workflows
    include_request=True,                  # include original request in fan-in message
)
async def main():
    async with fast.run() as agent:
        pull_requests = await agent.parallel("fetch")


if __name__ == "__main__":
    asyncio.run(main())
