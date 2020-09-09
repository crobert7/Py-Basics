def readint(prompt, min, max):
    ok = False 
    while not ok:
        try:
            user_input = int(input(prompt))
            ok = True
        except ValueError:
            print('Error: wrong input')
        if ok:
            ok = user_input >= min and user_input <= max
        if not ok:
            print('Error the value s not within the permitted range (' + str(min) + '..' + str(max) + ')')
    return user_input

v = readint('Enter a number from -10 to 10: ', -10, 10) # <--- arguments

print('The number is:', v)