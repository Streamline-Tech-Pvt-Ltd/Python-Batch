items={
    1:"Karate",
    2:"M45",
    3:"Biovita",
    4:"Profex Super",
    5:"Nativo",
    6:"Bavistin",
    7:"Round Up",
    8:"Urea",
    9:"DAP",
    10:"Gibrallic Acid"
}

price={
    1:500,
    2:2000,
    3:3500,
    4:700,
    5:1500,
    6:300,
    7:3000,
    8:400,
    9:800,
    10:4000
}

items_key = []
quantity = []

while True:
    print("="*80)
    print(" "*25, "🏵️ Shinde's Pesticide Shop 🏵️")
    print("="*80)

    for key in items:
        print(f"{key}. {items[key]:<25} {price[key]} Rs")

    print("="*80)
    print("11.Exit")
    print("="*80)

    choice = int(input("Enter item Number :- "))

    if choice == 11:
            break

    if choice in items:
            user_quantity = int(input("Enter Quantity : "))
            items_key.append(choice)
            quantity.append(user_quantity)
            print("Items added Succesfully....")

    else:
            print("Invalid Choice")


    #final bill

    print("="*120)
    print(" "*50,"Final Bill...")
    print("="*120)

    print("|{:^30}|{:^30}|{:^30}|{:^30}".format("Product_Name","Quantity","Price","Amount"))
    print("="*120)

    total = 0

    for i in range(len(items_key)):
          product_name = items[items_key[i]]
          qty=quantity[i]
          pr = price[items_key[i]]
          amount = qty*pr

          print("|{:^30}|{:^30}|{:^30}|{:^30}".format(product_name,qty,pr,amount))
          print("="*120)

          total += amount

    print(f"\n"," "*90,"$ Toatal Amount","Rs.",total,"/-")
    print("="*120)
    print(" "*55,"Thank You 🙏" \
    "   Visit Again...!!!") 