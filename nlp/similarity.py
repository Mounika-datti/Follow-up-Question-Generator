from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_similarity(question, answer):

    question_embedding = model.encode([question])

    answer_embedding = model.encode([answer])

    similarity = cosine_similarity(
        question_embedding,
        answer_embedding
    )[0][0]

    return round(float(similarity), 2)