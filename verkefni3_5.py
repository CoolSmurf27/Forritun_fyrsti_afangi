number = int(input()) # Do not change this line
# Fill in the missing code below
if number < 0 or number > 1000000:
    print("verdur ad vera tala milli 0 og 1000000")
else:
    no_7_found_yet = False

    while number > 0:
        tala = number % 10

        if tala == 7:
            no_7_found_yet = True
            break

        number = number // 10

if no_7_found_yet: # Hint: does this variable name suggest anything?
    print("The number contains 7.")
else:
     print("The number does not contain 7.") 