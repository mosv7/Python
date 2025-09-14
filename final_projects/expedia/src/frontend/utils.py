def input_valid_int(msg, start = 0, end = None):
    while True:
        inp = input(msg)

        if not inp.isdecimal():
            print('invalid input, please try again')
        elif end is not None:
            if start <= int(inp) <= end:
                return int(inp)
            else:
                print('invalid input, please try again')
        else:
            return int(inp)

def get_menu_choice(top_msg, messages):
    print(f'\n{top_msg}')

    messages = [f'{i + 1}  {message}' for i, message in enumerate(messages)]
    print('\n'.join(messages))

    msg = f'Enter a number between 1 and {len(messages)}: '
    return input_valid_int(msg, 1, len(messages))