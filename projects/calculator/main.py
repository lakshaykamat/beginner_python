from enum import Enum

class Operation(Enum):
    ADD = "+"
    MULTIPLY = "*"
    DIVIDE = "/"
    SUBTRACT = "-"

def calculate(num1, num2, operation):
    operations = {
        Operation.ADD: num1 + num2,
        Operation.SUBTRACT: num1 - num2,
        Operation.MULTIPLY: num1 * num2,
        Operation.DIVIDE: num1 / num2 if num2 != 0 else "Division by zero error"
    }

    return operations.get(operation, "Invalid Operation")

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operation():
    while True:
        try:
            op = Operation(input("Operation(+,-,*,/): "))
            return op
        except ValueError:
            print("Invalid operation. Please enter one of +, -, *, /.")

def main():
    num1 = get_number("Num1: ")
    num2 = get_number("Num2: ")
    operation = get_operation()
    
    result = calculate(num1, num2, operation)
    if result == "Invalid Operation":
        print(result)
    elif result == "Division by zero error":
        print(result)
    else:
        print(f"The result of {num1} {operation.value} {num2} = {result}")

if __name__ == "__main__":
    main()
