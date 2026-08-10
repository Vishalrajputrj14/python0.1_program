import os 

folders = os.listdir("vishal1")
# print(folders)

print(os.getcwd())
os.chdir("/Users")
print(os.getcwd())



# for folder in folders:   
#     print(folder)
#     print(os.listdir(f"vishal1/{folder}") )