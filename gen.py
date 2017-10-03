#!/usr/bin/env python

from random import *

def num():
    return str(randrange(100500))
def op():
    return choice(['-', '+', '*', '/', '%'])

print(num() + op() + '(' + num() + op() + num() + ')' + op() + num())