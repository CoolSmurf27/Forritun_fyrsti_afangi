
numberofinputs = int(input())
chores = set()
filtered_chores = []
for i in range(numberofinputs):
    chore = input().strip()
    if chore not in chores:
        chores.add(chore)
        filtered_chores.append(chore)
for chore in filtered_chores:
    print(chore)

    