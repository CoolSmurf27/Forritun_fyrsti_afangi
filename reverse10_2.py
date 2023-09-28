
#!/usr/bin/env python3
def main():
    number_of_outputs = int(input())
    numb = []
    for _ in range(number_of_outputs):
        num = int(input())
        numb.append(num)
    for numb in reversed(numb):
        print(numb)

if __name__ == "__main__":
    main()













