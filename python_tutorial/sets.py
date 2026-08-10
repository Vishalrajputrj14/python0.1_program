 # sets ki full from => Set is a collection of well defined objects.
# python sets 

'''
Sets are unordered collection of data items. they
store multipe iitems in single variable. Set items are
separeated by commas and enclosed within curly brackets {}. sets are unchangeable, meaning you 
connot change items of the set once created. sets do not contain diplicate items.

venv bnad karne ke liye deactivate
'''
s = { 2,4,2,98}
print(s)

info = {"Carla",96,False, "vishal", 5.3,96,88,"yogesh"}
print(info)

'''
Here we see that the items of set occur in random 
order and hence they cannot be accessed using index
numbars .Also ests do not allow duplicare values.

Quicl Quiz Try to create an empty set. check using the type() function 
whether the type of your variable is a set 

'''

vishal = {95,88,89,95, "vishal",False,True, "yogesh"}
harry = set()
print(type(vishal))
print(vishal)
print(harry)


for value in vishal:
    print(value)

# Sets class 2 
'''
Sets in python more or less work in the same way as 
sets in mathematics. We can perform operations like 
union and intersection on the sets just like in mathematics.

1. union() and  update():

The union() and update() method prints all items that are present in the
two sets. the union ()method retuns a new set whereas update() method adds item into the exiting set from another set.

'''
s = {1,2,5,6}
s1 = {3,6,9}
print(s.union(s1))
print(s,s1)
s.update(s1)
print(s)

citites = {"bharatpur", "jaipur", "Agra", "delhi"}
citites1 = {"Kota", "jodhpur","bharatpur", "vikaner" "mumbai"}
citites2 = citites.union(citites1)
print(citites2)
for stet in citites2:
    print(stet)
'''
II. intersection and intersection_update():
The intersection() and intersection_update() methods prints only items that are similar to both the sets. The intersection()
 method returns a new set whereas intersection_update() method updates into the existing set from another set.

Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)'''

'''
III. symmetric_difference and symmetric_difference_update():
The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.

Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)
'''

citites1 = {"bharatpur", "jaipur", "Agra", "delhi","kota"}
citites2 = {"Kota", "jodhpur","bharatpur", "vikaner" "mumbai"}
citites3 = citites1.intersection_update(citites2)
print(citites3)

'''
IV. difference() and difference_update():
The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)'''

citites1 = {"bharatpur", "jaipur", "Agra", "delhi","kota"}
citites2 = {"Kota", "jodhpur","bharatpur", "vikaner" ,"mumbai"}
citites3 = citites1.symmetric_difference(citites2)
print(citites3)


'''
uperset():
The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))
Output:
False
False

issubset():
The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))
Output:
True

add()
If you want to add a single item to the set use the add() method.

Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)
Output:
{'Tokyo', 'Helsinki', 'Madrid', 'Berlin', 'Delhi'}

update()
If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.

Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)
Output:
{'Seoul', 'Berlin', 'Delhi', 'Tokyo', 'Warsaw', 'Helsinki', 'Madrid'}

remove()/discard()
We can use remove() and discard() methods to remove items form list.

Example :
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)
Output:
{'Delhi', 'Berlin', 'Madrid'}

The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Seoul")
print(cities)
Output:
KeyError: 'Seoul'

pop()
This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.

Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)
Output:
{'Tokyo', 'Delhi', 'Berlin'} Madrid

del
del is not a method, rather it is a keyword which deletes the set entirely.

Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)
Output:
NameError: name 'cities' is not defined We get an error because our entire set has been deleted and there is no variable called cities which contains a set.

What if we don’t want to delete the entire set, we just want to delete all items within that set?

clear():
This method clears all items in the set and prints an empty set.

Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)
Output:
set()

Check if item exists
You can also check if an item exists in the set or not.

Example
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
Output:
Carla is present.'''

citites1 = {"bharatpur", "jaipur", "Agra", "delhi","kota"}
citites2 = {"Kota", "jodhpur","bharatpur", "vikaner" ,"mumbai"}
print(citites1.isdisjoint(citites2))
 

citites1 = {"bharatpur", "jaipur", "Agra", "delhi","kota"}
citites2 = {"Kota", "jodhpur","bharatpur", "vikaner" ,"mumbai"}
print(citites1.issuperset(citites2))

citites1 = {"bharatpur", "jaipur", "Agra", "delhi","kota"}
citites2 = {"Kota", "jodhpur","bharatpur", "vikaner" ,"mumbai"}
print(citites1.issubset(citites2))


citites1 = {"bharatpur", "jaipur", "Agra", "delhi","kota"}
citites1.add("helsink")
print(citites1)
citites1.remove("bharatpur")

citites1 = {"bharatpur", "jaipur", "Agra", "delhi","kota"}
item =citites1.pop()
print(citites1)
print(item)
''''



32 Day32 - Set Methods

Files
Commands
Search
Packager files
Preview your app here
The app is currently not running.

Run
to see the results of your app.

Set Methods
There are several in-built methods used for the manipulation of set.They are explained below

isdisjoint():
The isdisjoint() method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))
Output:
False

issuperset():
The issuperset() method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))
Output:
False
False

issubset():
The issubset() method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))
Output:
True

add()
If you want to add a single item to the set use the add() method.

Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)
Output:
{'Tokyo', 'Helsinki', 'Madrid', 'Berlin', 'Delhi'}

update()
If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.

Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)
Output:
{'Seoul', 'Berlin', 'Delhi', 'Tokyo', 'Warsaw', 'Helsinki', 'Madrid'}

remove()/discard()
We can use remove() and discard() methods to remove items form list.

Example :
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)
Output:
{'Delhi', 'Berlin', 'Madrid'}

The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Seoul")
print(cities)
Output:
KeyError: 'Seoul'

pop()
This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.

Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)
Output:
{'Tokyo', 'Delhi', 'Berlin'} Madrid

del
del is not a method, rather it is a keyword which deletes the set entirely.

Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)
Output:
NameError: name 'cities' is not defined We get an error because our entire set has been deleted and there is no variable called cities which contains a set.

What if we don’t want to delete the entire set, we just want to delete all items within that set?

clear():
This method clears all items in the set and prints an empty set.

Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)
Output:
set()

Check if item exists
You can also check if an item exists in the set or not.

Example
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
Output:
Carla is present.'''