# def double(x):
#   return x*2

def appl(fx, value):
  return 6 + fx(value)

double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(5))
print(avg(3, 5, 10))
print(appl(lambda x: x * x , 2))
print(appl(cube, 2))


"""
lambda arguments: expression

# Function to double the input
def double(x):
  return x * 2
# Lambda function to double the input
lambda x: x * 2


# Function to calculate the product of two numbers
def multiply(x, y):
    return x * y
# Lambda function to calculate the product of two numbers
lambda x, y: x * y


# Lambda function to calculate the product of two numbers,
# with additional print statement
lambda x, y: print(f'{x} * {y} = {x * y}')

"""