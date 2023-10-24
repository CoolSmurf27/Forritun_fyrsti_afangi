import string


def clean_and_tokenize(filename):
    with open(filename, 'r') as file:
        text = file.read()
        
        words = {word.strip(string.punctuation) for word in text.split()}
        return words


file1 = input()
file2 = input()


words1 = clean_and_tokenize(file1)
words2 = clean_and_tokenize(file2)


def print_words(words, title):
    n = len(words)
    if n > 0:
        print(title)
        print("These words are as follows:")
        sorted_words = sorted(words)
        if n > 1:
            words_str = ", ".join(sorted_words[:-1]) + " and " + sorted_words[-1] + "."
            print(words_str)
        else:
            words_str = sorted_words[0] + "."
            print(words_str)
        


common_words = words1 & words2
print_words(common_words, f"The two files have {len(common_words)} words in common.")


unique_to_file1 = words1 - words2
unique_to_file2 = words2 - words1

n2 = len(unique_to_file1) + len(unique_to_file2)
print_words(unique_to_file1 | unique_to_file2, f"There are {n2} words that are only in either file but not both.")

n3 = len(unique_to_file1)
print_words(unique_to_file1, f"There are {n3} words that only appear in the first file.")

