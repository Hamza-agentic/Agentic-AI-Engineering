from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def run_embeddings_demo():
    # Load a pretrained sentence-transformer model
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    # Define sentences to compare
    sentences = [
        "How do I reset my password?",
        "I forgot my password.",
        "The weather is very hot today.",
    ]

    # Generate dense vector embeddings for the sentences
    embeddings = model.encode(sentences)

    # Calculate cosine similarity between related vs unrelated sentences
    password_similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    weather_similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[2]]
    )[0][0]

    print("--- Semantic Similarity Results ---")
    print(f"Sentence 1: '{sentences[0]}'")
    print(f"Sentence 2: '{sentences[1]}'")
    print(f"Password similarity score: {password_similarity:.4f}\n")

    print(f"Sentence 1: '{sentences[0]}'")
    print(f"Sentence 3: '{sentences[2]}'")
    print(f"Weather similarity score: {weather_similarity:.4f}")

if __name__ == "__main__":
    run_embeddings_demo()