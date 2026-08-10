d = {} # Empty dictionary

marks ={
    "vishal" : 100,
    "subham" : 56,
    "rohan" : 30
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"vishal" : 99})
print(marks)

print(marks.get("harry2"))# prints none
print(marks["vishal2"])