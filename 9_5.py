def main():
    name = get_name()
    age = get_age()
    print(f"Nice to meet you {name}. Congratulations on your {age} years.")

def get_name() -> str:
   while True:
    name = input("What's your name? ")
    if not name.replace(" ", "").isalpha() or not any(char.isalpha() for char in name):
        print("Please enter a valid name.")
    else:
        return name

def get_age() -> str:
    while True:
        try:
            age = int(input("How old are you? "))
            
            if age < 0 or age > 125:
                print(f"You seriously expect me to believe you are {age} years old?")
            else:
                return age
        except ValueError: 
            print("Please enter an integer.")


if __name__ == "__main__":
    main()
