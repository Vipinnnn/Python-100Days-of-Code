# Calculator
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

continue_calculations = True
while continue_calculations:
    num1 = float(input("Enter first number:\n"))
    for symbol in operators:
        print(symbol)
    operator = input("Enter the operator: ")
    num2 = float(input("Enter second number:\n"))
    selected_operation = operators[operator]
    answer = selected_operation(num1, num2)
    print(f"{num1} {operator} {num2} = {answer} ")
    wish_to_continue = int(input("Enter 0 to continue 1 to stop: "))
    if wish_to_continue == 1:
        continue_calculations = False
