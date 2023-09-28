#!/usr/bin/env python3


problems = input().split(';')

total_problems = 0


for part in problems:

    if '-' in part:
        start, end = map(int, part.split('-'))
        total_problems += (end - start + 1)
    else:
        total_problems += 1

print(total_problems)




