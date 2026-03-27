# Basic Calculator in Python

def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 == 0:
                    print("Error: Division by zero")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator")
                continue
            
            print("Result:", result)
            
            again = input("Do another calculation? (y/n): ").lower()
            if again != 'y':
                break
                
        except ValueError:
            print("Invalid input. Enter numbers only.")

calculator()
