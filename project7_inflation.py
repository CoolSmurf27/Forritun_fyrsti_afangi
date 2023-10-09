def main():
    file_name = input()
    try:
        with open(file_name, 'r') as file:
            data = [line.strip().split() for line in file]
        print_data(data)
    except FileNotFoundError:
        return None

def print_data(data):
    for insert in data:
        index = float(insert[1].rstrip(')')) 
        print((insert[0], index))


    years = sorted(set(entry[0][:4] for entry in data))
    for year in years:
        year_data = [(entry[0], float(entry[1])) for entry in data if entry[0].startswith(year)]
        first_index = year_data[0][1]
        last_index = year_data[-1][1]
        print((int(year), first_index, last_index))

    for year in years:
        year_data = [(entry[0], float(entry[1])) for entry in data if entry[0].startswith(year)]
        first_index = year_data[0][1]
        last_index = year_data[-1][1]
        inflation = round(((last_index - first_index) / first_index) * 100, 2)
        print((int(year), inflation))

if __name__ == "__main__":
    main()

    

