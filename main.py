def add(num_one, num_two):
    return num_one + num_two

def subtract(num_one, num_two):
    return num_one - num_two

def multiply(num_one, num_two):
    return num_one * num_two

def divide(num_one, num_two):
    return num_one / num_two

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

current_result = 0 
while True:
    first_input = float(input("Input first number: "))
    current_result = first_input
    while True:
        print("+\n-\n*\n/")
        operator_used = input("Pick an operation: ")
        second_input = float(input("Input next number: "))

        previous_result = current_result
        current_result = operators[operator_used](current_result, second_input)

        print(f"\n{previous_result} {operator_used} {second_input} = {current_result}\n")
        continue_or_start = input(f"Type 'y' to continue calculating with {current_result}\nType 'n' to start a new calculation: ")

        if continue_or_start == "n":
            break
        elif continue_or_start == "y":
            continue

