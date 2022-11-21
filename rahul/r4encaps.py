# example for hybrid inheritence 


class virus:
    def __init__(self):
        #access specifires in the class
        self.a = 1
        self._b = 2
        self.__c = 3

    def view(self):
        # we can acces public protected and preivate within the class
        print(self.a, self._b, self.__c) 



# class antivirus(virus):
#     def __init__(self):
#         #access specifires in the class
#         self.x = 10
#         self._y = 20
#         self.__z= 30

#     def display(self):
#         # we can acces public protected and preivate within the class
#         print(self.x, self._y, self.__z)
#         # we can accesss public attribute of another class
#         print(self.a)
#         # we can accesss ptlic and protected attribute of another class
#         # print(self.a, self._b)
#         # we can accesss public and protected attribute of another class but not private
#         # print(self.a, self._b, self.__c)



# v  = virus()
# v.view()