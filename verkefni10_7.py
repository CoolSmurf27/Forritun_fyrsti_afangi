amount = int(input())
og_order = input().split()

for i in range(len(og_order)):
    og_order[i] = int(og_order[i])

og_order.sort()

for i in range(len(og_order)):
    og_order[i] = str(og_order[i])

final_order_str = ""

split_amount = amount / 3

first_split = int(split_amount)
second_split = int(split_amount*2)

final_order_str += " ".join(og_order[first_split:second_split])
final_order_str += " " + " ".join(og_order[0:first_split])
final_order_str += " " + " ".join(og_order[second_split:])

print(final_order_str)