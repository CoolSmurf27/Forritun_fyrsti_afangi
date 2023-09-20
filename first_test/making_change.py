price = int(input())
amount_paid = int(input())

    
change = amount_paid - price

   
available_bills = [20, 10, 5, 2, 1]

   
for bill in available_bills:
    while change >= bill:
        print(bill)
        change -= bill
