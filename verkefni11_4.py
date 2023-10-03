
input1 = input().split()

number = [(float(x)) for x in input1]

if len(number) < 3:
    print("At least 3 scores needed!")
else:
    number.sort()
   
    number = number[3:]
    
    total_sum = round(sum(number),1)
    
    print(f"Sum of scores (3 lowest removed): {total_sum}")
        

