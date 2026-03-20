def simple_rag(query):
    knowledge = {
        "refund": "Refund available within 30 days.",
        "password": "Reset password via account settings."
    }

    for key in knowledge:
        if key in query.lower():
            return knowledge[key]

    return "No information found."

if __name__ == "__main__":
    query = input("Ask: ")
    print(simple_rag(query))
