# from dotenv import load_dotenv
# import os
import pandas as pd
from llama_index.query_engine import PandasQueryEngine
from llama_index.agent import OpenAIAgent
from prompts import new_prompt, instruction_str, context, system_prompt
from note_engine import note_engine
from llama_index.tools import QueryEngineTool, ToolMetadata
from llama_index.agent import ReActAgent
from llama_index.llms import OpenAI
# from pdf import canada_engine
from fsg_website_vectorquery import fsg_website_engine
from fsg_brands import fsg_brands_engine
from llama_index import download_loader, VectorStoreIndex, SimpleDirectoryReader
import os

os.environ["OPENAI_API_KEY"] = "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"


# AirtableReader = download_loader("AirtableReader")

# reader = AirtableReader("patpIUNoRVFpbaBF9.9f7c8f7dc299e7dab9b7eef0f04da9f417258f2bffb710cee3cc53ad95659087")
# documents = reader.load_data(table_id="tblR0EQFKw4NVttP5", base_id="appmgtQn7kKi7I7MQ")

# index = VectorStoreIndex.from_documents(documents)

# query_engine = index.as_query_engine()
# result = query_engine.query("All Encik tan outlets")

# print(result)

# print(documents)

# load_dotenv()



population_path = os.path.join("data", "fsg_outlets.csv")
population_df = pd.read_csv(population_path)


population_query_engine = PandasQueryEngine(
    df=population_df, verbose=True, instruction_str=instruction_str
)
population_query_engine.update_prompts({"pandas_prompt": new_prompt})

# population_query_engine.query("What the opening hours for encik tan's outlets?")

tools = [
    note_engine,
    QueryEngineTool(
        query_engine=population_query_engine,
        metadata=ToolMetadata(
            name="outlets_address_and_operating_hours_data",
            description="this gives information about outlet address and operating hours. the brand name and/or location is a MUST as an input."
        ),
    ),
    QueryEngineTool(
        query_engine=fsg_website_engine,
        metadata=ToolMetadata(
            name="fsg_website_data",
            description="this gives information about job openings.",
        ),
    ),
    QueryEngineTool(
        query_engine=fsg_brands_engine,
        metadata=ToolMetadata(
            name="fsg_brands_data",
            description="this gives detailed information about the brands, including their website, facebook, instagram, and twitter links.",
        ),
    ),
]

llm = OpenAI(model="gpt-4-turbo-preview")
# agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=system_prompt)
agent = OpenAIAgent.from_tools(
    tools, llm=llm, verbose=True, system_prompt=system_prompt
)

while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.chat(prompt)
    print(result)
