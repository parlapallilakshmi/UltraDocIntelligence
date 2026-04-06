def calculate_confidence(scores, highlighted_sources):
    # ✅ Convert distance → similarity (0 to 1)
    similarities = [1 / (1 + s) for s in scores]
    similarity_score = sum(similarities) / len(similarities)

    # Coverage score (same as yours)
    highlight_count = sum(s.count("<mark>") for s in highlighted_sources)
    coverage_score = min(1.0, highlight_count / 10)

    # Final weighted score
    confidence = (0.7 * similarity_score) + (0.3 * coverage_score)

    return round(confidence, 2)