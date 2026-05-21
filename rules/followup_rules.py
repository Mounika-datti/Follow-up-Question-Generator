def apply_rules(evaluation, followup_count):

    confidence = evaluation["confidence"]

    word_count = evaluation["word_count"]

    similarity = evaluation["semantic_similarity"]

    missing_topics = evaluation["missing_topics"]

    # Stop infinite chains
    if followup_count >= 3:
        return "stop"

    # Very poor answer
    if word_count < 4:
        return "clarification"

    # Low semantic relevance
    if similarity < 0.3:
        return "off_topic"

    # Missing concepts
    if len(missing_topics) > 0:
        return "missing_topic"

    # Strong answer
    if confidence > 0.8:
        return "advanced"

    return "general"