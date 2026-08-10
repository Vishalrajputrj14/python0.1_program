# break statment
for i in range(12):
    print(f"{i} x 21 = {i*2}")
    if(i == 5):
        break

print("Done with loop")


for i in range(12):
    if i == 10:
        print("skip the iteration")
        continue
    print(f"{i} x 21 = {i*5}") 