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

pinecone_index = pc.Index("brand-menus")

print(pinecone_index)

vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
# storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
retriever = VectorIndexRetriever(index=index, similarity_top_k=5)

brand_menus_engine = RetrieverQueryEngine(retriever=retriever)
