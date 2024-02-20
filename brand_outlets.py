import os
import pandas as pd
from llama_index.query_engine import PandasQueryEngine
from prompts import brand_outlets_prompt, instruction_str

path = os.path.join("data", "Outlets-FSG_Outlets (1).csv")
df = pd.read_csv(path)

# print(df.head())


brand_outlets_query_engine = PandasQueryEngine(
    df=df, verbose=True, instruction_str=instruction_str
)

brand_outlets_query_engine.update_prompts({"pandas_prompt": brand_outlets_prompt})
