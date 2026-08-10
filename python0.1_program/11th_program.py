#  string are immutable in python
name = "vishal   !!!!!!!!!!!!!!!  vishal"

print(len(name))
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.count("a"))
print(name.rstrip("l") )
print(name.replace("vishal", "sonam"))
print(name.split("  "))
blogheanding = "python is a great programming language"
print(blogheanding.capitalize())
print(name.count("vishalrajput!!!!!!!!!!!!!!!  vishalrajput  "))
str =  " Welcome to the Console !!!"
print(str.endswith("!!!"))

str1 = "He's name is Dan. He is an honest man.  "
print(str1.find("ishh"))
# print(str1.index("ishh"))

str2 = "WelcomeToTheconsole"
print(str2.isalnum())
str3 = "Welcome to the console"
print(str3.isalpha())

str4 = "hello world"
print(str4.islower())
str5 = "HELLO WORLD"
print(str5.isupper())
