print("============CALCULATOR============")

print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")

option = int(input("Choose an operation(1-4): "))

if (option in [1,2,3,4]):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if (option == 1):
        result = num1 + num2
    elif(option == 2):
        result = num1 - num2
    elif(option == 3):
        result = num1 * num2
    elif(option == 4):
        if num2 == 0:
            result = "Not dividable"
        else:
            result = num1 / num2
        
        print(f'Result of operation is {result}')
        
else:
    print("Invalid operation")
