# function accepting an arbitrary arguments lists
# Use arbitrary arguments lists in functions when you don't know how many arguments 
# callers will pass but want the functions to handle whatever is passed. 
def print_arg(* args):
    # for arg in args:
        # print(f'arg {arg}')
    print(args)
    print(type(args))

print_arg('a')
print_arg('a','b')
print_arg('a','b','c')

def print_keyword_args(**kwargs):
    third = kwargs.get('third', None)
    
    if third != None:
        print('third arg = ', third)

print_keyword_args(first = 'a')
print_keyword_args(first = 'b', second = 'c')
print_keyword_args(first = 'd', second = 'e', third = 'f')
