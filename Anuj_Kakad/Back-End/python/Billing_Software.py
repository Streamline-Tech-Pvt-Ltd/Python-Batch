
products = {
    1: "Greeting Card",
    2: "Teddy Bear",
    3: "Gift Box",
    4: "Chocolate",
    5: "Bouquet"
}

pricing = {
    1: 50,
    2: 350,
    3: 150,
    4: 100,
    5: 250
}

total = 0

print("===== GIFT SHOP BILL =====")
print("Available Products:")

for key, value in products.items():
    print(f"{key}. {value} - ₹{pricing[key]}")

print("\nEnter product numbers to purchase (1-5).")
print("Enter 0 to finish shopping.")

while True:
    choice = int(input("Enter product number: "))

    if choice == 0:
        break

    if choice in products:
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            price = pricing[choice]
            amount = price * quantity
            total += amount

            print(f"{products[choice]} x {quantity} = ₹{amount}")
        else:
            print("Quantity must be greater than zero.")
    else:
        print("Invalid product number!")

print("\n===== FINAL BILL =====")
print(f"Total Amount: ₹{total}")
print("Thank you for shopping!")
