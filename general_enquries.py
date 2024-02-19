import os
from dotenv import load_dotenv
from pinecone import Pinecone
from llama_index import VectorStoreIndex, StorageContext
from llama_index.vector_stores import PineconeVectorStore
from llama_index.retrievers import VectorIndexRetriever
from llama_index.query_engine import RetrieverQueryEngine

load_dotenv()

api_key = os.environ["PINECONE_API_KEY"]

pc = Pinecone(api_key=api_key)

pinecone_index = pc.Index("general-enquiries")

vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
# storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
retriever = VectorIndexRetriever(index=index, similarity_top_k=5)

general_enquiries_engine = RetrieverQueryEngine(retriever=retriever)
