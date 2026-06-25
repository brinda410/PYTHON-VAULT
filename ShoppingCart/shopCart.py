item=input("Enter the item to buy:")
quantity=int(input("Enter the quantity u want to buy: "))
price=float(input("The price of 1 {item} is:"))

total=quantity*price
print(f"The total is:${total}")
print(f"You brought {quantity}x{item} for ${round(total,4)}")