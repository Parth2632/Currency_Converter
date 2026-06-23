from langchain_core.tools import tool, InjectedToolArg
# pyrefly: ignore [missing-import]
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from typing import Annotated # Annotated = attach extra info to a type
from langchain_core.messages import HumanMessage
import requests

import os

load_dotenv()

hf_token = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
if not hf_token:
    raise ValueError("Set HF_TOKEN or HUGGINGFACEHUB_ACCESS_TOKEN in your .env file.")

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=hf_token,
)
model = ChatHuggingFace(llm=llm)

@tool 
def get_conversion_factor(base_currency : str, target_currency : str) -> float:
    """Get conversion factor between two currencies"""
    api_key = os.getenv("RATE_EXCHANGE")
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"
    if not url:
        raise ValueError("Set RATE_EXCHANGE in your .env file.")
    response = requests.get(url)
    data = response.json()
    return data
    
print(get_conversion_factor.invoke({"base_currency" : "USD", "target_currency" : "INR"}))

@tool
def convert(base_currency_value : int, conversion_rate : Annotated[float, InjectedToolArg]) -> int:
    """Convert currency"""
    return base_currency_value * conversion_rate
    
#Binding

llm_with_tools = model.bind_tools([get_conversion_factor, convert])
messages = [HumanMessage(content="conversion factor between USD and INR and based on that convert 10 USD to INR")] #added human message
ai_message = llm_with_tools.invoke(messages)
print(ai_message.tool_calls)
messages.append(ai_message)


import json 
for tool_call in ai_message.tool_calls:
    if tool_call["name"] == "get_conversion_factor":
        tool_message1 = get_conversion_factor.invoke(tool_call)
        conversion_rate = json.loads(tool_message1.content)["conversion_rate"] #converting json to python
        messages.append(tool_message1)
    if tool_call["name"] == "convert":
        tool_call['args']['conversion_rate'] = conversion_rate #added one more arg manually
        tool_message2 = convert.invoke(tool_call)
        messages.append(tool_message2)
        final_message = llm_with_tools.invoke(messages)
        print(final_message.content)
        
        