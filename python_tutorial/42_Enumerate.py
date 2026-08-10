# Enumerate function in python 

'''
the enumerate function isa built - in funtion in python that allows 
you to loop over a sequence (such as a list , tuple, or string ) and get 
the indes and value of each element in the sequence at the same 
time. here's a besi exmaple of how it works:
'''

marks = [ 12,56,62,95,97,12,45,1,2,3]
index = 0

# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("vishal,  awesome!")
#         index += 1


for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
         print("vishal,  awesome!")




