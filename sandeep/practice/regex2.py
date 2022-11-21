class Circle:

    def __init__(self, radius):
        self.radius = radius


    @property
    def radius(self):
        return self._radius


    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Only numbers are allowed")
        self._radius = value

    def circumference(self):
        return 2*3.142*self.radius


        