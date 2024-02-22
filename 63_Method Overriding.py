class Shape:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def area(self):
      return self.x * self.y

class Circle(Shape):
    def __init__(self, radius):
      self.radius = radius
      super().__init__(radius, radius)

    def area(self):
        return 3.14 *  super().area()
      
# rec = Shape(3, 5)
# print(rec.area())

c = Circle(5)
print(c.area())

"""
class Shape:
    def area(self):
        pass




class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius




        

        
class Shape:
    def area(self):
        print("Calculating area...")







class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Calculating area of a circle...")
        super().area()
        return 3.14 * self.radius * self.radius

"""