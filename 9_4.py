def main():
    file_name = input()
    with open (file_name, 'r') as file:
        for line in file:
            reversed_line = ' '.join([word[::-1] for word in line.split()])
            print(reversed_line)

if __name__ == "__main__":
    main()

    
    
    

