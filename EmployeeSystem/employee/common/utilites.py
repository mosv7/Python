def input_valid_int(msg, start = 0, end = None):
    while True:
        inp = input(msg)

        if not inp.isdecimal():
            print('Invalid range. Try again!')
        
        elif end is not None:
            if not (start <= int(inp) <= end):
                print('Invalid range. Try again!')
            else:
                return int(inp)
        
        else:
            return int(inp)