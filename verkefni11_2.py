def list_to_int_tuple(search_list):
    int_elements = []
    
    for element in search_list:
        try:
            int_element = int(element)
            int_elements.append(int_element)
        except ValueError:
            pass
    
    return tuple(int_elements)
    