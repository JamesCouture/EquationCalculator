#Class Variable
class Variable:
    def __init__(self, name, value, unit):
        self.name = name
        self.value = value
        self.unit = unit

    def print(self):
        print(self.name + " = " + str(self.value) + self.unit)
