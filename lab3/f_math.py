from random import randint,choice
from ex2 import evaluate

f_n= choice(["+","-","*","/"])
x=randint(0,9)
y=randint(0,9)
error = randint(-1,1)

r = evaluate(f_n,x,y) + error
# r = i + error
r_a = (error == 0)
print(f"{x}{f_n}{y}={r}")

while True:
    user_choice = input("Your answer?(Y/N)").upper()
    if user_choice != "Y" and user_choice != "N":
        print("Choose Y/N answer!")
    else:
        break
u_a = (user_choice == "Y")
if u_a == r_a:
    print("Yay!")
else:
    print("Wrong!")
    
