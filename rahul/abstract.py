#specializaion

"""

#example for abstraction

#abstraction is the process where we hide the implimentation and 
# allow the give authority use functionality
# we not able to create the object for abstract class

from abc import ABC, abstractclassmethod



class myclass(ABC):
    
    @abstractclassmethod
    def mymethod(self):
        pass





class person(myclass):
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def work(self):
        print("person will work ")
        return f"{self.name} is working"


    # def mymethod(self):
    #     print("this is the mymethod in person class")




p1 = person("name", 38)

p1.mymethod()
p1.work()


"""