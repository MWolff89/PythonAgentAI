import os
import pandas as pd
from llama_index.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str

population_path = os.path.join("data", "Brands-Halal Status.csv")
population_df = pd.read_csv(population_path)


population_query_engine = PandasQueryEngine(
    df=population_df, verbose=True, instruction_str=instruction_str
)

population_query_engine.update_prompts({"pandas_prompt": new_prompt})
