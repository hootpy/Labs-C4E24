# x = int(input("Enter first number"))
# y = int(input("Enter second number"))

# fun = input("Funtion:")
def evaluate(fun,x,y):
    if fun== "+":
        n = x + y
    elif fun == "-":
        n = x - y
    elif fun == "*":
        n = x * y
    elif fun == "/":
        n = x/y
    return n

