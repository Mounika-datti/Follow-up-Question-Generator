from nlp.keyword_extractor import extract_keywords
from nlp.similarity import calculate_similarity

def evaluate_answer(question, answer):

    keywords = extract_keywords(question)

    found_keywords = []

    for word in keywords:

        if word.lower() in answer.lower():

            found_keywords.append(word)

    missing_topics = []

    for word in keywords:

        if word not in found_keywords:

            missing_topics.append(word)

    word_count = len(answer.split())

    similarity_score = calculate_similarity(
        question,
        answer
    )

    score = 0

    # Keyword score
    score += len(found_keywords)

    # Length score
    if word_count > 10:
        score += 2

    # Semantic score
    if similarity_score > 0.5:
        score += 3

    confidence = round(score / 10, 2)

    return {
        "score": score,
        "confidence": confidence,
        "keywords_found": found_keywords,
        "missing_topics": missing_topics,
        "word_count": word_count,
        "semantic_similarity": similarity_score
    }