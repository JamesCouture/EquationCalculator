class Equation:
    def __init__(self, name, equationString, listOfVariables):
        self.name = name
        self.equationString = equationString
        self.equationRepresentation = None
        self.listOfVariables = listOfVariables

    def setEquationReplesentation(self, representation):
        self.equationRepresentation = representation

    def print(self):

        strListOfVariables = ', '.join(self.listOfVariables)

        if self.equationRepresentation == None:
            print(
                "Name: " + self.name + ", Equation string: " + self.equationString + ", Equation representation: None, List of variables: " + strListOfVariables)
        else:
            print(
                "Name: " + self.name + ", Equation string: " + self.equationString + ", Equation representation: " + self.equationRepresentation+ ", List of variables: " + strListOfVariables)

