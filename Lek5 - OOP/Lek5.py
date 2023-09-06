class Coordinate:
    #definer init
    def __init__(self,x ,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "<" +str(self.x) + "," + str(self.y) + ">"

    def distance(self,other):
        x_diff = (self.x - other.x)**2
        y_diff = (self.y - other.y)**2
        return (x_diff + y_diff)**0.5

a = Coordinate(2,4)
b = Coordinate(0,0)

print(Coordinate.distance(a,b))
print(a)

print(a.x)




