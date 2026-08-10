'''
local and global variables 

Before we dive the differences between  local and global variables, let's first recall what a variable is  in  python 



A variable is a named loction in momory that stores a valuse. In python, we can assign valuse to 
variables using the assignent operator =. for example : 

x = 5 
y = "hello world 


Now, let's talk about local and global variables.

A local variale is a variable that is defined withon a function and is only accessible withinnthatn
function. It is created when the function is called and is destroyed when the funtion returns 


On the other hand, a global variable is a variable that is defined outside of a funtion and is 
accessible from within any function in your code.

'''

x = 4
print(x)


def hello():
    x = 20
    y = 15
    z = x+y
    print(f"The local x is {x}")
    print("hello vishal")
    print(x)


print(f"The global x is {x}")
hello()
print(f"The global x is {x}")


# myfile.txt


# File handling in Python

# Step 1: Open file in write+read mode
with open("myfile.txt", "w+") as f:
    # Step 2: Write content
    f.write("This is test content.")

    # Step 3: Cursor ko start pe le jao
    f.seek(0)

    # Step 4: Read content
    text = f.read()
    print("=== File Content ===")
    print(text)

# Reading existing file content

with open("myfile.txt", "r") as f:
    text = f.read()
    print("=== File Content ===")
    print(text)

# File ka exact path daalo (apna path replace karo)
filepath = r"C:\Users\HP VICTUS\OneDrive\ドキュメント\python prgrams\python_tutorial\myfile.txt"

with open(filepath, "r", encoding="utf-8") as f:
    text = f.read()
    if text.strip() == "":
        print("⚠️ File khaali hai (no content).")
    else:
        print("=== File Content ===")
        print(text)


# Sirf read karna jo myfile.txt me already likha hai
with open("myfile.txt", "r") as f:
    text = f.read()
    print(text)

# Check if file exists and read content
import os

filename = "myfile.txt"

if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
        if text.strip() == "":
            print("⚠️ File khaali hai (no content).")
        else:
            print("=== File Content ===")
            print(text)
else:
    print(f"⚠️ File '{filename}' exist nahi karti.")

