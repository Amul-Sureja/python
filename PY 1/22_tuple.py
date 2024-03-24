tup1 = (1)
tup = (1, 2, 76, 342, 32, "green", True)
print(type(tup), tup)
print(type(tup1), tup1) # run = <class 'int'> 1 # solution =>  tup1 = (1, ) run = <class 'tuple'> (1, )
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if  3421 in tup:
  print("Yes 342 is present in this tuple")
tup2 = tup[1:4]
print(tup2)

"""
error =>
tup = (1, 2, 76, 342, 32, "green", True)
tup[0] = 90
"""

"""
run =>
tup = [1, 2, 76, 342, 32, "green", True]
tup[0] = 90
"""

"""
range
Tuple[start : end : jumpIndex]
"""

