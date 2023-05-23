from api.config import load_env

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

import os

# api keys

envs = load_env()

os.environ["OPENAI_API_KEY"] = envs["OPENAI_API_KEY"]
os.environ["SERPAPI_API_KEY"] = "fe89b1adaaba86f6c8ca6ac3e3524b7c057b915cc2a42c10074f2b0421f7c962"
os.environ["GOOGLE_CSE_ID"] = "05d376f54d3ac45e5"
os.environ["GOOGLE_API_KEY"] = "AIzaSyABII3Xyk0eIqj76ebt_P1Hxr0gL0ABDOU"

llm = ChatOpenAI(temperature=0.9, streaming=True)

system_message_prompt = SystemMessagePromptTemplate.from_template("你是一个有用的助手，能帮助我准确得分解任务")

human_message_prompt = HumanMessagePromptTemplate.from_template("""
    分解任务的时候，要用尽量少的步骤，并且只能用以下3种工具：

    1. search
    2. run code
    3. write file
    4. browser website

    我想{goal}，请分步骤告诉我用什么工具和输入内容是什么，并且一定要用以下格式返回给我：
    [tool="工具", input="输入内容"]

""")

chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

chain = LLMChain(llm=llm, prompt=chat_prompt)

# print(chat_prompt.format_prompt(goal="快速学习英语").to_messages())


app = FastAPI() # 创建API实例

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    res = chain.run({
        'goal': '北京今天的天气'
    })
    return {"message": res}