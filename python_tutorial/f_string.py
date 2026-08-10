# staring formatting in python 
'''
string formatting  can be done in python using the format method .


txt = "for only {price: .2f} dollars"
print{txt.format{price = 49}}


f - strings in python 

It is a new string formatting mechanism introduced by the PEP 489. It
is also known as literal string Interpolation or more commonly as
 f - string (f character preceding thestring litera (). 
the primary focus of this machinsm is to make the interpolation easier.

When we prefix the strng with the letter 'f' the string becomes the f-string itself.
 the f - string can be formatted in much same as the 
str.format() method.
 the f-string offers a convenient way to embed python expression inside string literals for formatting.
'''

lettar = "hey my name is {1} and am from {0}"
country = "india"
name = "vishal rajput"

print(lettar.format(country ,name))
print(f"hey my name is {name} and i am from {country}")

txt = "for only{price:.2f} dollars!"
print(txt.format(price = 49.300000))



print(f"{2**3}")