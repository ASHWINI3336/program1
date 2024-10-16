def suggest_completions(search_history, partial_query):
    # Convert the partial query to lowercase for case-insensitive matching
    partial_query = partial_query.lower()
    
    # Find suggestions that start with the partial query
    suggestions = [item for item in search_history if item.lower().startswith(partial_query)]
    
    return suggestions

def main():
    search_history = [
        "apple",
        "banana",
        "carrot",
        "pear",
        "pineapple",
        "potato",
        "strawberry"
    ]
    
    # Get user input for the partial search query
    partial_query = input("Enter your partial search query: ")
    
    # Get suggestions based on the search history
    suggestions = suggest_completions(search_history, partial_query)
    
    # Output the suggestions
    print("Suggestions:")
    for suggestion in suggestions:
        print(suggestion)

if __name__ == "__main__":
    main()
