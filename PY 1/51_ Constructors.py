class Person:

  def __init__(self, name, occ):
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")


a = Person("Harry", "Developer")
b = Person("Divya", "HR") 
# c = Person(1, 2, 3) <== error
a.info()
b.info()
# print(a.name)
# a.name = "Divya"
# a.occ = "HR"
# a.info()


"""
=> Syntax of Python Constructor
def __init__(self):
	# initializations



exampples : 
class Details:
  def __init__(self, animal, group):
      self.animal = animal
      self.group = group

obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")


"""


"""
1] Parameterized Constructor
class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group

obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")



2]Default Constructor
class Details:
  def __init__(self):
    print("animal Crab belongs to Crustaceans group")
obj1=Details()

"""