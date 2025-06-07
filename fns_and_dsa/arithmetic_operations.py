def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtraction':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'division':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation."

def main():
    print("Arithmetic Operations")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (add, subtraction, multiply, division): ")

        result = perform_operation(num1, num2, operation)
        print(f"Result: {result}")
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
