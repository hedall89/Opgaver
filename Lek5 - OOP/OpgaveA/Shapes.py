import math

class Squares:
    def __init__(self, side1, side2):
        assert type(side1) == int and type(side2) == int, "ints not used"
        self.side1 = side1
        self.side2 = side2


    def __str__(self):
        return f"Firkantens side1 = {self.side1} og side2 = {self.side2}"

    def getArea(self):
        area = self.side1 * self.side2
        return area

    def getCircumferende(self):
        circumference = 4 * self.side1
        return circumference

    def __add__(self, other):
        self_sum = self.getArea()
        other_sum = other.getArea()

        return (self_sum + other_sum)




class Circles:
    def __init__(self, radius, pi):
        assert type(radius) == float and type(pi) == float, "ints not used"
        self.radius = radius
        self.pi = pi

    def __str__(self):
        return f"Cirklens radius = {self.radius} og pi = {self.pi}"


    def getArea(self):
        area = (self.pi * self.radius**2)
        return area

    def getCircumferende(self):
        circumference = 2 * self.pi * self.radius
        return circumference

    def __add__(self, other):
        self_sum = self.getArea()
        other_sum = other.getArea()

        return (self_sum + other_sum)


class Triangles:
    def __init__(self,bredde, hoejde):
        assert type(bredde) == int and type(hoejde) == float, "ints not used"
        self.bredde = bredde
        self.hoejde = hoejde


    def __str__(self):
        return f"Trekantens bredde = {self.bredde} og trekantens hoejde = {self.hoejde}"

    def getArea(self):
        area = (0.5 * self.bredde * self.hoejde)
        return area

    def getCircumferende(self):
        side3 = self.bredde**2 + self.hoejde**2
        side3 = math.sqrt(side3)
        circumference = self.hoejde + self.bredde + side3
        return circumference

    def __add__(self, other):
        self_sum = self.getArea()
        other_sum = other.getArea()

        return (self_sum + other_sum)




a = Squares(4,5)
b = Squares(5,6)

c = Circles(5.0,3.14)
d = Circles(4.0, 3.14)

e = Triangles(5, 4.0)
f = Triangles(4, 2.0)


print(a.__add__(b))
print(c.__add__(d))
print(e.__add__(f))



