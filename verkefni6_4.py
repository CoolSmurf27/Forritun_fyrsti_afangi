a_str = input()

# Complete the program below
invert = "".join([char.upper() if char.islower() else char.lower() for char in a_str])
print(invert)

