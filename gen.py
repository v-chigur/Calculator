#!/usr/bin/env python

from random import *

def num():
    return str(randrange(10))
def op():
    return choice(['-', '+', '*', '/', '%', '^'])
def f():
    return choice([choice(['sin', 'cos', 'tan', 'sqrt', 'asin', 'acos', 'atan']) + '(' + num() + ')'] + ['log' + '(' + num() + ',' + num() + ')'] )

print(num() + op() + '(' + num() + op() + f() + op() + num() + ')' + op() + num())