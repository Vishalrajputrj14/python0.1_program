import os

# Specify the directory path (use '.' for the current directory)
directory_path = "/"

# Get the list of files and directories
contents = os.listdir(directory_path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)