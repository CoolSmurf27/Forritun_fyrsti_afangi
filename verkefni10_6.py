#!/usr/bin/env python3



def are_permutation_of_same_digits(m: str, n: str) -> bool:
    
    return sorted(m) == sorted(n)
        
a = input()
b = input()
        
if are_permutation_of_same_digits(a, b):
    print(f"The numbers {a} and {b} are permutations of each other.")
else:
    print(f"The numbers {a} and {b} are not permutations of each other.")

