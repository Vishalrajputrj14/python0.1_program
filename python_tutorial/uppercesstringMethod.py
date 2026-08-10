# string method upper()
# python provide a set of built-in methods that we use to alter  and modify the  strings.
# स्ट्रिंग मेथड upper()
# Python स्ट्रिंग्स को बदलने और संशोधित करने के लिए कई बिल्ट-इन (built-in) मेथड प्रदान करता है।


a = "vishalrajput"
print(len(a))
print(a.upper())

# string method lower()
# स्ट्रिंग मेथड lower()
# Python स्ट्रिंग्स को छोटे अक्षरों (lowercase) में बदलने के लिए lower() मेथड प्रदान करता है।

b = "VISHALRAJPUT"
print(b.lower())
print(b.lower().isupper())

# the rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
# rstrip() मेथड स्ट्रिंग के अंत (trailing) में मौजूद characters को हटाता है।
# डिफ़ॉल्ट रूप से यह खाली स्थान (space) को हटाता है।

c  = "!!!!vishalrajput!!!!"
print(c.rstrip("!"))

# the replace() method replaces a string with another string.
# replace() मेथड एक स्ट्रिंग को दूसरी स्ट्रिंग से बदलता है।
d = "vishal"
print(d.replace("vishal","rahul"))
print(d.replace("vishal","rajput"))

# the split() method splits the given string at the specified instance returns the separated string as a list items.
# split() मेथड निर्दिष्ट instance पर दी गई स्ट्रिंग को विभाजित करता है और अलग-अलग स्ट्रिंग को एक सूची (list) के रूप में लौटाता है।
e = "hello vishal how are you"
print(e.split(" "))
print(a.split("h"))

# capitalize() method
# the capitalize() method turns only the first character of the string  to uppercase and the rest other characters of the string are turned to lowercase. the string has no effect if the first character is already uppercase.
# capitalize() मेथड स्ट्रिंग के केवल पहले अक्षर को बड़े अक्षरों (uppercase) में बदलता है और बाकी सभी अक्षरों को छोटे अक्षरों (lowercase) में बदल देता है। यदि पहले अक्षर पहले से ही बड़े अक्षरों में है, तो इसका कोई प्रभाव नहीं पड़ता है।
blogheading = "introduction to python"
print(blogheading.capitalize())


# center() method
# the center() method will center align the string, using a specified character (space is default) as the fill character.
# center() मेथड
# center() मेथड स्ट्रिंग को बीच (center) में align करता है।
# इसमें आप कोई character specify कर सकते हैं जिसे fill character के रूप में इस्तेमाल किया जाएगा।
# डिफ़ॉल्ट रूप से space लिया जाता है।
txt = "hello vishal"
print(txt.center(20))
print(len(txt.center(20)))
print(len(txt))

# count() method
# the count() method returns the number of times the given value has accurred within the giben string.
# count() मेथड  
# count() मेथड यह बताता है कि कोई दिया गया value (शब्द/अक्षर) 
# किसी स्ट्रिंग में कितनी बार आया है।  


txt1 = "i love python programming and python is my favourite language"
print(txt1.count("python"))

# endswith() method
 # the endswith() method checks if the sting ends with the given value. if yes then return true else return Fales. 
 # endswith() मेथड  
# endswith() मेथड यह चेक करता है कि स्ट्रिंग किसी दिए गए value से समाप्त हो रही है या नहीं।  
# अगर हाँ, तो True return करता है, अन्यथा False return करता है।  


txt2 = "hello vishal"
print(txt2.endswith("vishal"))
print(txt2.endswith("hello"))

# find() method
'''
the find() method searches for the first occurrence of the given value
and returns the index where it is prasent. if given valuse is absent from 
the string then it returns -1.

# find() मेथड  

find() मेथड स्ट्रिंग में दिए गए value को खोजता है और  
उसके पहले occurrence (स्थान) का index number return करता है।  
अगर value स्ट्रिंग में मौजूद नहीं है तो यह -1 return करता है।  
'''

str1 = "he's name is vishal. is an honest ,man he works hard"
print(str1.find("vishal"))
print(str1.find("is"))
print(str1.find("hello"))
# print(str1.index("hello"))

# isalnum() method
'''
the isalnum() method returns true if the intire string only consists if A-Z, a-z, 0-9 characters (alphanumeric characters).
if any other characters or punctuation is present in the string then it returns false.'''
# isalnum() मेथड  
'''
isalnum() मेथड True return करता है अगर पूरी स्ट्रिंग में सिर्फ A-Z, a-z, 0-9  
(alphanumeric characters) ही मौजूद हों।  
अगर स्ट्रिंग में कोई और character या punctuation है, तो यह False return करता है।  
'''
str2 = "helloVishal123"
print(str2.isalnum())

#isalpha() method
'''
the isalpha() method returns true if the intire string only consists of A-Z, a-z characters (alphabetical characters).
if any other characters or punctuation is present in the string then it returns false.
# isalpha() मेथड  

isalpha() मेथड True return करता है अगर पूरी स्ट्रिंग में सिर्फ A-Z या a-z  
(alphabetical characters) ही हों।  
अगर स्ट्रिंग में कोई और character या punctuation मौजूद है,  
तो यह False return करता है।  

'''
str3 = "helloVishal"
print(str3.isalpha())
str4 = "helloVishal123"
print(str4.isalpha())

# islower() method
'''
the islower() method returns true if all the characters of the string are in lower case.
if any character is not in lower case then it returns false.
'''
# islower() मेथड  
'''
islower() मेथड True return करता है अगर स्ट्रिंग के सारे characters छोटे अक्षरों (lowercase) में हों।  
अगर कोई भी character lowercase में नहीं है, तो यह False return करता है।  
'''

str5 = "hello vishal"
print(str5.islower())

str6 = "Hello Vishal"
print(str6.islower())


#isprintable() method
'''
the isprintable() method  returns true if all the values within the given string are printable values.
if any character is not printable then it returns false.
'''
# isprintable() मेथड  
'''
isprintable() मेथड True return करता है अगर स्ट्रिंग के सारे characters प्रिंट करने योग्य (printable) हों।  
अगर स्ट्रिंग में कोई भी ऐसा character है जो printable नहीं है, तो यह False return करता है।  
'''

str7 = "hello vishal\n"
print(str7.isprintable())
str8 = "hello vishal"
print(str8.isprintable())

#isspace() method
'''
the isspace() method returns true if all the characters in the string are whitespaces.
if any character is not a whitespace then it returns false.
'''
# isspace() मेथड  
'''
isspace() मेथड True return करता है अगर स्ट्रिंग के सारे characters सिर्फ whitespace (खाली स्थान) हों।  
अगर स्ट्रिंग में कोई भी character whitespace न हो, तो यह False return करता है।  
'''


str9 = "   "
print(str9.isspace())
str10 = "  hello vishal  "
print(str10.isspace())
str11 = "hello vishal"
print(str11.isspace())

# istitle() method
''' 
the istitle() method returns true only if thr first letter of each word of 
the string  is capitalized. else it returns false.

'''
# istitle() मेथड  
''' 
istitle() मेथड True return करता है अगर स्ट्रिंग के हर शब्द का पहला अक्षर capital (बड़ा) हो।  
अगर किसी शब्द का पहला अक्षर capital न हो, तो यह False return करता है।  
'''
 

str12 = "Hello Vishal"
print(str12.istitle())
str13 = "Hello vishal"
print(str13.istitle())
# isupper() method
'''
the isupper() method returns true if all the characters of the string are in upper case.
if any character is not in upper case then it returns false.
'''
# isupper() मेथड  
'''
isupper() मेथड True return करता है अगर स्ट्रिंग के सारे characters बड़े अक्षरों (UPPERCASE) में हों।  
अगर कोई भी character uppercase में न हो, तो यह False return करता है।  
'''

str14 = "HELLO VISHAL"
print(str14.isupper())
str15 = "Hello VISHAL"
print(str15.isupper())

#startswith() method
'''
the startswith() method checks if the string starts with the given value. if yes then return
true else return Fales. 
'''
# startswith() मेथड  
'''
startswith() मेथड यह चेक करता है कि स्ट्रिंग किसी दिए गए value से शुरू हो रही है या नहीं।  
अगर हाँ, तो यह True return करता है, अन्यथा False return करता है।  
'''

str16 = "hello"
print(str16.startswith("hello"))
str17 = "hello vishal"
print(str17.startswith("vishal"))
# swapcase() method
'''
# the swapcase() method converts all uppercase characters to lowercase and all lowercase characters to uppercase.
'''
# swapcase() मेथड  
'''
swapcase() मेथड स्ट्रिंग के सभी uppercase अक्षरों को lowercase में और  
सभी lowercase अक्षरों को uppercase में बदल देता है।  
'''

str18 = "Hello VISHAL"
print(str18.swapcase())
str19 = "hELLO vishal"
print(str19.swapcase())
str20 = "hello vishal"
print(str20.swapcase())

# title() method
'''
the title() method converts the first character of each word to upper case.
if the first character of a word is already in upper case then it remains unchanged.
'''
# title() मेथड  
'''
title() मेथड स्ट्रिंग के हर शब्द के पहले अक्षर को बड़े अक्षरों (UPPERCASE) में बदल देता है।
अगर किसी शब्द का पहला अक्षर पहले से ही uppercase में है, तो वह अपरिवर्तित रहता है।  
'''

str21 = "hello vishal"
print(str21.title())
str22 = "Hello vishal"
print(str22.title())


