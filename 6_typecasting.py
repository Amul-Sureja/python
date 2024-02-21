"""
Typecasting in python
The conversion of one data type into the other data type is known as type casting in python or type conversion in python.

Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), 
set(), list(), dict(), etc. for the type casting in python.
"""

#Explicit typecasting

string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)


#implicit type casting

# Python automatically converts
# a to int
a = 7
print(type(a))
# Python automatically converts b to float
b = 3.0
print(type(b))
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))