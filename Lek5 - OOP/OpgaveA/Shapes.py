class Squares:
    def __int__(self,side1, side2):
        self.side1 = side1
        self.side2 = side2


    def __str__(self):
        return f"Firkantens side1 = {self.side1} og side2 = {self.side2}"

    def getArea(self):
        pass

    def getCircumferende(self):
        pass


class Circles:
    def __init__(self,radius, pi):
        self.radius = radius
        self.pi = pi

    def __str__(self):
        return f"Cirklens radius = {self.radius} og pi = {self.pi}"


    def getArea(self):
        pass

    def getCircumferende(self):
        pass


class Triangles:
    def __init__(self,bredde, hoejde):
        self.bredde = bredde
        self.hoejde = hoejde


    def __str__(self):
        return f"Trekantens bredde = {self.bredde} og trekantens hoejde = {self.hoejde}"

    def getArea(self):
        pass

    def getCircumferende(self):
        pass
