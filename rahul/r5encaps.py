from r4encaps import virus

class computer(virus):
    def __init__(self):
        #access specifires in the class
        self.p = 100
        self._q = 200
        self.__r = 300
        

    def test(self):
         # we can acces public protected and preivate within the class
        print(self.p, self._q, self.__r)
        # we can accesss public attribute of another class of another file
        print(self.a)
        # we can accesss ptlic and protected attribute of another class of another file
        # print(self.a, self._b)
        # we can accesss public and protected attribute of another class but not private if another file
        # print(self.a, self._b, self.__c)


c1 = computer()
c1.test()
c1.view()