import re

# Function to parse the document collection file
def parse_document_collection(filename):
    documents = []
    current_document = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line == "<END OF DOCUMENT>":
                if current_document:
                    documents.append(' '.join(current_document))
                current_document = []
            else:
                current_document.append(line)
    return documents

# Function to build the word-to-document mapping
def build_word_mapping(documents):
    word_mapping = {}
    for idx, document in enumerate(documents):
        words = re.findall(r'\b\w+\b', document.lower())
        for word in words:
            if word not in word_mapping:
                word_mapping[word] = set()
            word_mapping[word].add(idx)
    return word_mapping

# Function to search for documents based on search terms
def search_documents(word_mapping, search_terms):
    search_terms = search_terms.split()
    search_terms = [term.lower() for term in search_terms]
    
    matching_documents = set()
    for term in search_terms:
        if term in word_mapping:
            if not matching_documents:
                matching_documents = word_mapping[term]
            else:
                matching_documents = matching_documents.intersection(word_mapping[term])

    return sorted(list(matching_documents))

# Main program
if __name__ == "__main__":
    collection_filename = input()
    
    try:
        documents = parse_document_collection(collection_filename)
        word_mapping = build_word_mapping(documents)

        while True:
            action = input()
            if action == "print":
                document_number = int(input())
                if document_number >= 1 and document_number <= len(documents):
                    print(f"Document #{document_number}:")
                    print(documents[document_number - 1])
                else:
                    print("No match")
            elif action == "search":
                search_terms = input()
                matching_documents = search_documents(word_mapping, search_terms)
                if matching_documents:
                    print("Documents matching search:", ' '.join(map(str, matching_documents)))
                else:
                    print("No match")
            elif action == "quit":
                break
    except FileNotFoundError:
        pass
