import asyncio
from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("bragme")


@fast.agent(
    "Reviewer",
    "Given a github pull request, read every file in /Users/dengket/project/hackthon/fast-agent/summarization/ \
        and follow the guidance in /Users/dengket/project/hackthon/fast-agent/summarization/comments_styles.md to be how you will make comments then make your comments as details as you can for each specific lines.\
            Use 8BRIG4RFWU as Knowledge Base ID and aws profile as bedrock, region us-east-1\
            Check the knowledge base for the API used for correctness. \
                check knowledge base for the naming as well. \
                save your comments about the specific line or lines with the number of the lines to a folder naming followed by ./new_comments_<repo>_PR<the PR number> with name related to the Pull request like PR454_Comments_Naming.md. \
                    And then, generates the comments only if needed and keep the positive comments out as the input for create_pull_request_review, \
                        save it to a file to the same folder with naming like `input_PR454_comments_naming.json`, but don't really submit the comments",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem", "bedrock-kb"],
)
async def main():
    # use the --model command line switch or agent arguments to change model
    async with fast.run() as agent:
        await agent.interactive()
        # pull_requests = await agent.parallel("https://github.com/awslabs/aws-c-s3/pull/517")

if __name__ == "__main__":
    asyncio.run(main())
