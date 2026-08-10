# python Dictionaries
'''
Dictionaries are ordered collection of data items.
they store multiple items in a single variable. 
Dictionary items are key-value pairs that are separated by commas and 
enclosed within curly brackets{}.
'''

dic = {
    "Name"        : "Vishal rajput",
    "Age"         :  "18",
    "College"     :  "Univsty of tecnolgy",
    "Address"     :  "dahi wali gali bharatpur (raj.)",
    "FatherName"  :  "Kishan singh rajput",
    "MatharName"  :  "Maya Davi",
    "PhoneNo."    :  9694193221,
    "12th Marks"  :   "98.20%",
    "10th Makrs"  :   "88.23%"
}

print(dic["Name"])
# print(dic)

# for key, value in dic.items():
#     print(key, ":", value)


RollNO = {

    1001  :   "vishalrajput",
    1002  :    "yogesh rajput",
    1003  :    "punnet rajput",
    1004  :    "Rudre Sharma",
    1005  :    "uthkarsh sharma",
    1006  :    "harsh sharma",
    1007  :    "anshu sharma"
}
print(RollNO[1006])




dict = {
    "Name"        : "Vishal rajput",
    "Age"         :  "18",
    "College"     :  "Univsty of tecnolgy",
    "Address"     :  "dahi wali gali bharatpur (raj.)",
    "FatherName"  :  "Kishan singh rajput",
    "MatharName"  :  "Maya Davi",
    "PhoneNo."    :  9694193221,
    "12th Marks"  :   "98.20%",
    "10th Makrs"  :   "88.23%"
}

for key in dict.keys():
    print(f"the value carresponding to the key {key} is {dict[key]}")
