letter = "hey my name is {1} and i am from {0}"
country = "India"
name = "vishal"

print(f"hey my name is  {name} and i am from {country}")
print(letter.format(country, name))

txt = "The price of the book is {price} dollars."
print(txt.format(price=258.000000))

print(f"{8  * 5}")


# Docstring in python


def square(n):
    ''' Takes in another n, returns the square of n'''
    print(n ** 2)

square(8)
print(square.__doc__)