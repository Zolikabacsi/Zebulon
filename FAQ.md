## Frequently Asked Questions

Here are some questions users might encounter, for reference:

### 1. **What are the advantages of LightAgent compared to other Agent frameworks (e.g., LangChain, LlamaIndex)?**
   - **Answer**: LightAgent's design philosophy is minimalism and efficiency, not relying on complex dependency libraries (like LangChain, LlamaIndex), making it suitable for rapid deployment and flexible expansion. At the same time, LightAgent has built-in memory modules, Tree of Thought, and multi-agent collaboration functions, which can better handle complex tasks. In addition, LightAgent supports multiple large models, and will soon launch streaming API and Agent evaluation functions, further enhancing its flexibility and practicality.

### 2. **Which large models does LightAgent support?**
   - **Answer**: LightAgent is compatible with various large models, including OpenAI, Zhipu ChatGLM, Baichuan Large Model, DeepSeek, and Qwen series large models. Specifically supported models include, but are not limited to: `gpt-3.5-turbo`, `gpt-4`, `gpt-4o`, `gpt-4o-mini`, `DeepSeek-V2.5`, `DeepSeek-V3`, `qwen-plus`, etc. Users can choose the appropriate model for deployment based on their needs.

### 3. **How to customize tools and integrate them into LightAgent?**
   - **Answer**: Users can define a Python function and pass it as a tool through the `tools` parameter. LightAgent supports automated tool generation and flexible expansion. Tools can be any Python function, supporting parameter type annotations and automatic generation of tool descriptions. Specific examples can be found in the tool integration section of the documentation.

### 4. **How does LightAgent's memory module work?**
   - **Answer**: LightAgent has a built-in `mem0` memory module that supports context memory and history management. Through the memory module, the Agent can maintain context consistency in multi-turn conversations. Users can enable the memory function by setting `memory=True` to maintain coherence in multi-turn conversations.

### 5. **What is the role of the Tree of Thought (ToT) function?**
   - **Answer**: The Tree of Thought module supports complex task decomposition and multi-step reasoning. Through the Tree of Thought, the Agent can better handle complex tasks and improve task completion efficiency. Users can enable the Tree of Thought function by setting `tree_of_thought=True` to make the Agent more intelligent when handling complex tasks.

### 6. **Does LightAgent support multi-agent collaboration?**
   - **Answer**: Yes, LightAgent supports Swarm-like multi-agent collaborative work, where multiple Agents can collaborate to complete complex tasks. Users can use the `collaborate` method to enable multiple Agents to work together, thereby improving task processing efficiency.

### 7. **When will the streaming API feature be launched?**
   - **Answer**: The streaming API feature is under development and is expected to be launched by the end of 2024. This feature will support OpenAI streaming API service output, seamlessly integrating with mainstream Chat frameworks, further enhancing the user experience.

### 8. **How to evaluate LightAgent's performance?**
   - **Answer**: We are developing a built-in Agent evaluation tool to facilitate users in evaluating and optimizing Agent performance. This feature is expected to be launched in early 2025. Users can use this tool to quantitatively evaluate the Agent's performance and optimize it accordingly.

### 9. **Is LightAgent open source?**
   - **Answer**: Yes, LightAgent is open source under the Apache 2.0 license. Users can view and contribute code on GitHub. We welcome contributions in any form, including submitting Issues or Pull Requests, to jointly promote the development of LightAgent.

### 10. **How to get technical support or provide feedback?**
   - **Answer**: Users can submit issues through GitHub Issues, or send emails to service@wanxingai.com for technical support. We attach great importance to user feedback and will respond and solve problems as soon as possible.

---

## Other Possible Questions

### 11. **Does LightAgent support local deployment?**
   - **Answer**: Yes, LightAgent supports local deployment. Users can deploy LightAgent in a local environment according to the guidelines in the documentation, and configure and extend it as needed.

### 12. **Does LightAgent support multiple languages?**
   - **Answer**: LightAgent currently mainly supports Chinese and English, but due to its compatibility with multiple large models, users can achieve multi-language processing by choosing models that support multiple languages. We plan to further expand multi-language support in the future.

### 13. **Does LightAgent support custom models?**
   - **Answer**: Yes, LightAgent supports custom models. Users can specify the use of custom models by configuring the `model` parameter, provided that the model complies with LightAgent's interface specifications.

### 14. **Does LightAgent support multi-threading or multi-processing?**
   - **Answer**: Yes, LightAgent supports multi-threading and multi-processing. Users can configure multi-threading or multi-processing during deployment as needed to improve task processing efficiency.

### 15. **Does LightAgent support integration with other systems?**
   - **Answer**: Yes, LightAgent supports integration with other systems. Users can integrate LightAgent into existing systems through API or SDK to achieve intelligent functional expansion.

---

## Summary

As a lightweight, flexible, and powerful proactive Agent framework, LightAgent aims to provide users with efficient and easy-to-use intelligent solutions. Whether it's intelligent customer service, data analysis, or automated tool generation, LightAgent can meet diverse needs. We look forward to working with developers to jointly promote the development of LightAgent and build a more intelligent future.