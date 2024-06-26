def is_float(string_to_test: str) -> bool:
    """Returns True if the given string is a float, otherwise False."""
    try:
        is_number = float(string_to_test)
        return True
    except ValueError:
        return False
