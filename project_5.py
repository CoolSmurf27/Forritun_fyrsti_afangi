def collect_digits(a_str):
    digits = ''.join(filter(str.isdigit, a_str))
    return digits


def inverse_case(a_str):
    invert = "".join([char.upper() if char.islower() else char.lower() for char in a_str])
    return invert

def to_hex(an_int):
    if an_int == 0:
        return "0"
    hex = "0123456789ABCDEF"
    result = ""
    while an_int > 0:
        remainder = an_int % 16
        result = hex[remainder] + result
        an_int //= 16
    return result
    
while True:
    function_choice = input()
    
    if function_choice == "q":
        break
    
    input_string = input()
    
    if function_choice == "c":
        result = collect_digits(input_string)
    elif function_choice == "i":
        result = inverse_case(input_string)
    elif function_choice == "h":
        result = to_hex(int(input_string))
    print(result)


























































































