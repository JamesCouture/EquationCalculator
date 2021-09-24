class Equation:
    def __init__(self, name, equationString, listOfVariables):
        self.name = name
        self.equationString = equationString
        self.equationRepresentation = None
        self.listOfVariables = listOfVariables

    '''set the equation representation'''
    def setEquationReplesentation(self, representation):
        self.equationRepresentation = representation

    '''Printing the equation in order to help visualize the equation'''
    def print(self):

        strListOfVariables = ', '.join(self.listOfVariables)

        if self.equationRepresentation == None:
            print(
                "Name: " + self.name + ", Equation string: " + self.equationString + ", Equation representation: None, List of variables: " + strListOfVariables)
        else:
            print(
                "Name: " + self.name + ", Equation string: " + self.equationString + ", Equation representation: " + self.equationRepresentation+ ", List of variables: " + strListOfVariables)

