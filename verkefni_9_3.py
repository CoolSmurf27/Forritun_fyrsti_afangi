def main():
    num1_str = input()
    num2_str = input()

    result = divide_safe(num1_str, num2_str)
    
    if result is not None:
        print(result)
    else: 
        print(None)
def divide_safe(num1_str, num2_str):
    
    try:
        num1_str = float(num1_str)
        num2_str = float(num2_str)
        if num2_str == 0:
            return None
        result = num1_str / num2_str
        return round(result, 5)
    
    except (ValueError, ZeroDivisionError):
        return None
     
if __name__ == "__main__":
   main()
