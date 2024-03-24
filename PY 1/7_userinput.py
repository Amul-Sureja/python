# variable=input()

a = input("enter your name : ")
print("my name is",a,"\n")

x = input("enter first number : ")
y = input("enter secound number : ")

print("before type casting")
print(x + y,"\n")

print("after type casting")
print(int(x) + int(y),"\n")

print(int(x) + int(a))