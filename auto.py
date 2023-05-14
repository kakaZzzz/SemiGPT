from langchain.utilities import SerpAPIWrapper
from langchain.agents import Tool
from langchain.tools.file_management.write import WriteFileTool
from langchain.tools.file_management.read import ReadFileTool

import os
os.environ["OPENAI_API_KEY"] = "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"
os.environ["SERPAPI_API_KEY"] = "fe89b1adaaba86f6c8ca6ac3e3524b7c057b915cc2a42c10074f2b0421f7c962"
os.environ["GOOGLE_CSE_ID"] = "05d376f54d3ac45e5"
os.environ["GOOGLE_API_KEY"] = "AIzaSyABII3Xyk0eIqj76ebt_P1Hxr0gL0ABDOU"


search = SerpAPIWrapper()
tools = [
    Tool(
        name = "search",
        func=search.run,
        description="useful for when you need to answer questions about current events. You should ask targeted questions"
    ),
    WriteFileTool(),
    ReadFileTool(),
]

from langchain.vectorstores import FAISS
from langchain.docstore import InMemoryDocstore
from langchain.embeddings import OpenAIEmbeddings

# Define your embedding model
embeddings_model = OpenAIEmbeddings()
# Initialize the vectorstore as empty
import faiss

embedding_size = 1536
index = faiss.IndexFlatL2(embedding_size)
vectorstore = FAISS(embeddings_model.embed_query, index, InMemoryDocstore({}), {})

from langchain.experimental import AutoGPT
from langchain.chat_models import ChatOpenAI

agent = AutoGPT.from_llm_and_tools(
    ai_name="Tom",
    ai_role="Assistant",
    tools=tools,
    llm=ChatOpenAI(temperature=0),
    memory=vectorstore.as_retriever()
)
# Set verbose to be true
agent.chain.verbose = True

agent.run(["write a weather report for SF today"])