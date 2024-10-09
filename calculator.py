from art import logo
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

def calculator():
    print(logo)
    should_continue = True
    first_number = int(input("Type the first number: "))
    number = first_number
    while should_continue:
        chosen_operator = input('Choose an operator "+", "-", "*" or "/": ')
        second_number = int(input("Type the second number: "))
        result = ""
        if chosen_operator == "+":
            result = operators["+"](number, second_number)

        elif chosen_operator == "-":
            result = operators["-"](number, second_number)

        elif chosen_operator == "*":
            result = operators["*"](number, second_number)

        elif chosen_operator == "/":
            result = operators["/"](number, second_number)
        print(result)
        number = result
        want_to_continue = input("Do you wants to continue working with the previous result? yes/no: ")
        if want_to_continue == "no":
            print("\n"*40)
            calculator()
calculator()
