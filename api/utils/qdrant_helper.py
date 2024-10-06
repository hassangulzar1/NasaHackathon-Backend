from qdrant_client import QdrantClient
import os

qdrant_client = QdrantClient(
    url="https://1c567b57-a9a3-4959-95a8-a20ce9b0f0d5.europe-west3-0.gcp.cloud.qdrant.io:6333",
    api_key="ICfCrvnuKA10Swwy7giPRy3P6uQxKDn8dgefeNYpfIuqqV_j4ifE4w",
)

def get_context(query_text):
    # Instead of using sentence-transformers locally, consider using an API
    # for embedding generation or pre-compute embeddings
    # This is a simplified version that just searches based on the query
    search_results = qdrant_client.search(
        collection_name="planets",
        query_vector=[0] * 384,  # Replace with actual embedding
        limit=1
    )
    
    if search_results:
        return search_results[0].payload
    return "No relevant information found."