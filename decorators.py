# This script uses 2 functions: one inner and one outer function

def outer_func(msg):
    def inner_func():
        print(msg)

    return inner_func # no () to work


hi_func = outer_func('Hi is the outer function')

bye_func = outer_func('Bye is the inner function')

print('-------------------------------------------------------------')

print('A decorator is a function taking another one as argument...')

hi_func()

print()

print('def outer_function:')

print('    def inner_function:')

print()

bye_func()

print()

print('-------------------------------------------------------------')
