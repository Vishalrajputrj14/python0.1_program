s =  {2, 5,2,3,3,5,8,9,9,54}
print(s)

info = {"Carla",19, False,  9.5, 152}
print(info)

harry = set()
print(type(harry))

for value in info:
    print(value)

print("hye ye next line hai")

print(s.union(info))


# Set banaye
cities = {"tokyo", "madrid", "berlin", "delhi"}
cities1 = {"tokyo", "seoul", "kabul", "madrid"}

print("Cities Set:", cities)
print("Cities1 Set:", cities1)

# 1️⃣ Union (dono sets ke sare elements)
cities2 = cities.union(cities1)
print("\nUnion:", cities2)

# 2️⃣ Intersection (common elements)
cities3 = cities.intersection(cities1)
print("Intersection:", cities3)

# 3️⃣ Difference (cities me jo hai par cities1 me nahi)
cities4 = cities.difference(cities1)
print("Difference:", cities4)

# 4️⃣ Symmetric Difference (jo common nahi hai)
cities5 = cities.symmetric_difference(cities1)
print("Symmetric Difference:", cities5)

# 5️⃣ Add element
cities.add("paris")
print("\nAfter Add:", cities)

# 6️⃣ Remove element
cities.remove("delhi")
print("After Remove:", cities)

# 7️⃣ Intersection Update (cities ko update karega)
cities.intersection_update(cities1)
print("After Intersection Update:", cities)