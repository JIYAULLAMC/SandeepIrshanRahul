class Manager:
    def __init__(self, name, mgr=None):
        self.name = name
        self.mgr = mgr


    
class Employee:
    def __init__(self, name, mnr=None):
        self.name =name
        self.mnr = mnr 

m = Manager("Steeve")
e = Employee("Bob")