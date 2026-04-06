SIMILARITY_THRESHOLD = 0.1

def apply_guardrails(answer, scores):
    if "not found" in answer.lower():
        return answer, False

    avg_similarity = sum(scores) / len(scores)

    if avg_similarity < SIMILARITY_THRESHOLD:
        return "Not found in document.", False

    return answer, True