
# Simulated retrieval step (can be replaced with FAISS / vector DB)
def simple_rag(query: str) -> str:
    knowledge_base = {
        "refund": "Refund requests are supported within 30 days of purchase.",
        "password": "Users can reset passwords from the account settings page.",
        "delivery": "Delivery status can be tracked from the orders section."
    }

    query_lower = query.lower()
    for key, value in knowledge_base.items():
        if key in query_lower:
            return value

    return "No relevant information found in the knowledge base."


if __name__ == "__main__":
    user_query = input("Ask a question: ")
    response = simple_rag(user_query)
    print(response)
