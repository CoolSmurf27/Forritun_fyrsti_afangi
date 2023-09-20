x = int(input()) # Do not change this line

if x < 0 or x > 100000:
    print("Talan a ad vera milli 0 og 100000")

xx = x

while xx != 1:
    print(xx)

    if xx % 2 == 0:
        xx = xx // 2
    else:
        xx = 3 * xx + 1
print(xx)