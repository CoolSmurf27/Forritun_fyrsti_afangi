min_length = 6
max_length = 20
stop = 'q'
password = ''
counter = 0
valid = 0
invalid = 0
while password != stop:
    password = input()
    if password == stop:
        break
    counter += 1

   
    if len(password) < min_length or len(password) > max_length:
        print(f"{password}: Invalid length.")
        invalid += 1
        continue

   
    has_lower = False
    has_upper = False
    has_digit = False

    
    for char in password:
        if char.islower():
            has_lower = True
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_digit = True

    
    if has_lower and has_upper and has_digit:
        print(f"{password}: Valid password of length {len(password)}.")
        valid += 1
    else:
        invalid += 1
        if not has_lower:
            print(f"{password}: Missing lower case letter.")
