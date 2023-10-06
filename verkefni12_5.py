def main():
    input_list = get_correct_data()
    if input_list:
        print_information(input_list)

def get_correct_data() -> list:
    
    while True:
        input_list = get_data()
        if input_list:
            return input_list
        else:
            print("Incorrect input! Please try again.")

def get_data():
    

    try:
        input_string = input().strip()
        input_list = [int(x) for x in input_string.split(',')]

       
        if all(x > 0 for x in input_list):
            return input_list
        else:
            return None

    except ValueError:
        return None

def is_prime(n: int) -> bool:
    
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False

    return True

def print_information(input_list: list):
    lsorted = sorted(input_list)
    lcomposite = sorted(set(x for x in input_list if not is_prime(x)))
    lminimum_value = min(input_list)
    lmaximum_value = max(input_list)
    laverage_value = round(sum(input_list) / len(input_list), 2)

    print(f"Input list: {input_list}")
    print(f"Sorted list: {lsorted}")
    print(f"Composite list: {lcomposite}")
    print(f"Min: {lminimum_value}, Max: {lmaximum_value}, Average: {laverage_value:.2f}")

if __name__ == "__main__":
    main()
