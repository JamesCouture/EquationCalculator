from ItemFolder import *

#This is the main file that operates the software
if __name__ == "__main__":

    def equationSheetReader():
        #reader of the txt file
        return

    conti = True

    '''test = Variable.Variable("x",5,"k")
    test.print()

    testEquation = Equation.Equation("test","1=xyz",["x","y","z"])
    testEquation.print()'''

    equationSheet = EquationSheetReader.EquationSheet()
    equationSheet.readEquationSheet()

    for i in range(len(equationSheet.EquationSet)):
        equationSheet.EquationSet[i].print()


