import math
a_str = input() # Do not change this line.
b_str = input() # Do not change this line.
c_str = input() # Do not change this line.
# Fill in the missing code below.

a_int = int(a_str)
b_int = int(b_str)
c_int = int(c_str)

s = (a_int + b_int + c_int) / 2
area = math.sqrt(s * (s - a_int) * (s - b_int) * (s - c_int))
print(area) # Change this line at your own peril.

