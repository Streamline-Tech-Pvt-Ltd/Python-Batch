def fibonacci():
    a = 0
    b = 1

    while True:
        yield a

        a,b = b,a+b
        
n = int(input("Enter The Number:"))

f = fibonacci()
for i in range(n):
    print(next(f))

