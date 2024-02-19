import os
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, GPTVectorStoreIndex
from llama_index.vector_stores import PineconeVectorStore
from pinecone import Pinecone
from llama_index.retrievers import VectorIndexRetriever
from llama_index.query_engine import RetrieverQueryEngine
from dotenv import load_dotenv
load_dotenv()



api_key = os.environ["PINECONE_API_KEY"]

pc = Pinecone(api_key=api_key)

pinecone_index = pc.Index("brands-halal-status")

print(pinecone_index)

vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
# storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
retriever = VectorIndexRetriever(index=index, similarity_top_k=5)



# fsg_website_path = os.path.join("data", "feisiong-group-1.json")
# fsg_website_reader = SimpleDirectoryReader(input_files=[fsg_website_path])

# fsg_website_documents = fsg_website_reader.load_data()

# # print(f"Loaded {len(fsg_website_documents)} docs")

# fsg_website_index = VectorStoreIndex.from_documents(fsg_website_documents, show_progress=True)

halal_status_engine = RetrieverQueryEngine(retriever=retriever)
# result = fsg_website_engine.query("Encik tan facebook link")

# print(result)