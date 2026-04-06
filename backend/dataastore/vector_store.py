from backend.services.embedding import get_embedding_model
from langchain_community.vectorstores import FAISS



db = None


embedding_model = get_embedding_model()

def create_vector_store(chunks):
    global db
    db = FAISS.from_texts(chunks, embedding_model)


def get_retriever():
    global db
    return db.as_retriever(search_kwargs={"k": 3})

def similarity_search_with_score(query,k=5):
    global db
    return db.similarity_search_with_score(query, k=5)