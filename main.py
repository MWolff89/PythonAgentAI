from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from prompts import system_prompt
from llama_index.agent import ReActAgent
from llama_index.llms import OpenAI
from tools import tools
from llama_index.memory import ChatMemoryBuffer
from typing import Dict

load_dotenv()

llm = OpenAI(model="gpt-4-turbo-preview")
user_memory_buffers: Dict[str, ChatMemoryBuffer] = {}

app = FastAPI()

class Query(BaseModel):
    text: str
    thread_id: str

async def startup_event():
    global base_context
    global initial_prompt
    # Your startup logic here
    initial_prompt = system_prompt  # Load any initial state or configurations here
    base_context = "Starting the agent"  # Setup any necessary base context for your application

async def shutdown_event():
    # Your shutdown logic here
    # This could involve saving state, closing connections, etc.
    print("Application shutdown")

app.add_event_handler("startup", startup_event)
app.add_event_handler("shutdown", shutdown_event)

@app.post("/query")
async def query(query: Query):
    if query.thread_id not in user_memory_buffers:
        user_memory_buffers[query.thread_id] = ChatMemoryBuffer(token_limit=1000, max_tokens=1000, max_turns=10)
    
    user_memory = user_memory_buffers[query.thread_id]
    agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=base_context, memory=user_memory)
    
    result = agent.chat(query.text)
    print(f"Thread: {query.thread_id}, Query: {query.text}, Result: {result}")
    
    return {
        "response": result
    }
