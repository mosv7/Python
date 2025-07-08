while True:
    print("""
Menu:
Enter 1 to sum numbers from 1 to N
Enter 2 to evaluate simple 2 number expression (e.g. 2 + 3)
Enter 3 to end the program
""")
    choice = int(input('Enter choice from 1 to 3: '))


    if 0 < choice < 4:
        if choice == 1:
            n = int(input('Enter a number: '))
            sum = (n * (n + 1)) // 2  # Using the formula for sum of first n natural numbers
            print(f'Sum from 1 to {n} is {sum}')

        elif choice == 2:
            num1, op, num2 = input('Enter a simple expression: ').split()
            num1, num2 = float(num1), float(num2)

            if op == '+':
                print('Expression value is', num1 + num2)
            elif op == '-':
                print('Expression value is', num1 - num2)
            elif op == '*':
                print('Expression value is', num1 * num2)
            elif op == '/':
                if num2 == 0:
                    print('Error: Division by zero is not allowed.')
                else:
                    print('Expression value is', num1 / num2)
            elif op == '//':
                if num2 == 0:
                    print('Error: Division by zero is not allowed.')
                else:
                    print('Expression value is', num1 // num2)
            else:
                print('Expression value is', num1 ** num2)

        else:
            break
    else:
        print('Invalid Input...Try again')
