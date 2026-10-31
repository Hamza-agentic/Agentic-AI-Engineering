
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def run_semantic_search():
    # Define a collection of text documents
    documents = [
        "Customers can track their active orders using the tracking link sent via email.",
        "Refund and return requests must be submitted within 7 days of delivery.",
        "Our customer support team is available 24/7 to help with payment issues.",
        "You can update or change your shipping address before the order is dispatched.",
    ]

    query = "Where can I register my courses?"

    # Load the sentence transformer model
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    # Generate document and query embeddings
    document_embeddings = model.encode(documents)
    query_embedding = model.encode([query])

    # Calculate similarity scores between query and all documents
    scores = cosine_similarity(query_embedding, document_embeddings)[0]

    # Rank documents by similarity score in descending order
    results = sorted(
        zip(documents, scores),
        key=lambda item: item[1],
        reverse=True,
    )

    print(f"Query: '{query}'\n")
    print("Ranked Search Results:")
    for document, score in results:
        print(f"{score:.4f} -> {document}")

if __name__ == "__main__":
    run_semantic_search()