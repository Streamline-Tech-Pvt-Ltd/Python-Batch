#  electronics store billing software....

#items:

items ={
    1:"TV",
    2:"Washing Machine",
    3:"Fridge",
    4:"Fan",
    5:"Home theaters",
    6:"AC",
    7:"Floor mill",
    8:"Heater",
    9:"cooler",
    10:"Speakers"
    }

#prices:
price ={
    1:15000,
    2:30000,
    3:20000,
    4:3000,
    5:8000,
    6:25000,
    7:10000,
    8:5500,
    9:4500,
    10:6550
    }

items_key = []
qunatity = []

while True:
    print("=" * 149)
    print(" "*50, "Krishna Electronics")
    print(" "*20, "...Welcome to Krishna Electronics store here we will provide quality digital products... ")
    print("=" * 149)

    for key in items:
        print(f"{key}. {items[key]:<80}  {price[key]}")
    print("=" * 149)
    print("11. Exit")
    print("=" * 149)
    choice = int(input("Enter items  number :- "))
    if choice == 11:
        break
        
        
        
    if choice in items:
        user_quantiy = int(input("Enter Quantity :"))
        items_key.append(choice)
        qunatity.append(user_quantiy)
        print("Item added sucessfully")
    else:
        print("invalid choice")
            

print("=" * 149)
print(" "*70, " Final Bill ")
print("=" * 149)

print("|{:^36}|{:^36}|{:^36}|{:^36}|".format("Product Name","Quantity","price","amount"))
print("=" * 149)

total = 0

for i in range(len(items_key)):
    product_name = items[items_key[i]]
    qty = qunatity[i]
    pr = price[items_key[i]]
    amount = qty * pr
    print("|{:^36}|{:^36}|{:^36}|{:^36}|".format(product_name,qty,pr,amount))
    print("=" * 149)
    total += amount
    

print(f"\n"," " * 120,"total amount = RS",total,"/-")
print("=" * 149)


print(" "*60, " Thank You ! visit again.")
print("=" * 149)