from backend.dataastore.vector_store import similarity_search_with_score

def retrieve_docs(query):
    results = similarity_search_with_score(query,k=5)

    docs = []
    scores = []

    for doc, score in results:
        docs.append(doc)
        scores.append(score)

    return docs, scores