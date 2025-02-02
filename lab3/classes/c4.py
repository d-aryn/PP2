import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"'X': {self.x}, 'Y': {self.y}\n")
    
    def move(self, nx, ny):
        self.x = nx
        self.y = ny 
        print(f"The points have succesfully changed!\nNew coordinates: 'X': {self.x}, 'Y': {self.y}\n")

    def dist(self, dx, dy):
        print(f"The distance between ({self.x}, {self.y}) and ({dx, dy}) is: {math.sqrt((abs(self.x-dx))**2+abs(self.y-dy)**2)}\n")

points = Point(2, 5)
points.show()
points.dist(9, 15)
points.move(4, 10)
points.show()
points.dist(9, 15)