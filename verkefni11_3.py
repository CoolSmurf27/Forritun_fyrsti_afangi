from typing import List, Tuple

def list_to_bool_tuple(a_list: List[str]) -> Tuple[bool]:
    boolean_value = []
    for i in a_list:
        if i.isdigit():
            boolean_value.append(bool(int(i)))
        else:
            boolean_value.append(bool(i))
    boolean_value_tuple = tuple(boolean_value)
    return boolean_value_tuple

