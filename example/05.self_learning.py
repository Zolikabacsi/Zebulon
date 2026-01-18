import os
from loguru import logger
from LightAgent import LightAgent, LightSwarm


# Or use a custom memory module, here is an example with mem0 https://github.com/mem0ai/mem0/
from mem0 import Memory

class CustomMemory:
    def __init__(self):
        self.memories = []
        os.environ["OPENAI_API_KEY"] = "your_api_key"
        os.environ["OPENAI_API_BASE"] = "http://your_base_url/v1"
        # Initialize Mem0
        config = {
            "version": "v1.1"
        }
# If qdrant is to be used as a vector database to store memories in mem0, change the config to the code below
        # config = {
        #     "vector_store": {
        #         "provider": "qdrant",
        #         "config": {
        #             "host": "localhost",
        #             "port": 6333,
        #         }
        #     },
        #     "version": "v1.1"
        # }
        self.m = Memory.from_config(config_dict=config)

    def store(self, data: str, user_id):
        """Store memory. Developers can modify the internal implementation of the storage method."""
        result = self.m.add(data, user_id=user_id)
        return result

    def retrieve(self, query: str, user_id):
        """Retrieve related memory. Developers can modify the internal implementation of the retrieval method."""
        result = self.m.search(query, user_id=user_id)
        return result


agent = LightAgent(
        name="Agent A",  # Agent name
        instructions="You are a helpful agent.",  # Role description
        role="Please remember that you are LightAgent, a useful assistant to help users use multiple tools.",  # system role description
        model="gpt-4o-mini",  # Supported models: openai, chatglm, deepseek, qwen, etc. qwen-turbo-2024-11-01 \ step-1-flash
        api_key="your_api_key",  # Replace with your API Key
        base_url="http://your_base_url/v1",  # api url
        memory=CustomMemory(),  # Enable memory function
        tree_of_thought=False,  # Enable Tree of Thought
        self_learning=True,  # Enable agent self-learning
        debug=True,
        log_level="DEBUG",
        log_file="example.log"
    )

def run_conversation(query: str, stream=False, max_retry=5, user_id="user1"):
    logger.info(f"\nStarting to think about the question: {query}")
    response = agent.run(query, stream=stream, max_retry=max_retry, user_id=user_id)  # Run query using agent
    # 处理响应
    if stream:
        for chunk in response:
            print(chunk, end="\n", flush=True)
            # content = chunk.choices[0].delta.content or ""
            # print(content, end="", flush=True)
    else:
        logger.info(f"Final Reply: \n{response}")
    return response

# Agent self-learning test 1
logger.info("\n=========== next conversation ===========")
user_id = "test_user_1"
query = "I have a purchase payment that needs to be transferred. What is my approval process?"
run_conversation(query, stream=True, user_id=user_id)
logger.info("\n=========== next conversation ===========")
query = "Please remember: According to the company's new regulations, starting from January 2025, all purchase payments of the company need to be signed by General Manager Ding, who is in charge of procurement, then submitted to the financial manager for approval. After the financial manager's approval, the general manager's approval is also required before the cashier can make the transfer."
run_conversation(query, stream=True, user_id=user_id)

user_id = "test_user_2"
query = "Hello, I have a purchase payment to transfer to the other party. How do I apply for the transfer?"
run_conversation(query, stream=True, user_id=user_id)