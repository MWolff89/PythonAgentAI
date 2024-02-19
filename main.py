from dotenv import load_dotenv
# import os
import pandas as pd
from llama_index.query_engine import PandasQueryEngine
from llama_index.agent import OpenAIAgent
from prompts import new_prompt, instruction_str, context, system_prompt
from note_engine import note_engine
from llama_index.tools import QueryEngineTool, ToolMetadata, RetrieverTool
from llama_index.agent import ReActAgent
from llama_index.llms import OpenAI
# from pdf import canada_engine
from website_and_social_links_vector_query import brands_website_and_social_links_engine
from outlets_address_and_operating_hours import outlets_address_and_operating_hours_engine
from fsg_brands import fsg_brands_engine
from general_enquries import general_enquiries_engine
from halal_status import halal_status_engine
from llama_index import download_loader, VectorStoreIndex, SimpleDirectoryReader
import os
from flask import jsonify, request
from fastapi import FastAPI, Body
from pydantic import BaseModel


# AirtableReader = download_loader("AirtableReader")

# reader = AirtableReader("patpIUNoRVFpbaBF9.9f7c8f7dc299e7dab9b7eef0f04da9f417258f2bffb710cee3cc53ad95659087")
# documents = reader.load_data(table_id="tblgz1L63NLlXildM", base_id="appmgtQn7kKi7I7MQ")

# index = VectorStoreIndex.from_documents(documents)

# query_engine = index.as_query_engine()
# result = query_engine.query("halal brands")

# print(documents)
# print(result)


load_dotenv()



population_path = os.path.join("data", "Brands-Halal Status.csv")
population_df = pd.read_csv(population_path)

print(population_df.head())


population_query_engine = PandasQueryEngine(
    df=population_df, verbose=True, instruction_str=instruction_str
)
population_query_engine.update_prompts({"pandas_prompt": new_prompt})

# result = population_query_engine.query("halal brands")

# print(result)

tools = [
    # note_engine,
    QueryEngineTool(
        query_engine=outlets_address_and_operating_hours_engine,
        metadata=ToolMetadata(
            name="outlets_address_and_operating_hours_data",
            description="this gives information about outlet address and operating hours. the brand name and/or location is a MUST as an input."
        ),
    ),
    QueryEngineTool(
        query_engine=brands_website_and_social_links_engine,
        metadata=ToolMetadata(
            name="brands_website_and_social_links",
            description="this gives information about the brands website, facebook, instagram and twitter. this is strictly only for brands  links and not for any other links.",
        ),
    ),
    QueryEngineTool(
        query_engine=general_enquiries_engine,
        metadata=ToolMetadata(
            name="general_enquiries",
            description="this gives information about general enquiries."
        )
    ),
     QueryEngineTool(
        query_engine=population_query_engine,
        metadata=ToolMetadata(
            name="halal_status",
            description="this helps answer questions on which brand(s) are fully halal, not halal or only selected stores within the brand are halal. the input should consist of either a brand name or a choice of [FULLY HALAL, NOT HALAL, SELECTED STORES] OR BOTH. If the user is asking for which brands are halal then we should filter by all that are != NOT HALAL"
        )
    ),
    
]

llm = OpenAI(model="gpt-4-turbo-preview")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=system_prompt)
# agent = OpenAIAgent.from_tools(
#     tools, llm=llm, verbose=True, system_prompt=system_prompt
# )

# while (prompt := input("Enter a prompt (q to quit): ")) != "q":
#     result = agent.chat(prompt)
#     print(result)

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