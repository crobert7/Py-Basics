def print_keyword_arg(**kwargs):
    print('\n')
    print(kwargs)
    print(type(kwargs))

    for key, value in kwargs.items():
        print(f'{key} = {value}')

    third = kwargs.get('third', None)
    if third != None:
        print('third arg =', third)


print_keyword_arg(first = 'a')
print_keyword_arg(first = 'b', second = 'c')
print_keyword_arg(first = 'd', second = 'e', third = 'f')

