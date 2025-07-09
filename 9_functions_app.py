def read_expression():
    expression = input('Enter a simple expression (e.g. 2 + 3): ')
    num1, operator, num2 = expression.split()
    return int(num1), operator, int(num2)

def sum_from_1_to_n(n):
    """Calculate the sum of all natural numbers from 1 to n."""
    return (n * (n + 1)) // 2  # Using the formula for sum of first n natural numbers

def read_number():
    n = int(input('Enter a number: '))
    return n

def calculator(num1, operator, num2):
    """Perform basic arithmetic operations based on the operator."""
    if operator == '+':
        print('Expression value is', num1 + num2)
    elif operator == '-':
        print('Expression value is', num1 - num2)
    elif operator == '*':
        print('Expression value is', num1 * num2)
    elif operator == '/':
        if num2 == 0:
            print('Error: Division by zero is not allowed.')
        else:
            print('Expression value is', num1 / num2)
    elif operator == '//':
        if num2 == 0:
            print('Error: Division by zero is not allowed.')
        else:
            print('Expression value is', num1 // num2)
    else:
        print('Expression value is', num1 ** num2)

def manipulate(option):
    if 1 <= option <= 3:
        if option == 1:
            n = read_number()
            print(f'Sum from 1 to {n} is {sum_from_1_to_n(n)}')

        elif option == 2:
            num1, operator, num2 = read_expression()
            calculator(num1, operator, num2)
        else:
            print('Ending the program...')
            exit(0)
    else:
        print('Invalid Input...Try again')

def choose_option():
    option = int(input('Enter choice from 1 to 3: '))
    return option

def start():
    while True:
            print("""
Menu:
Enter 1 to sum numbers from 1 to N
Enter 2 to evaluate simple 2 number expression (e.g. 2 + 3)
Enter 3 to end the program
""")
            option = choose_option()
            manipulate(option)

start()