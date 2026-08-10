f = open("C:/Users/HP VICTUS/OneDrive/ドキュメント/python prgrams/CHAPTER9/vi.txt")

# lines = f.readlines()

# print(lines, type(lines))


line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()