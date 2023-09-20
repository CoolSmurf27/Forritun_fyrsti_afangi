num_items = 0
total_price = 0.0
lowest_price = None

    
while True:
        
        price = float(input())
        
        
        if price == 0:
            break

        
        num_items += 1

        
        total_price += price

        
        if lowest_price is None or price < lowest_price:
            lowest_price = price
   
print(f"Number of items: {round(num_items, 1)}")
print(f"Total price: {round(total_price, 1)}")
 
if num_items > 0:
    print(f"Lowest price: {round(lowest_price, 1)}")






