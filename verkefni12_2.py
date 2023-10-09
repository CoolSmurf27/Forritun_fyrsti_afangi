def main():
    with get_file() as file_obj:
        numbers = get_numbers_from_file(file_obj)
        display_numbers(numbers)

def get_file():
    while True:
        file_name = input()
        file = open_file(file_name)
        if file:
            return file

def open_file(filename: str):
    try:
        return open(filename, 'r')
    except FileNotFoundError:
        print(f"{filename} not found! Please try again.")
        return None

def get_numbers_from_file(file) -> list:
    
    numbers = []
    for line in file:
        words = line.split()
        for word in words:
            try:
                num = int(word)
                numbers.append(num)
            except ValueError:
                pass
    return numbers

def display_numbers(numbers):
   
    numbers.sort()
    print(numbers)

if __name__ == "__main__":
    main()



