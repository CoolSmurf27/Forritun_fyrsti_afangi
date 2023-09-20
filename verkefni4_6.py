mb_per_month = int(input())

n = int(input())

total_used = 0

for i in range(n):
    notad = int(input())
    total_used += notad

remaining_data = max(0, mb_per_month * (n + 1) - total_used)

print(remaining_data)
