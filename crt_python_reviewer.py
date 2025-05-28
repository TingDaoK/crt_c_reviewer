import asyncio
from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("bragme")

knowledge_base_id = "HKNW5BLFRA"
profile = "bedrock"
region = "us-east-1"

generic_prompt = f"You are a helpful AI Agent. Use {knowledge_base_id} as Knowledge Base ID and `{profile}` as the profile, region {region}.\
    Given a github pull request. The code in the pull request is very related to the knowledge base, fetch the details of the code base you want to learn about the code from the knowledge base. \
        But if the code is just added by the pull request, then the knowledge base will not help. \
            Follow the guidance in /Users/dengket/project/hackthon/fast-agent/crt_c_reviewer/summarization/comments_styles.md to be how you will make comments then make your comments. \
                Ignore the tests change. \
                Keep all the line information when you retrieve the pull request."


def specific_prompt(specific):
    return f"{generic_prompt} \
        and make your comments as details as you can for each specific lines only about the {specific} on the pull request, \
            save your comments about the specific line or lines with the exact number of the lines of the new code to a folder naming followed by ./new_comments_crt_python_PR<the PR number> with name related to the Pull request like PR454_Comments_{specific}.md. \
                And then, generates the comments only if needed and keep the positive comments out for the specific line or lines as the input for create_pull_request_review, \
                    save it to a file to the same folder with naming like `input_PR454_comments_{specific}.json`, but don't really submit the comments"


@fast.agent(
    "Reviewer_naming",
    specific_prompt("function and variable naming"),
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem", "bedrock-kb"],
)
@fast.agent(
    "Reviewer_documentation",
    specific_prompt("documentation"),
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem", "bedrock-kb"],
)
@fast.agent(
    "Reviewer_API_usage",
    specific_prompt("usage of API"),
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem", "bedrock-kb"],
)
@fast.agent(
    "Reviewer_Error_handling",
    specific_prompt("error handling"),
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem", "bedrock-kb"],
)
@fast.agent(
    "Reviewer_memory_management",
    specific_prompt("memory management"),
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem", "bedrock-kb"],
)
@fast.agent(
    "Reviewer_code_simplicity",
    specific_prompt("code simplicity"),
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem", "bedrock-kb"],
)
@fast.parallel(
    name="implementation",                       # name of the parallel workflow
    # list of agents to run in parallel
    fan_out=["Reviewer_API_usage", "Reviewer_Error_handling",
             "Reviewer_memory_management", "Reviewer_code_simplicity"],
    # instruction to describe the parallel for other workflows
    include_request=True,                  # include original request in fan-in message
)
@fast.parallel(
    name="docs",                       # name of the parallel workflow
    # list of agents to run in parallel
    fan_out=["Reviewer_naming",
             "Reviewer_documentation"],
    # instruction to describe the parallel for other workflows
    include_request=True,                  # include original request in fan-in message
)
async def main():
    # use the --model command line switch or agent arguments to change model
    async with fast.run() as agent:
        await agent.interactive()
        # pull_requests = await agent.parallel("https://github.com/awslabs/aws-c-s3/pull/517")

if __name__ == "__main__":
    asyncio.run(main())
