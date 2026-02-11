# typecasting in python

a = "12"
b = "8"
print(a+b) # this will concatenate the two strings and give 128 as output
print(int(a)+int(b)) # this will convert the strings to integers and give 20 as output
d = 3.14
c = 2
print(d+c) # this will give 5.14 as output

string = "15"
numbar = 5
string_numbar = int(string) # throws an error if the string is a not a valid numbar 
sum = string_numbar + numbar
print("the sum of string and numbar is", sum)

