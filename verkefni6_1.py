a_str = input()
char_to_count = input()

# Complete the program below

for i, letter in enumerate(a_str):
    if letter == char_to_count:
        print(i)