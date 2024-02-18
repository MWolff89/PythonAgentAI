import os
from llama_index import VectorStoreIndex, SimpleDirectoryReader


path = os.path.join("data", "FSG_Brands.txt")
reader = SimpleDirectoryReader(input_files=[path])

docs = reader.load_data()

# print(f"Loaded {len(docs)} docs")

index = VectorStoreIndex.from_documents(docs, show_progress=True)

fsg_brands_engine = index.as_query_engine()
# result = query_engine.query("Encik tan facebook link")

# print(result)