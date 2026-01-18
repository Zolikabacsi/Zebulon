import os
from loguru import logger
from LightAgent import LightAgent, LightSwarm

agent = LightAgent(
        name="Agent A",  # Agent name
        instructions="You are a helpful agent.",  # Role description
        role="Please remember that you are LightAgent, a useful assistant to help users use multiple tools.",  # system role description
        model="gpt-4o-mini",  # Supported models: openai, chatglm, deepseek, qwen, etc. qwen-turbo-2024-11-01 \ step-1-flash
        api_key="your_api_key",  # Replace with your API Key
        base_url="http://your_base_url/v1",  # api url
        debug=True,
        log_level="DEBUG",
        log_file="example.log"
    )


# Simulate historical conversation
history = [
    {"role": "user", "content": "How's the weather today?"},
    {"role": "assistant", "content": "The weather is sunny today, with a temperature around 25 degrees Celsius."},
]


user_id = "test_user_2"
query = "Hello, please summarize the above information"
response = agent.run(query, history=history, stream=True, user_id=user_id)  # Run query using agent
for chunk in response:
    print(chunk, end="\n", flush=True)