name = input()
first_last = name.split(", ")

first_initial = first_last[1][0].upper()

last_name = first_last[0].capitalize()

changed_name = f"{first_initial}. {last_name}"
print(changed_name)