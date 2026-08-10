'''
Write a python program to translate a message into secret code 
language. Use  the rules below to translete normal Emglish into secret code language


Coding :

if the word contains atleast 3 characters, remove the first letter and append it at the end 
now append three random characters, at the starting and the end 
else:
simply reverse the string 


Decofing :

if the word contains less than 3 characters , reverse it 
else:
remove 3 randim characters from start and end . Now remove the last letter and 
'''

# else: 
''' remove 3 random characters from start and end. Now remove the last letter and append  it to
the beginning
'''

'''
last  letter and append it to the beginning 


Your program should ask whether you want to code or decode 

'''
# st  = input("Entar meassge:  ")
# words = st.split(" ")
# coding = input("1 for Coding or decoding ")
# coding = True if (coding == "1") else False

# if(coding):
#     nwords  = []
#     for word in words:
#         if(len(word) >= 3):
#             r1 = "dsf"
#             r2 = "jkr"
#             stnew = word[1:] + word[0] + r2
#             nwords.append(stnew)
#         else:
#             nwords.append(word[::-1])
#     print(" ".join(nwords))

# else:
#     nwords  = []
#     for word in words:
#         if(len(word) >= 6):   # kam se kam dsf + word + jkr
#             stnew = word[3:-3]
#             if stnew:   # empty string check
#                 stnew = stnew[-1] + stnew[:-1]
#                 nwords.append(stnew)
#             else:
#                 nwords.append("")
#         else:
#             nwords.append(word[::-1])
#     print(" ".join(nwords))



import random
import string

st  = input("Entar meassge:  ")
words = st.split(" ")
coding = input("1 for Coding or decoding: ")
coding = True if (coding == "1") else False

# Secret key (sirf tumhe pata hai)
SECRET_KEY = "mysecret"

nwords = []

if coding:   # Encoding
    for word in words:
        if len(word) >= 3:
            # Random prefix aur suffix generate
            prefix = ''.join(random.choices(string.ascii_lowercase, k=3))
            suffix = ''.join(random.choices(string.ascii_lowercase, k=3))
            
            # Word ko shift karo
            stnew = word[1:] + word[0] + SECRET_KEY
            
            # Final encoded word
            nwords.append(prefix + stnew + suffix)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

else:   # Decoding
    for word in words:
        if SECRET_KEY in word:
            # Prefix aur suffix hatao
            start = 3
            end = -3
            stnew = word[start:end]
            
            # Secret key hatana
            stnew = stnew.replace(SECRET_KEY, "")
            
            if stnew:
                stnew = stnew[-1] + stnew[:-1]
                nwords.append(stnew)
            else:
                nwords.append("")
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
