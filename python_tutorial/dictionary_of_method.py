# Dictionary Methods
'''
Dictionary uses several built-in method for manipulation.they are listed below

updete() =>  

The upadete() method update the value of the key
provided to it if the item already exists in the dictinory , else it creates a new key-value pair.
'''

ep1 = {
    122 : 45,
    123 : 89,
    152 : 90,
    145 : 75,
    130 : 78
}
ep2 = {
    1220 : 455,
    1230 : 899,
    1520 : 900,
    1450 : 755,
    1300 : 788
}
ep1.update(ep2)

print(ep1)

for key, value in ep1.items():
    print(key, ":", value)


ep22 = {
    1220 : 455,
    1230 : 899,
    1520 : 900,
    1450 : 755,
    1300 : 788
}

ep22.clear()
print(ep22)


ep221 = {
    1220 : 455,
    1230 : 899,
    1520 : 900,
    1450 : 755,
    1300 : 788
}
ep221.pop(1230)
print(ep221)

ep231 = {
    1220 : 455,
    1230 : 899,
    1520 : 900,
    1450 : 755,
    1300 : 788
}
ep231.popitem()
del ep231[1220]
print(ep231)
