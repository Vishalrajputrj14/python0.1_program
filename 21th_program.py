tup = (1, 5, 3, 2, 4,342,32,55,"green",True, False)
print(type(tup))
print(tup)

tup1 = (1, 5, 3, 2, 4,"vishal","yogesh", "kalu")
print(type(tup1), tup1)

date_of_birth =( 1, "june", 1998 , "vishal","9694193221","DAHI wali gali bharatpur",
                 2, "March", 1998 , "yogesh","6377003282","jaipur saganer road",
                 3, "April", 1998 , "raam","6975225996", "dehli",
                 4, "May", 1998 , "satyarth", "9694193221", "DAHI wali gali bharatpur")
        # for i in range(0, len(date_of_birth), 4):
        #     print("date of birth of", date_of_birth[i+3], "is", date_of_birth[i], date_of_birth[i+1], date_of_birth[i+2])

for i in range(0, len(date_of_birth), 6):
    print("ID",date_of_birth[i])
    print("month",date_of_birth[i+1])
    print("year",date_of_birth[i+2])
    print("name",date_of_birth[i+3])
    print("phone number",date_of_birth[i+4])
    print("address",date_of_birth[i+5])
    print("..................")
    


    if 342 in tup:
        print("yes 342 is present in this  tup")
    else:
        print("no 342 is not present in this tup")

    tup2 = tup[0:4]
    print(tup2)
countrise = ("India", "Pakistan", "Bangladesh", "Sri Lanka", "Nepal")
temp = list(countrise)
temp.append("Bhutan")   # add item
temp.pop(3)              # remove item
temp[2]= "Russia"        # update item
countrise = tuple(temp)
print(countrise)

tuple1 = (1, 2, 3, 4, 5)
res = tuple1.index(3)
print('Count of 3 in tuple1 is:', res )



