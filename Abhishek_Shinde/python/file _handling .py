try:
    f = open("demo.txt", "r")
    num = int(f.read())
    print(10 / num)
    f.close()

except FileNotFoundError:
    print("File not found")

except ValueError:
    print("Invalid data in file")

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program completed")