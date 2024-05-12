
class Employee1(object):    # RE
    def __init__(self):
        self.type = "Employee1"

    def new(self):
        print(self.type, ' New is NOT allowed')

    def delete(self):
        print(self.type, ' Delete is NOT allowed')

    def read(self):
        print(self.type, ' Read is allowed')

    def alter(self):
        print(self.type, ' Alter is NOT allowed')

    def execute(self):
        print(self.type, ' Execute is allowed')


class Manager1(Employee1):  # RDE
    def __init__(self):
        self.type = "Manager1"

    def delete(self):
        print(self.type, ' Delete is allowed')

