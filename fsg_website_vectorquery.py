import os
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.vector_stores import PineconeVectorStore
import pinecone

os.environ["PINECONE_API_KEY"] = "f90cd424-83d7-4ad0-b147-fa4af7d28fee"

api_key = os.environ["PINECONE_API_KEY"]

pinecone.init(
    api_key=api_key,
    environment="us-west-2",
)

pinecone_index = pinecone.Index("fei-siong-group")

print(pinecone_index)

vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
# storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex(vector_store=vector_store)


# fsg_website_path = os.path.join("data", "feisiong-group-1.json")
# fsg_website_reader = SimpleDirectoryReader(input_files=[fsg_website_path])

# fsg_website_documents = fsg_website_reader.load_data()

# # print(f"Loaded {len(fsg_website_documents)} docs")

# fsg_website_index = VectorStoreIndex.from_documents(fsg_website_documents, show_progress=True)

fsg_website_engine = index.as_query_engine()
# result = query_engine.query("Encik tan facebook link")

# print(result)