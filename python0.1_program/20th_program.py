list = [1, 2, 3, 4, 5, "vishal", "rajput", "python", "programming", "15"]
# print("The list is: ", list)
# print("The length of the list is: ", len(list))
# print(type(list))
# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])
# print(list[4])
if "15"in list:
    print("The student has passed")
else:
    print("The student has failed")  
# Same thing applies for strings as well!
if "vi" in "vishal":
    print("yes")

print(list)
print(list[1:-1])
print(list[1:5])
print(list[1:6:2])

list = [i*i for i in range(6)]
print(list)

names = ["vishal", "rajput", "python", "programming", "15"]
nameswith_0 = [item for item in names if (len(item) > 5)]
print(nameswith_0)