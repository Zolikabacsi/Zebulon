import os
import time

from LightAgent import LightAgent
from browser_use import Agent
from langchain_openai import ChatOpenAI


os.environ["OPENAI_API_KEY"] = "<your_api_key>"
os.environ["OPENAI_BASE_URL"] = "http://<your_base_url>/v1"


async def fetch_data_with_browser(task_description: str) -> str:
    """
    Fetch data using a browser for tasks that cannot be directly accessed by other tools.
    """
    time_start = time.time()
    llm = ChatOpenAI(model='gpt-4.1-mini')
    agent = Agent(
        task=task_description,
        llm=llm,
        use_vision=False
    )
    result = await agent.run()
    time_end = time.time()
    print("\n======== Task Execution Time ========")
    print("Time taken:", int(time_end - time_start), "seconds")
    print("\n======== Task Result ========")
    print(result.final_result())
    return result.final_result()


# Define tool information within the function
fetch_data_with_browser.tool_info = {
    "tool_name": "browser_data_fetcher",
    "tool_title": "Use Browser",
    "tool_description": "For tasks that cannot be directly accessed by other tools, use a browser to obtain text data or file URLs.",
    "tool_params": [
        {"name": "task_description", "description": "Description of the task to be executed by the browser.", "type": "string", "required": True}
    ]
}

tools = [fetch_data_with_browser]

# Initialize Agent
agent = LightAgent(model="gpt-4.1-mini", api_key="<your_api_key>",
                   base_url="http://<your_base_url>/v1",
                   tools=tools,
                   debug=True,
                   log_level="debug",
                   log_file="example.log")

# Run Agent
response = agent.run("Please search the weather in Shanghai.", stream=True)
full_response = ''
for chunk in response:
    print(chunk, end="\n", flush=True)
