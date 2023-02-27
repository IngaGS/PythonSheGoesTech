import re

print ("Magical calculator")
print("Enter 'quit' to exit\n")

previous=0
run=True

def performMath():
    global run
    global previous
    equation=""
    if previous== 0:
        equation=input("Enter equation")
    else:
        equation=input(str(previous))


    if equation=='quit':
        print("Goodbye, Inga")
        run=False
    else:
        equation=re.sub('[a-zA-z,.:()" "]','',equation)

        if previous==0:
            previous=eval(equation)
        else:
            previous=eval(str(previous)+equation)

while run:
    performMath()