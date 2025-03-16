def calculator():
    try:
        # Prompt user for the first number
        num1 = float(input("Enter the first number: "))
        # Prompt user for the second number
        num2 = float(input("Enter the second number: "))
        # Prompt user for the operation
        operation = input("Enter the operation (+, -, *, /): ")

        # Perform the appropriate operation based on user input
        if operation == '+':
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
        else:
            print("Error: Invalid operation. Please enter one of +, -, *, or /.")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values for numbers.")

# Call the calculator function to execute the program
calculator()
