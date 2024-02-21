info = {'name':'Karan', 
        'age':19, 
        98 : "amul",
        'eligible':True}
print(info["name"])
# print(info) 
# print(info.keys())
# print(info.values())

# for key in info.keys():
#   print(f"The value corresponding to the key {key} is {info[key]}")

# print(info.items())
# for key, value in info.items():
#   print(f"The value corresponding to the key {key} is {value}") 
  

  
# I. Accessing single values:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('name'))
print(info.get('eligible'))
print(info['name2'])   # <= error
print(info.get('name2'))  # <= output is None

# II. Accessing multiple values:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())

# III. Accessing keys:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())

# IV. Accessing key-value pairs:
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())