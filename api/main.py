from fastapi import FastAPI

from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from langchain.experimental import BabyAGI
from langchain.experimental import AutoGPT

from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# api keys
import os
os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "fe89b1adaaba86f6c8ca6ac3e3524b7c057b915cc2a42c10074f2b0421f7c962"
os.environ["GOOGLE_CSE_ID"] = "05d376f54d3ac45e5"
os.environ["GOOGLE_API_KEY"] = "AIzaSyABII3Xyk0eIqj76ebt_P1Hxr0gL0ABDOU"

llm = OpenAI(temperature=0.9)

system_message_prompt = SystemMessagePromptTemplate.from_template("你是一个有用的助手，能帮助我准确得分解任务")

human_message_prompt = HumanMessagePromptTemplate.from_template("""
    我想{goal}，请分步骤告诉我怎么做
""")

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

chain = LLMChain(llm=llm, prompt=chat_prompt)

print(chat_prompt.format_prompt(goal="快速学习英语").to_messages())


app = FastAPI() # 创建API实例

@app.get("/")
async def root():
    res = chain.run()
    return {"message": res}