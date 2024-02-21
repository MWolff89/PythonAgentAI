import os
import pandas as pd
from llama_index.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str

path = os.path.join("data", "Brands-Halal Status.csv")
df = pd.read_csv(path)


halal_query_engine = PandasQueryEngine(
    df=df, verbose=True, instruction_str=instruction_str
)

halal_query_engine.update_prompts({"pandas_prompt": new_prompt})
