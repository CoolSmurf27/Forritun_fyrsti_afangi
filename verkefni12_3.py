from typing import List

def extract_evens(int_list):
    return [x for x in int_list if x % 2 == 0]

def remove_odds(int_list):
    int_list[:] = [x for x in int_list if x % 2 == 0]

if __name__ == "__main__":

    input_list = [1, 1, 2, 3, 4, 5]

    print("Original list before calling functions:", input_list)

    even_list = extract_evens(input_list)
    print("Resulting list after extracting evens:", even_list)

    print("Original list after extracting evens and before removing odds:", input_list)
   
    remove_odds(input_list)
    print("Original list after removing odds:", input_list)



    