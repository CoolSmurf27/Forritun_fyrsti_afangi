n = int(input())
a, b, c = 1, 2, 3

if n >= 1:
    print(a)
if n >= 2:
    print(b)

if n >= 3:
    print(c)

for i in range(4, n + 1):
    next_num = a + b + c  
    print(next_num)  
    
    a, b, c = b, c, next_num


