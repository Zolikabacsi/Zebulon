# -*- coding: utf-8 -*-
import json
import os
import sys
from LightAgent import LightAgent

# Initialize LightAgent
agent = LightAgent(
    name="Agent A",  # Agent name
    instructions="You are a helpful agent.",  # Role description
    role="Please remember that you are a tool generator; your task is to automatically generate corresponding tool code based on the text description provided by the user and save it to the specified directory. Please ensure that the generated code is accurate, usable, and meets the user's needs.",  # Tool generator's role description
    model="gpt-4.1",  # Replace with your model. Supported models: openai, chatglm, deepseek, qwen, etc.
    api_key="your_api_key",  # Replace with your API Key
    base_url="your_base_url",  # Replace with your API URL
)

# Sample text description
text = """
### Weather Query Tool Function Documentation

#### Function Description
This function is used to obtain real-time weather information for a specified city by calling a public weather API (wttr.in) and returning formatted weather data.

#### Parameter Description
- **city_name** (str):
    The name of the city to query (must be a string type)
  Example: `"Beijing"`, `"New York"`

#### Return Value
- The return type is a string, with the following two possibilities:
  1. On success: Returns a JSON formatted string containing weather data
  2. On failure: Returns an error message string (including exception stack trace)

#### Data Content
The successfully returned weather data includes the following fields:
- `temp_C`: Current temperature (Celsius)
- `FeelsLikeC`: Feels like temperature (Celsius)
- `humidity`: Humidity percentage
- `weatherDesc`: Weather phenomenon description
- `observation_time`: Data observation time

#### Exception Handling
1. **Input Validation**：
   - If `city_name` is not a string type, a `TypeError` is thrown

2. **API Request Exception**：
   - When network requests fail or data parsing is abnormal, all errors are caught and a string containing error details is returned

#### Implementation Details
1. **API Endpoint**：
   ```python
   f"https://wttr.in/{city_name}?format=j1"
   ```
   - Use `j1` format to get JSON data

2. **Data Filtering**：
   ```python
   key_selection = {
       "current_condition": ["temp_C", "FeelsLikeC", ...]
   }
   ```
   - Only extract key fields from the complete data returned by the API

3. **Error Handling**：
   ```python
   except:
       ret = "Error encountered while fetching weather data!\n" + traceback.format_exc()
   ```
   - Retain complete error stack information for easy debugging

"""

# Build the path to the tools directory
tools_directory = os.path.join("tools")

# Create tools directory if it does not exist
if not os.path.exists(tools_directory):
    os.makedirs(tools_directory)

print(f"Tools directory has been created: {tools_directory}")

# Use agent to generate tool code
agent.create_tool(text, tools_directory=tools_directory)