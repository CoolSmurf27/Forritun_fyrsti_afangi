
def extract_integers_and_find_missing(input_str: str):
    
    tokens = input_str.split()

    T = []
    A = []
    B = []
    for token in tokens:
        T.append(token)
        try:
            integer_value = int(token)
            A.append(integer_value)
        except ValueError:
            pass
    max_integer = max(A, default=0)
    for i in range(max_integer + 1):
        if i not in A:
            B.append(i)
    return [T, A, B]
input_string = input()
result = extract_integers_and_find_missing(input_string)
for output_list in result:
    print(output_list)
