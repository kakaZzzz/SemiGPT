from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
import json

import os
os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "fe89b1adaaba86f6c8ca6ac3e3524b7c057b915cc2a42c10074f2b0421f7c962"
os.environ["GOOGLE_CSE_ID"] = "05d376f54d3ac45e5"
os.environ["GOOGLE_API_KEY"] = "AIzaSyABII3Xyk0eIqj76ebt_P1Hxr0gL0ABDOU"

llm = OpenAI(temperature=0)

tools = load_tools(["google-search", "llm-math"], llm=llm)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True, return_intermediate_steps=True)

response = agent({"input":"梅西和c罗谁更厉害？"})

# print(response["intermediate_steps"])

print(json.dumps(response, indent=2))


