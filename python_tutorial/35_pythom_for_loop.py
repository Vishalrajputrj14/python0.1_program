# python - else in loop
'''
As you have learned before, the else clause is used along with 
the if statement. 
python allow the else keyword to be used with the for and while loops too. 
The statements in the else block will be executed after all iteration are 
copleted . The program exits the loop only after the else block is executed,
'''

for i in range(5):
    print(i)
else:
    print("Sorry no i ")


i = 0
while i < 7 :
    print(i)
    i = i + 1
    if i == 4:
        break
else:
    print("Sorry no I")

# exmple 3 => Prime Number Check


num = int(input("Enter a number: "))

for i in range(2, num):
    if num % i == 0:
        print(num, "is not Prime")
        break
else:
    print(num, "is Prime")

# example 3 => Search in a List


numbars =[10,20,30,40,50,60]
x = int(input("Entar numbar to  search:  "))

for n in numbars:
    if n == x:
        print(x ,"found in list ")
        break
else:
    print(x , " not found in list")

# example 4 => Check if All Numbars are Evan 

nums = int(input("entar check tha numbar for evan and odd "))

for n in range(2,nums):
    if n % 2 != 0:  
        print("List has odd numbar: ", n)
        break
else: 
    print("numbars is even", n)

    
# example 5 => Password Checker (with attempts)

correct  =  "vishal@123"

for i in range(3):
    pwd = input("Entar your passwrd: ")
    if pwd == correct:
        print("Access Granted psw")
        break
else: 
    print("Too many wrong attempts ")


# example 5 => Check Palindrome String 

text = input("Entar string:  ")
length = len(text)

for i in range(length // 2):
    if text[i] != text[length - i - 1]:
        print("Not a palidrome")
        break
else: 
    print("palidrome string")

    # numbar is palidrome

    num = int(input("Enter a number: "))
num_str = str(num)   # number ko string me badal diya
length = len(num_str)

for i in range(length // 2):
    if num_str[i] != num_str[length - i - 1]:
        print(num, "is Not a Palindrome Number")
        break
else:
    print(num, "is a Palindrome Number")


 # example 5 =>  Check Armstrong Number 

num = int(input("Entar number : "))
order = len(str(num))
sum_of_powers = 0

for digit in str(num):
    sum_of_powers += int(digit) ** order
else:
    if sum_of_powers == num:
        print(num, "is an Armstrog number ")
    
    else:
        print(num, "is not an Armstrong number ")

 # example 5 => Check If String Contains Vowels

word = input("Entar a word: ")

for ch in word:
    if ch.lower() in "aeiou":
        print("String has vowel: ", ch)
        break    
else:
        print("No vowels found in string")


 # example 5 =>  Check Perfect Number

num = int(input("Entar number: "))
s = 0

for i in range(1, num):
    if num % i == 0:
        s += i 
else: 
    if s == num:
        print(num, "is a Perfect numbar")
    else:
        print(num, "is not a perfect number")


 # example 5 => 9. Find First Negative Number in List 

nums = [5, 10, -3, 20, 7]

for n in nums:
    if n < 0:
        print("First negative number found:", n)
        break
else:
    print("No negative numbers found")

 # example 5 => Check If Word is in Sentence

sentence = "Python is a powerful programming language"
word = input("Enter word to search: ")

for w in sentence.split():
    if w.lower() == word.lower():
        print("Word found in sentence")
        break
else:
    print("Word not found in sentence")
