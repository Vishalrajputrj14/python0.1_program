furits = [ "apple" , "orange", 5, 345.65, False, "Aakash", "Rohan" ]
 

print(furits[0])
furits[0] = "grapes" # unlike  strings lists are mutable


print(furits[0])
print(furits[1:4])

print(furits)

furits.append("vishal") # append ka mtlv list me itame jod dena 
print(furits)


li = [1,25,62,5,5,6,442,]
li.sort() # choti se badi  sankhiya
print(li)
li.reverse() # badi se choti sankhiya me bdal deta hai 
print(li)
li.insert(3, 333333)#insert 333333 such that its index in the list is 3
print(li)
li.pop(0)
print(li)
print(li.pop(0))