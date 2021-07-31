#!/usr/bin/python

class mathCalculator:


    sum = None

    # this function get math formula from input
    def mathFormula(self):
        return input("What is your math formull?\n")

    # This function adds two numbers
    def add(self, x, y):
        return x + y

    # This function subtracts two numbers
    def subtract(self, x, y):
        return x - y

    # This function multiplies two numbers
    def multiply(self, x, y):
        return x * y

    # This function divides two numbers
    def divide(self, x, y):
        return x / y

    # This function Exponent two numbers
    def exponent(self, x, y):
        return x ** y

    # This function Floor divides two numbers
    def floorDivide(self, x, y):
        return x // y

    def formula2List(self, txtFormula):

        formula2List = []
        x = None
        y = None
        z = None
        i = None
        parentheses = 0
        currentIndex = -1

        for i in txtFormula:
            currentIndex += 1
            if i == "(":
                x = "start"
                formula2List.append(i)
                parentheses += 1
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
                if formula2List == [] and x == None and y == None:
                    print(f"You input an operator {i}, in first of formula, please correct your formula")
                    break
                else:
                    z = i
                    if x is not None:
                        formula2List.append(int(x))
                        x = None
                    elif y is not None:
                       formula2List.append(int(y))
                       y = None
                    elif formula2List[-1] == i :
            #            print (f"i = {i} & formullList[-2] = {formullList[-1]}")
                        if i == "/":
                            formula2List[-1] = "//"
                            continue
                        elif i == "*":
                            formula2List[-1] = "**"
                            continue
                    formula2List.append(i)
            elif i == ")":
                if parentheses == 0:
                    print("You input more parenthese ')' in your formula, please correct your formula")
                    break
                else:
                    if x is not None:
                        formula2List.append(int(x))
                        x = None
                    elif y is not None:
                        formula2List.append(int(y))
                        y = None
                    formula2List.append(i)
                    parentheses -= 1
            else:
                print(f"Undefined character \"{i}\" is in your formula. Please input correct frormula!")
                break
        else:
            if x == None and y == None:
                print(f"You input {i}, Please input correct frormula!")
            elif parentheses != 0:
                print("You didn't close all your parentheses, please correct your formula!")

        if x != None and x != "start":
            formula2List.append(int(x))
        elif y != None:
            formula2List.append(int(y))

        return formula2List

clss = mathCalculator()
fList = clss.formula2List(clss.mathFormula())
print(f" formula2List = {fList}\n")


    #def formulaSolution(myList = []):
    #    for i in myList:
    #        if i.isdigit():
    #            formulaResult = i


    #rightParantese = formulaList.index(")")
    #leftParantese = None

    #print(rightParantese)

    #for m  in range(formulaList.index(")")-1):
    #    if formulaList[6:-1] == "(":
    #        leftParantese = m
    #        break

    #for i in range(leftParantese+1:rightParantese-1):
    #    if formulaList[i].isdigit:
    #        sum = formulaList[i]
    #    elif formulaList[i] in ["+","-","*","/","//","%","**"]:
    #        operator = formulaList[i]
    #        continue






