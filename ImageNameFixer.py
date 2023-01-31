import os
from PIL import Image

def image_name_fixer(folder_path):
    dirListing = os.listdir(folder_path)

    for file in dirListing:
        file_extension = get_files_extension(file)

        image= Image.open("./image/"+file)
    
        image_info = image._getexif()

        tmp_tim = image_info[36867].split()
        date = tmp_tim[0].split(':')

        file_name = date[0] + "-" + date[1] + "-" + date[2] 
        
        image.close()
        
        change_file_name(folder_path + '/' +  file,folder_path,file_name,file_extension,0)

def change_file_name(old_file,folder_path,file_name,file_extension,count):
    try:
        if(count == 0):
            os.rename(old_file, folder_path + '/' + file_name + "." + file_extension)
        else:
            os.rename(old_file, folder_path + '/' + file_name + " (" + str(count) + ")." + file_extension)
    except Exception:
        change_file_name(old_file,folder_path,file_name,file_extension,count+1)

def get_files_extension(file_path):
    tmp = file_path.split('.')
    file_extension = tmp[1]

    return file_extension

image_name_fixer("./image")