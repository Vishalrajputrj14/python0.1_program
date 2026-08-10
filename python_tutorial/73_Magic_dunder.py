import os

def clear_clutter(folder_path):
    os.chdir(folder_path)  # Go inside target folder
    files = os.listdir(folder_path)

    extensions = {}  # To track numbering per file type

    for file in files:
        if os.path.isfile(file):  # skip folders
            file_name, ext = os.path.splitext(file)
            ext = ext.lower()

            if ext not in extensions:
                extensions[ext] = 1
            else:
                extensions[ext] += 1

            new_name = f"{extensions[ext]}{ext}"
            os.rename(file, new_name)
            print(f"Renamed: {file} → {new_name}")

    print("\n✅ Folder cleaned successfully!")

# ----------- Example Usage -----------
folder_path = r"C:\Users\HP\Desktop\clutter"  # 👈 Change this to your folder path
clear_clutter(folder_path)






# class shape:
#     def __init__(self,x ,y):
#         self.x = x
#         self.y = y


#     def __area(self):
#         return self.x * self.y
    
# class Circle(shape):
#     def __init__(self, x , y , radius):
#         super().__init__(x , y)
#         self.radius = radius

    
#     def area_circle(self):
#         return 3.14 * self.radius * self.radius

# rec = shape(5,6)
# print(rec._shape__area())
# circle = Circle(0,0,7)
# print(circle.area_circle())