import subprocess

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


def calculator():
    operations = {
        "+" : add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }
    
    should_accumulate = True
    number1 = float(input("What\'s the first number?: "))
    while should_accumulate:
        
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")

        number2 = float(input("What\'s the next number?: "))

        answer = operations[operation_symbol](number1, number2)
        print(f"{number1} {operation_symbol} {number2} = {answer}")

        choice = input(f"Type \'y\' to continue calculating with {answer}, or type \'n\' to start a new calculation: ")

        if choice == "y":
            number1 = answer
        else:
            should_accumulate = False
            subprocess.call("cls||clear", shell=True)
            calculator()



calculator()

