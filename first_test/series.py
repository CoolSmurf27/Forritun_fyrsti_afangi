n = int(input())
   
cumulative_sum = 0
term = 0.5
   
for i in range(1, n + 1):  
    cumulative_sum += term   
    print(cumulative_sum)  
    term /= 2