
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
        age_str = input("How old are you? ")
        try:
            age_int = int(age_str)
            if age_int < 0 or age_int > 125:
                print(f"You seriously expect me to believe you are {age_str} years old?")
            else:
                return age_str
        except ValueError:
            print("Please enter an integer.")
if __name__ == "__main__":
    main()
