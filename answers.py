#prompt user for input: price and discount_percent
price = float(input("Enter original price: "))
discount_percent = float(input("Enter discount percentage: "))

#calculate discount and price after discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent/100) * price
        return price - discount_amount
    else:
        return price

final_price = calculate_discount(price, discount_percent)
print(f"Final price: ", final_price)


