#!/usr/bin/python


mathFormull = input("What is your math formull?\n")

formullList = []
x = None
y = None
z = None
i = None

for i in mathFormull:
    if i == "(":
        x = "start"
        formullList.append(i)
        continue
    elif i.isdigit():
        if x == "start":
           x = i
        elif x != None:
           x += i
        elif y != None:
           y += i
        else:
           y = i
    elif i in ["+","-","*","/","//","%","**"]:
 #       print (f" i = {i} & x = {x} & y = {y} & formullList = {formullList}")
        if x is not None:
            formullList.append(int(x))
            x = None
        elif y is not None:
           formullList.append(int(y))
           y = None
        elif formullList[-1] == i :
#            print (f"i = {i} & formullList[-2] = {formullList[-1]}")
            if i == "/":
                formullList[-1] = "//"
                continue
            elif i == "*":
                formullList[-1] = "**"
                continue
        formullList.append(i)
    elif i == ")":
        if x is not None:
            formullList.append(int(x))
            x = None
        elif y is not None:
            formullList.append(int(y))
            y = None
        formullList.append(i)
    else:
        print(f"Undefined character \"{i}\" is in your formull!")
        break
else:
    if x == None and y == None:
        print(f"You input {i}, Please input correct frormull!")

if x != None:
    formullList.append(int(x))
elif y != None:
    formullList.append(int(y))


print(f" formulllist = {formullList}\n x = {x}\n y = {y}\n")

