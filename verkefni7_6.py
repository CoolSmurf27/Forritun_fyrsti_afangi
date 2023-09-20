def decimal_to_binary(decimal: int) -> str:
    """Converts an integer from decimal to its binary representation."""

    # Fill in the missing code
    if decimal == 0:
        return "0"
    
    binary_str = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        binary_str = str(remainder) + binary_str
    
    return binary_str