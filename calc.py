#!/usr/bin/python

class mathCalculator:

#    testFormula = "1+2*(9-6/(3+4*5))-7+8*0"

    # this function get math formula from input
    def mathFormula(self):
        return input("What is your math formull? Something like:  1+2*(9-6/(3+4*5))-7+8*0  \n")

    # This function adds two numbers
    def add(self, x, y):
#        print(f" add x = {x} & y = {y}")
        return x + y

    # This function subtracts two numbers
    def subtract(self, x, y):
#        print(f" subtract x = {x} & y = {y}")
        return x - y

    # This function multiplies two numbers
    def multiply(self, x, y):
#        print(f" multiply x = {x} & y = {y}")
        return x * y

    # This function divides two numbers
    def divide(self, x, y):
#        print(f" divide x = {x} & y = {y}")
        return x / y

    # This function Exponent two numbers
    def exponent(self, x, y):
#        print(f" exponent x = {x} & y = {y}")
        return x ** y

    # This function Floor divides two numbers
    def floorDivide(self, x, y):
#        print(f" floorDivide x = {x} & y = {y}")
        return x // y

    # This function Floor divides two numbers
    def reminder(self, x, y):
#        print(f" reminder x = {x} & y = {y}")
        return x % y

    def formula2List(self, txtFormula):

        formula2List = []
        x = None
        y = None
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
                if formula2List == [] and x == None and y == None:
                    print(f"You input an operator {i}, in first of formula, please correct your formula")
                    break
                else:
                    if x is not None:
                        formula2List.append(int(x))
                        x = None
                    elif y is not None:
                       formula2List.append(int(y))
                       y = None
                    elif formula2List[-1] == i :
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

        self.gFormulaList = formula2List
        return formula2List

    def removeListItems(self, formula2List, m, n, s = 1):
        # print(f" Line121: formula2List = {formula2List} & -------  m = {m} & n = {n} & s = {s}    \n")
        for j in range(m, n, s):
            formula2List.pop(j)
            # print(f" Line124: formula2List = {formula2List} & --  m = {m} & n = {n} & s = {s} & j = {j} ")

    test =1

    def solveFormula(self, formula2List):


        i = 0
        z = 0
        lParenthese = 0
        totalRemovedParentheses = -1
        zone = 0

        # print(f" Line137: --- formula2List = {formula2List} ---")

        while len(formula2List) > 1:


            # print(f" Line142: --- formula2List = {formula2List}  ---")

            if type(formula2List[i]) in [int, float]:
                # print(f" Line145: --- formula2List = {formula2List} ---")

                if formula2List[i+1] in ["+", "-", "*","/","//","%","**"]:
                    # print(f" Line148: --- formula2List = {formula2List} ---")

                    if formula2List[i+2] == "(":
                        afterParentheses = False
                        totalRemovedParentheses = 1
                        # print(f" Line153: i = {i} & z = {z} & formula2List = {formula2List} & len(formula2List) = {len(formula2List)}")
                        for z in range(i+3,len(formula2List)):
                            # print(f" Line155: --- formula2List = {formula2List} ---")
                            totalRemovedParentheses += 1
                            if formula2List[z] == "(":
                                # print(f" Line158: --- formula2List = {formula2List} ---")
                                lParenthese += 1
                            elif formula2List[z] == ")" and lParenthese == 0:
                                # print(f" Line161: i = {i} & i+2 = {i+2} & z = {z} & formula2List ={formula2List} & formula2List[{z}] = {formula2List[z]}")
                                lParenthese = -1
                                formula2List.pop(z)
                                formula2List.pop(i+2)
                                tempList1 = formula2List[i+2:z-1]
                                tempList2 = formula2List[z:]
#                                print(f" ~~~~~~ Line167: --- formula2List = {formula2List} tempList1 ={tempList1} & tempList2 = {tempList2} ---")
                                formula2List.insert(i+2,self.solveFormula(tempList1))
                                # print(f" Line169: --- formula2List = {formula2List} & i={i} & z={z} ---")
                                self.removeListItems(formula2List, z-1, i+2, -1)
                                # print(f" Line171: --- formula2List = {formula2List} ---")
                                if tempList2 != []:
#                                    print(f"-1111- Line173: --- formula2List = {formula2List} & i={i} & z={z}---")
                                    formula2List.insert(i+4,self.solveFormula(tempList2))
#                                    print(f"-2222- Line175: --- formula2List = {formula2List} & i={i} & z={z} & len(tempList2 | 1)= {len(tempList2)} | {len(tempList1)} \
#                                            & len(formula2List) = {len(formula2List)} ---")
                                    self.removeListItems(formula2List, len(formula2List)-1, i+4, -1)
#                                    print(f"-3333- Line178: --- formula2List = {formula2List} & i={i} & z={z}---")
                                    formula2List.insert(i,self.solveFormula(formula2List))
#                                    print(f"-4444- Line180: --- formula2List = {formula2List} & i={i} & z={z} & len(tempList2 | 1)= {len(tempList2)} | {len(tempList1)} \
#                                            & len(formula2List) = {len(formula2List)} ---")
                                    self.removeListItems(formula2List, len(formula2List)-1, i, -1)
#                                    print(f"-5555- Line183: --- formula2List = {formula2List} ---")
                                if len(formula2List) == 1:
                                    return formula2List[0]
                                afterParentheses = True
                                break
                            elif formula2List[z] == ")" and lParenthese > 0:
                                # print(f" Line190: --- formula2List = {formula2List} ---")
                                lParenthese -= 1
                            elif lParenthese > 0 and z == len(formula2List):
                                # print(f" Line193: --- formula2List = {formula2List} ---")
                                print("Parentheses are undefined!! please correct them in your formula!")
                                exit(0)
#                        print(f"@@@@ Line196: formula2List = {formula2List}")
                        if len(formula2List) > 3 and afterParentheses == True:
#                            print(f"%%% Line198: continue --- formula2List[zone:] = {formula2List[zone:]} & zone = {zone}---")
                            continue
                    iNumber = False
                    if len(formula2List) > 3:
                        if type(formula2List[i+2]) in [int, float]:
                            iNumber = True

                    if iNumber or (len(formula2List) <= 3 and type(formula2List[0]) in [int,float]):
                        # print(f" Line206: --- formula2List = {formula2List} ---")

                        if formula2List[i+1] == "**":
                            x = formula2List[i]
                            y = formula2List[i+2]
                            self.removeListItems(formula2List, i+2, i, -1)
                            formula2List.insert(i,self.exponent(x, y))
                            return formula2List[0]

                        elif formula2List[i+1] == "//":
                            x = formula2List[i]
                            y = formula2List[i+2]
                            self.removeListItems(formula2List, i+2, i, -1)
                            formula2List.insert(i,self.floorDivide(x, y))
                            return formula2List[0]

                        elif formula2List[i+1] == "%":
                            x = formula2List[i]
                            y = formula2List[i+2]
                            self.removeListItems(formula2List, i+2, i, -1)
                            formula2List.insert(i,self.reminder(x, y))
                            return formula2List[0]

                        elif formula2List[i+1] == "/":
                            x = formula2List[i]
                            y = formula2List[i+2]
                            self.removeListItems(formula2List, i+2, i, -1)
                            formula2List.insert(i,self.divide(x,y))
                            return formula2List[0]

                        elif formula2List[i+1] == "*":
                            x = formula2List[i]
                            y = formula2List[i+2]
                            # print(f" Line239 i = {i} & formula2List = {formula2List} & x = {x} & y = {y}")
                            formula2List.insert(i,self.multiply(x, y))
                            self.removeListItems(formula2List, i+3, i, -1)
                            # print(f" Line242 i = {i} & formula2List = {formula2List} & x = {x} & y = {y}")
                            if len(formula2List) == 1:
                                return formula2List[0]
                            else:
                                continue

                        elif formula2List[i+1] == "+":
                            x = formula2List[i]
                            y = formula2List[i+2]
                            i3 = False
                            if len(formula2List) > 3:
                                if formula2List[i+3] in ["+","-"]:
                                    i3 = True
                            if i3:
#                                print(f"*** Line256: --- formula2List = {formula2List} ---")
                                self.removeListItems(formula2List, i+3, i, -1)
                                formula2List.insert(i,self.add(x, y))
#                                print(f"*** Line259: --- formula2List = {formula2List} ---")
                                return formula2List[0]
                            elif len(formula2List) == 3:
#                                print(f"*** Line262: --- formula2List = {formula2List} ---")
                                formula2List.insert(i,self.add(x, y))
                                self.removeListItems(formula2List, 2, 0, -1)
#                                print(f"*** Line265: --- formula2List = {formula2List} ---")
                                return formula2List[0]
                            else:
#                                print(f"*** Line268: --- formula2List = {formula2List}  ---\n\n")
                                formula2List.insert(i,self.add(x, self.solveFormula(formula2List[i+2:])))
                                self.removeListItems(formula2List, len(formula2List)-1, i, -1)
#                                print(f"*** Line271: --- formula2List = {formula2List} ---")
                                return formula2List[0]

                        elif formula2List[i+1] == "-":
                            x = formula2List[i]
                            y = formula2List[i+2]
                            i3 = False
                            if len(formula2List) > 3:
                                if formula2List[i+3] in ["+","-"]:
                                    i3 = True
                            if i3:
                                # print(f" Line282: --- formula2List = {formula2List} ---")
                                self.removeListItems(formula2List, i+3, i, -1)
                                formula2List.insert(i,self.subtract(x, y))
                                # print(f" Line285: --- formula2List = {formula2List} ---")
                                return formula2List[0]
                            elif len(formula2List) == 3:
                                # print(f" Line288: --- formula2List = {formula2List} ---")
                                formula2List.insert(i,self.subtract(x, y))
                                self.removeListItems(formula2List, 2, 0, -1)
                                # print(f" Line291: --- formula2List = {formula2List} ---")
                                return formula2List[0]
                            else:
                                # print(f" Line294: --- formula2List = {formula2List} ---")
                                formula2List.insert(i,self.subtract(x, self.solveFormula(formula2List[i+2:])))
                                self.removeListItems(formula2List, len(formula2List)-1, i, -1)
                                # print(f" Line297: --- formula2List = {formula2List} ---")
                                return formula2List[0]

                else:
                    print(f"something is rong, formula2List[{i}] = {formula2List[i]}")
                    exit(0)
            else:
                print(f"An unknown Error happend. formula2List = {formula2List}")
                exit(0)

        # print(f" Line307: formula2List() = {formula2List}\n")
        return -2000000  #formula2List[0]



#  Create an instance of class and test it
if __name__ == '__main__':
    clss = mathCalculator()
    fList = clss.formula2List(clss.mathFormula())   #clss.mathFormula())
    #print(f" formula2List = {fList}\n")

    f1List = clss.solveFormula(fList)
    print(f" Result = {f1List}")




