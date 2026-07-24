domain = {
    1:'Full Stack Python',
    2:'Full Stack Java',
    3:'Data Analytics',
    4:'Data Science',
    5:'Gen AI',
    6:'Agent AI',
}

price ={
    1:30000,
    2:30000,    
    3:32000,
    4:35000,
    5:35000,
    6:33000,
}

   
domain_key = []
quantity = []


while True:
    print("="*120)
    print(" "*30,"Welcome to the Streamline Tech Billing Software")
    print("="*120)
    # print("S.No"," "*20,"Domain Name"," "*70,"Price")
    print("|{:^20}|{:^30}|{:^66}|".format('sr_no', 'Domain Name', 'Price'))
    print("="*120)

    for key in domain:
        print(f"|{key:^20}|{domain[key]:^30}|{price[key]:^66}|")
        
    print("="*120)
    print("|{:^20}|{:^30}|{:^66}|".format(7, 'Exit'," "))
    print("="*120) 
    choice = int(input("Enter the Domain ID : "))   
    
    if choice == 7:
        break

    if choice in domain:
        qun = int(input("Enter the quantity : "))
        
        if choice in domain_key:
            ind = domain_key.index(choice)
            quantity[ind] += qun
        
        else:
            domain_key.append(choice)
            quantity.append(qun)
        
        # print(domain_key)
        # print(quantity)
    else:
        print("Invalid Input")
        

print("="*120)
print(" "*50,"Total Bill")
print("="*120)
print("|{:^20}|{:^35}|{:^30}|{:^30}|".format('sr_no', 'Domain Name','Quantity','Amount'))
print("="*120)

total = 0 

# domain_key =[1,2]

for i in range(len(domain_key)):
    sr_no = i+1
    do = domain[domain_key[i]]
    pr = price[domain_key[i]]
    qu  = quantity[i]
    amount = qu * pr
    print("|{:^20}|{:^35}|{:^30}|{:^30}|".format(sr_no,do,qu,amount))
    
    total += amount

print("="*120)
print(" "*80,"Total Bill Amount = RS-",total,"/-")
print("="*120)
print(" "*40,"Thank you for visiting Streamline tech")
print("="*120)
