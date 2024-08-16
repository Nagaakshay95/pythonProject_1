result = max(55,67,999,42361,0000000,-2345)
result2 = min(3,55,67,999,42361,0000000,-2345)

print(result)
print(result2)
print(id(result))
print(id(result2))

name = "Pramod"
name2 = 'Pramod'  # both name & name2 variables pointing to same memory 'Python uses memory effectively'
print(type(name))  # <class 'str'>
print(type(name2))  # <class 'str'>
print(name2)

print(id(name))
print(id(name2))