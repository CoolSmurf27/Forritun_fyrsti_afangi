#!/usr/bin/env python3

def main():
    # implement your code here

    l1 = []
    l0 = []
   
    last_char = ''
    while True:
        word = input().lower()
        if word == 'x':
            break

        if not last_char or word[0] == last_char:
            l1.append(word)
            last_char = word[-1]
        else:
            l0.append(word)

    print(' '.join(l1))
    print(' '.join(l0))



if __name__ == "__main__":
    main()
