import asyncio
from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("bragme")


@fast.agent(
    "Code_Scanner",
    "You are a C programer and expert. Given a github link to a C file implementation \
        check the file thoroughly for every function for any possible bugs and security issues. Like: buffer overflow, heap use after free and any potential bugs.\
            And then, generate a report with the details of the bugs and security issues you found. \
                Save your report to a file to the same folder with naming like `scan_result_<file_name>.json`, but don't really submit the comments",
    # Name of an MCP Server defined in fastagent.config.yaml
    servers=["github", "filesystem"],
)
async def main():
    # use the --model command line switch or agent arguments to change model
    async with fast.run() as agent:
        await agent.interactive()

if __name__ == "__main__":
    asyncio.run(main())
