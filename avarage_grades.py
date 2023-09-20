sum_credit = 0
weighted_sum = 0
highest_grade = -1  

while True:
    grade = float(input())
    
    if grade < 0:
        break
    
    credit = int(input())
    
    weighted_sum += grade * credit
    sum_credit += credit
    
    if grade > highest_grade:
        highest_grade = grade

if sum_credit > 0:
    weighted_average = weighted_sum / sum_credit
    print("Weighted average grade:", round(weighted_average, 2))

if highest_grade >= 0:
    print("Highest grade:", highest_grade)
   


