from dotenv import load_dotenv
from prompts import system_prompt
from llama_index.agent import ReActAgent
from llama_index.llms import OpenAI
from tools import tools
from fastapi import FastAPI, Body
from pydantic import BaseModel

load_dotenv()

llm = OpenAI(model="gpt-4-turbo-preview")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=system_prompt)
# agent = OpenAIAgent.from_tools(
#     tools, llm=llm, verbose=True, system_prompt=system_prompt
# )

class Query(BaseModel):
    text: str

app = FastAPI()

@app.post("/query")
def query(query: Query):
    print(query)
    result = agent.chat(query.text)
    print(result)
    return {
        "response": result
    }