import os

folder_path = r"C:\Users\HP\OneDrive\Desktop\hhh\garbage" # this is file path

files = os.listdir(folder_path) # this is files inside folder

file_group = {} # emty dictionary to store the extension of files

for filename in files:
    file_path = os.path.join(folder_path, filename)
    
    if os.path.isfile(file_path):
        _,ext = os.path.splitext(filename) 

        if ext not in file_group:
            file_group[ext] = []
        file_group[ext].append(filename)


# rename files inside each gourp


for ext, file_list in file_group.items():
    for i, filename in enumerate(file_list, start = 1):
        old_path = os.path.join(folder_path, filename)

        new_filename = f"{i}{ext}"

        new_path = os.path.join(folder_path, new_filename)

        os.rename (old_path, new_path)

        print(f"{filename} rename to {new_filename}")
        
