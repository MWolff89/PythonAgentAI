from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from prompts import system_prompt
from llama_index.agent import ReActAgent, OpenAIAgent
from llama_index.llms import OpenAI
from tools import tools
from tesa_tools import tesa_tools
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

# Ask for user input while the application is running and input is not 'q'
# while True:
#     user_input = input("Enter a query: ")
#     if user_input == "q":
#         break
#     else:
#         thread_id = 'xxx'
#         if thread_id not in user_memory_buffers:
#             user_memory_buffers[thread_id] = ChatMemoryBuffer(token_limit=128000, max_tokens=128000, max_turns=20)
        
#         user_memory = user_memory_buffers[thread_id]
#         agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=system_prompt, memory=user_memory)

#         result = agent.chat(user_input)
#         print(f"Thread: {thread_id}, Query: {user_input}, Result: {result}")
        


@app.post("/query")
async def query(query: Query):
    if query.thread_id not in user_memory_buffers:
        user_memory_buffers[query.thread_id] = ChatMemoryBuffer(token_limit=128000, max_tokens=128000, max_turns=20)
    
    user_memory = user_memory_buffers[query.thread_id]
    agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=system_prompt, memory=user_memory)
    
    result = agent.chat(query.text)
    print(f"Thread: {query.thread_id}, Query: {query.text}, Result: {result}")
    
    return {
        "response": result
    }

# @app.post("/tesa-query")
# async def tesa_query(query: Query):
#     if query.thread_id not in tesa_memory_buffers:
#         tesa_memory_buffers[query.thread_id] = ChatMemoryBuffer(
#             token_limit=128000, max_tokens=128000, max_turns=20
#         )
    
#     user_memory = tesa_memory_buffers[query.thread_id]
#     agent = OpenAIAgent.from_tools(tesa_tools, llm=llm, verbose=True, context=tesa_system_prompt, memory=user_memory)
    
#     result = agent.chat(query.text)
#     print(f"Thread: {query.thread_id}, Query: {query.text}, Result: {result}")
    
#     return {
#         "response": result
#     }