def extract_first_number_from_string(string_to_find_int):
    num_string = ''
    found = False

    for char in string_to_find_int:
        if char.isdigit():
            found = True
            num_string += char
        elif found:
            break


    if num_string:
        return int(num_string)
    else:
        return -1
        
        
        