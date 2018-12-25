from random import *

def evaluate(fun,a,b):
    if fun== "+":
        n = a + b
    elif fun == "-":
        n = a - b
    elif fun == "*":
        n = a * b
    elif fun == "/":
        n = a/b
    return n

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x=randint(0,9)
    while True:
        y=randint(0,9)
        fn = choice(["+","-","*","/"])
        if y != 0 and fn !="/":
            break
    error = randint(-1,1)
    r = evaluate(fn,x,y) + error
    return [x, y, fn , r]

def check_answer(x, y,fn, r, user_choice):
    if r == evaluate(fn,x,y):
        r_b = True
    else:
        r_b = False
    if user_choice == r_b:
        return True
    else:
        return False
    pass
