from langchain_community.embeddings import HuggingFaceEmbeddings

_embedding = None

def get_embedding_model():
    global _embedding

    if _embedding is None:
        _embedding = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

    return _embedding