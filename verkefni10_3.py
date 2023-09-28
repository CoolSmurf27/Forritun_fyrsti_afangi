#!/usr/bin/env python3

def main():
    n, k = map(int, input().split())
    bags = list(map(int, input().split()))

    position = bags.index(k) + 1

    if position == 1:
        print("fyrst")
    elif position == 2:
        print("naestfyrst")
    else:
        print(f"{position} fyrst")
if __name__ == "__main__":
    main()
