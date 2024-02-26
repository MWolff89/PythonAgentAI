import os
import pandas as pd
from llama_index.query_engine import PandasQueryEngine
from prompts import brand_claypot_prompt, instruction_str

path = os.path.join("data", "Outlets-Has Claypot Section.csv")
df = pd.read_csv(path)

# print(df.head())


brand_claypot_query_engine = PandasQueryEngine(
    df=df, verbose=True, instruction_str=instruction_str
)

brand_claypot_query_engine.update_prompts({"pandas_prompt": brand_claypot_prompt})
