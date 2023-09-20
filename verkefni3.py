stop_range = int(input())
num_divisors = int(input())

for i in range(10, stop_range):
    first_num = i // 10
    second_num = 1 % 10
    if i ==(first_num + second_num)**2:
        print(i)

for i in range(1, stop_range):
    divide = 0
    for k in range(1, 1+i):
        if i % k == 0:
            divide += 1
    if divide == num_divisors:
        print(i)
