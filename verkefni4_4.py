num = int(input()) # Do not change this line


def triangularnumber(i):
    return i * (i + 1) // 2
for i in range(1, num + 1):
    print(triangularnumber(i))

