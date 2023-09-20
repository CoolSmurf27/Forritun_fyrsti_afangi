# Do not change the following 4 lines:
budget = int(input())
project1 = int(input())
project2 = int(input())
project3 = int(input())

project_cost = project1 + project2 + project3

if project_cost > budget:
    print("Budget is insufficient.")
else:
    print("Budget is sufficient.")

