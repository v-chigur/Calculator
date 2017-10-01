from random import *

def num():
    return str(randrange(100500))
def op():
    return choice(['-', '+', '*', '/', '%'])

for i in range(10 ** 5):
    for j in range(10):
        print(num() + op() + '(' + num() + op() + num() + ')' + op() + num())