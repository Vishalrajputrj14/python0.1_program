f = open("C:/Users/HP VICTUS/OneDrive/ドキュメント/python prgrams/CHAPTER9/vi.txt")
print(f.read())
f.close()


# the same can be written using with statement like this: 
with open("C:/Users/HP VICTUS/OneDrive/ドキュメント/python prgrams/CHAPTER9/vi.txt") as f:
    print(f.read())