'''
INTRODUCTION TO LOOPS IN PYTHON
Sometimes a programmer wants to execute a group of statememts a ceratain numbar of times. this  can be done  using loops . based on  this loops are further classified into folloeing main  type;
1. for loop
2. while loop

 for loop while loop and nested loop.
nested loops 

THE FOR LOOP

for loop for loops can iterate over a sequence of iterable obkects in python. 
Iterating over a sequesnce is nothing but iterating over string , tuples, sets and dictionries.
The syntax of for loop is as follows:


'''
# example 1

a = "hello"
for i in a:
    print(i)

# example 2
color = ["red", "green", "blue", "yellow"]
for i in color:
     print(i)

# example 3
for i in range(1, 11):
     print(i)

# example 4
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
    print(fruit)    
    for letter in fruit:
        print(letter)

# example 5
for i in range(5):
    print("Outer loop iteration:", i+ 1)

# example 6
for i in range(1, 13 ,2):
    print(i)

# example 7
for i in range(1, 11):   # 1 se 10 tak
    print("2 x", i, "=", 2 * i)
# example 8
for k in range(1, 11):
    print(k*3 )


     


