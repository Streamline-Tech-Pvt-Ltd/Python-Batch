items ={1:"pencile",
        2:"shopner",
        3:"pen",
        4:"notebook",
        5:"paper",
        6:"writing board",
        7:"book"}

price = {
    1:10,
    2:20,
    3:14,
    4:34,
    5:20,
    6:35,
    7:30}

items_key = []
qnty = []

while True:
    print("+"*120)
    print(" "*45,"WELCOME TO GENERAL STORE ! 🙏")
    print(" "*45, "🏵️  Rahul's General store 🏵️")
    print("")
    print("="*120)


    for key in items:
        print(f"{key}.  {items[key]:<110} {price[key]}")

    print("="*120)
    print("8.exit")
    print("="*120)

    choice = int(input("enter product number:"))


    if choice == 8:
        break

    if choice in items:
        user_qnty = int(input("enter quantity of product:"))
        items_key.append(choice)
        qnty.append(user_qnty)
        print("Item is succesfully added....")


    else:
        print("invalid choice")


# final bill

print("="*120)
print(" "*50,"Final Bill...")
print("="*120)

print("|{:^30}|{:^30}|{:^30}|{:^30}".format("Product Name","Quantity","Price","Amount"))
print("="*120)

total = 0

for i in range(len(items_key)):
    product_name = items[items_key[i]]
    qty = qnty[i]
    pr = price[items_key[i]]
    amount = qty * pr

    print("|{:^30}|{:^30}|{:^30}|{:^30}".format(product_name,qty,pr,amount))
    print("="*120)

    total += amount

print(f"\n"," "*90,"...Total amount","RS.",total,"/-")
print("="*120)
print(" "*55,"🙏Thank You !")
print("*"*120)

