#!/usr/bin/env python3

def count_problems(input_str):
    chunks = input_str.split(';')
    total_problems = 0

    for chunk in chunks:
        if '-' in chunk:
            start, end = map(int, chunk.split('-'))
            total_problems += (end - start + 1)
        else:
            total_problems += 1

    return total_problems



