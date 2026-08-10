name = "vishal"
frinde = "rahul"
anther_frinde = "sachin"
apple = "he said , \"give me the apple\"eat an apple"
fullname = "vishalrajput"

print("hello,"+ name)
print(apple)

# multiline string
multiline_string = '''hello vishal
how are you
i am fine'''
print(multiline_string)

print(name[0]) # first letter
print(name[1]) # second letter
print(name[4]) # second letter

#print (name[5]) #  throws an error

print("lets use a for loop\n")
for char in name:
    print(char)

    for banana in apple:
        print(banana)

        for chare in fullname :
            print(chare)
            

# string slicing 

print(name[0:3]) # first 3 letter
print(name[1:4]) # 2nd to 4th letter
print(name[:4]) # first 4 letter
print(name[2:]) # from 3rd letter to end 

# string of lenthe funtion
print(len(name))
print(len(apple))
print(len(fullname))







        

