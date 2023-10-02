# Function to check if it's possible to change a string to float
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Function that opens a file
def open_file(filename):
    try:
        file_object = open(filename, "r")
        return file_object
    except FileNotFoundError:
        return None

def read_file(file_object):
    if file_object is not None:
        lines = [line.strip() for line in file_object.readlines() if is_float(line.strip())]
        return lines
    return []

def main():
    filename = input()
    file_object = open_file(filename)
    
    if file_object is not None:
        lines = read_file(file_object)
        file_object.close()
    
        if not lines:
            print()
        else:
            numbers = [float(line) for line in lines]

            formatted_numbers = []
            for number in numbers:
                formatted_numbers.append(str(round(number, 4)))
            print(" ".join(formatted_numbers))

 
            cumulative_sum = []
            running_sum = 0.0
            for number in numbers:
                running_sum += number
                cumulative_sum.append(str(round(running_sum, 4)))
            print(" ".join(cumulative_sum))

            
            sorted_numbers = sorted(numbers)
            formatted_sorted_numbers = []
            for number in sorted_numbers:
                formatted_sorted_numbers.append(str(round(number, 4)))
            print(" ".join(formatted_sorted_numbers))

           
            n = len(numbers)
            if n % 2 == 0:
                median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
            else:
                median = sorted_numbers[n // 2]
            print(round(median, 4))

if __name__ == "__main__":
    main()

















    


















