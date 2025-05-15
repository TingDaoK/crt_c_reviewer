import asyncio
from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("bragme")


@fast.agent(
    "Reviewer",
    "Given a github pull request. \
        The code in the pull request is very related to the knowledge base, fetch the details of the code base you want to learn about the code from the knowledge base. \
            Use 8BRIG4RFWU as Knowledge Base ID and aws profile as bedrock, region us-east-1\
                But if the code is just added by the pull request, then the knowledge base will not help \
        and follow the guidance in /Users/dengket/project/hackthon/fast-agent/crt_c_reviewer/summarization/comments_styles.md to be how you will make comments then make your comments \
            as details as you can for each specific lines on the pull request, \
                save your comments about the specific line or lines with the number of the lines to a folder naming followed by ./new_comments_s3_PR<the PR number> with name related to the Pull request like PR454_Comments.md. \
                    And then, generates the comments only if needed and keep the positive comments out for the specific line or lines as the input for create_pull_request_review, \
                        save it to a file to the same folder with naming like `input_PR454_comments.json`, but don't really submit the comments",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem", "bedrock-kb"],
)
@fast.agent(
    "Reviewer_naming",
    "Given a github pull request. \
        The code in the pull request is very related to the knowledge base, fetch the details of the code base you want to learn about the code from the knowledge base. \
            Use 8BRIG4RFWU as Knowledge Base ID and aws profile as bedrock, region us-east-1\
                But if the code is just added by the pull request, then the knowledge base will not help \
        and follow the guidance in /Users/dengket/project/hackthon/fast-agent/crt_c_reviewer/summarization/comments_styles.md to be how you will make comments then make your comments \
            as details as you can for each specific lines about the function and variable naming on the pull request, \
                save your comments about the specific line or lines with the number of the lines to a folder naming followed by ./new_comments_s3_PR<the PR number> with name related to the Pull request like PR454_Comments_Naming.md. \
                    And then, generates the comments only if needed and keep the positive comments out for the specific line or lines as the input for create_pull_request_review, \
                        save it to a file to the same folder with naming like `input_PR454_comments_naming.json`, but don't really submit the comments",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem", "bedrock-kb"],
)
@fast.agent(
    "Reviewer_documentation",
    "Given a github pull request. \
        The code in the pull request is very related to the knowledge base, fetch the details of the code base you want to learn about the code from the knowledge base. \
            Use 8BRIG4RFWU as Knowledge Base ID and aws profile as bedrock, region us-east-1\
                But if the code is just added by the pull request, then the knowledge base will not help \
        and follow the guidance in /Users/dengket/project/hackthon/fast-agent/crt_c_reviewer/summarization/comments_styles.md to be how you will make comments then make your comments \
            as details as you can for each specific lines about the documentation on the pull request, \
                save your comments about the specific line or lines with the number of the lines to a folder naming followed by ./new_comments_s3_PR<the PR number> with name related to the Pull request like PR454_Comments_Docs.md. \
                    And then, generates the comments only if needed and keep the positive comments out for the specific line or lines as the input for create_pull_request_review, \
                        save it to a file to the same folder with naming like `input_PR454_comments_docs.json`, but don't really submit the comments",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem", "bedrock-kb"],
)
@fast.agent(
    "Reviewer_API_usage",
    "Given a github pull request. \
        The code in the pull request is very related to the knowledge base, fetch the details of the code base you want to learn about the code from the knowledge base. \
            Use 8BRIG4RFWU as Knowledge Base ID and aws profile as bedrock, region us-east-1\
                But if the code is just added by the pull request, then the knowledge base will not help \
        and follow the guidance in /Users/dengket/project/hackthon/fast-agent/crt_c_reviewer/summarization/comments_styles.md to be how you will make comments then make your comments \
            as details as you can for each specific lines about the usage of API on the pull request, \
                save your comments about the specific line or lines with the number of the lines to a folder naming followed by ./new_comments_s3_PR<the PR number> with name related to the Pull request like PR454_Comments_Impl.md. \
                    And then, generates the comments only if needed and keep the positive comments out for the specific line or lines as the input for create_pull_request_review, \
                        save it to a file to the same folder with naming like `input_PR454_comments_API_usage.json`, but don't really submit the comments",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem", "bedrock-kb"],
)
@fast.agent(
    "Reviewer_Error_handling",
    "Given a github pull request. \
        The code in the pull request is very related to the knowledge base, fetch the details of the code base you want to learn about the code from the knowledge base. \
            Use 8BRIG4RFWU as Knowledge Base ID and aws profile as bedrock, region us-east-1\
                But if the code is just added by the pull request, then the knowledge base will not help \
        and follow the guidance in /Users/dengket/project/hackthon/fast-agent/crt_c_reviewer/summarization/comments_styles.md to be how you will make comments then make your comments \
            as details as you can for each specific lines about the error handling on the pull request, \
                save your comments about the specific line or lines with the number of the lines to a folder naming followed by ./new_comments_s3_PR<the PR number> with name related to the Pull request like PR454_Comments_Impl.md. \
                    And then, generates the comments only if needed and keep the positive comments out for the specific line or lines as the input for create_pull_request_review, \
                        save it to a file to the same folder with naming like `input_PR454_comments_Error_handling.json`, but don't really submit the comments",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem", "bedrock-kb"],
)
@fast.agent(
    "Reviewer_memory_management",
    "Given a github pull request. \
        The code in the pull request is very related to the knowledge base, fetch the details of the code base you want to learn about the code from the knowledge base. \
            Use 8BRIG4RFWU as Knowledge Base ID and aws profile as bedrock, region us-east-1\
                But if the code is just added by the pull request, then the knowledge base will not help \
        and follow the guidance in /Users/dengket/project/hackthon/fast-agent/crt_c_reviewer/summarization/comments_styles.md to be how you will make comments then make your comments \
            as details as you can for each specific lines about the memory management, check for memory leak and memory safety on the pull request, \
                save your comments about the specific line or lines with the number of the lines to a folder naming followed by ./new_comments_s3_PR<the PR number> with name related to the Pull request like PR454_Comments_Impl.md. \
                    And then, generates the comments only if needed and keep the positive comments out for the specific line or lines as the input for create_pull_request_review, \
                        save it to a file to the same folder with naming like `input_PR454_comments_memory_management.json`, but don't really submit the comments",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem", "bedrock-kb"],
)
@fast.agent(
    "Reviewer_code_simplicity",
    "Given a github pull request. \
        The code in the pull request is very related to the knowledge base, fetch the details of the code base you want to learn about the code from the knowledge base. \
            Use 8BRIG4RFWU as Knowledge Base ID and aws profile as bedrock, region us-east-1\
                But if the code is just added by the pull request, then the knowledge base will not help \
        and follow the guidance in /Users/dengket/project/hackthon/fast-agent/crt_c_reviewer/summarization/comments_styles.md to be how you will make comments then make your comments \
            as details as you can for each specific lines about the code simplicity on the pull request and suggest on how you can simplify the code without changing the functionality, \
                save your comments about the specific line or lines with the number of the lines to a folder naming followed by ./new_comments_s3_PR<the PR number> with name related to the Pull request like PR454_Comments_Impl.md. \
                    And then, generates the comments only if needed and keep the positive comments out for the specific line or lines as the input for create_pull_request_review, \
                        save it to a file to the same folder with naming like `input_PR454_comments_code_simplicity.json`, but don't really submit the comments",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem", "bedrock-kb"],
)
@fast.parallel(
    name="parallel",                       # name of the parallel workflow
    # list of agents to run in parallel
    fan_out=["Reviewer_naming",
             "Reviewer_documentation", "Reviewer_API_usage", "Reviewer_Error_handling", "Reviewer_memory_management", "Reviewer_code_simplicity"],
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
