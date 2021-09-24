from . import Equation
import os
#Reads the equations in EquationSheet.txt and stores those equations and return them into Main.py
class EquationSheet():
    def __init__(self):
        self.EquationSet = []

    def print(self):
        strEquationSet = ', '.join(str(var.print()) for var in self.EquationSet)
        print(strEquationSet)

    def readEquationSheet(self):

        with open(os.path.join(os.sys.path[0], "ItemFolder\EquationSheet.txt"), "r") as reader:

            lines = reader.readlines()
            for line in lines:
                wordList = line.split(' ')
                name = wordList[0]
                equation = wordList[1].strip()
                variableList = []

                for char in equation:
                    if char not in "/*123456789n0+-=":
                        variableList.append(char)

                self.EquationSet.append(Equation.Equation(name,equation,variableList))