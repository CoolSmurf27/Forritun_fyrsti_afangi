
def tokenize_line(line):
    words = []
    tokens = []
    parts = line.split()
    for part in parts:
        word = part.rstrip(string.punctuation)
        token = part[len(word):]
        words.append(word)
        if token:
            tokens.append(token)
    return words, tokens

def tokens(input_file):
    try:
        with open(input_file, 'r') as file:
            lines_in_file = file.readlines()
    except FileNotFoundError:
        return None
    
    all_words = []
    all_tokens = []

    for line in lines_in_file:
        line = line.strip()
        if not line:
            continue
        words, tokens = tokenize_line(line)
        all_words.extend(words)
        all_tokens.extend(tokens)

    return all_words, all_tokens
    
def main():
    input_file = input()
    result = tokens(input_file)
    if result:
        words, tokens = result
        word_count = len(words)
        token_count = len(tokens)
        print(word_count)
        for word in words:
            print(word)
        print(token_count)
        for token in tokens:
            print(token)
    

if __name__ == "__main__":
    main()



