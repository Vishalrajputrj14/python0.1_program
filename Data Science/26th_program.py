dec = {
    "Name" : "vishal rajput",
    "RollNo.": 321001 ,
    "address": "dahi walii gai",

}

print(dec)
print(dec.keys())
print(dec.values())

for keys, value in dec.items():
    print(keys ,":", value)


# Dictionary create
ep1 = {122: 45, 250: 89, 589: 78, 678: 80}
ep2 = {222: 96, 566: 90, 960: 80}

print("Original ep1:", ep1)
print("Original ep2:", ep2)

# 1️⃣ update() → ep2 ko ep1 me add karega
ep1.update(ep2)
print("\nAfter update:", ep1)

# 2️⃣ keys() → sab keys print karega
print("\nKeys:")
for k in ep1.keys():
    print(k)

# 3️⃣ values() → sab values print karega
print("\nValues:")
for v in ep1.values():
    print(v)

# 4️⃣ items() → key + value
print("\nItems:")
for k, v in ep1.items():
    print(k, ":", v)

# 5️⃣ get() → specific key ki value
print("\nGet value of 250:", ep1.get(250))

# 6️⃣ pop() → specific element remove
ep1.pop(250)
print("\nAfter pop(250):", ep1)

# 7️⃣ popitem() → last item remove
ep1.popitem()
print("After popitem():", ep1)

# 8️⃣ setdefault() → agar key nahi hai toh add karega
ep1.setdefault(700, 50)
print("After setdefault:", ep1)

# 9️⃣ copy() → dictionary copy
ep3 = ep1.copy()
print("Copied dictionary:", ep3)

# 🔟 fromkeys() → new dictionary create
keys = (1, 2, 3)
new_dict = dict.fromkeys(keys, 0)
print("Fromkeys dictionary:", new_dict)

# 1️⃣1️⃣ clear() → sab delete
ep1.clear()
print("After clear:", ep1)
