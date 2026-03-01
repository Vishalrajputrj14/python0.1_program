# # while loop

# # for loop 
# for i in  range(5):
#     print(i)
# # while loop
# i = 0
# while i < 5:
#     print(i)
#     i += 1
num = int(input("Enter a number: "))   
i = 1 
while (i <= 11):
    print(f"{i} x {num} = {i*num}")
    i = i + 1

print("Done with loop ")


count = 5
while (count > 0):
    print(count)
    count = count - 1
print("Done with loop")


while True:
    num = int(input("Enter number (0 to stop): "))
    
    if num == 1000:
        break
    
    print("You entered:", num)
