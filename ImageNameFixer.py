import os
import datetime
from PIL import Image

def image_name_fixer(folder_path):
    dirListing = os.listdir(folder_path)

    for file in dirListing:
        file_extension = get_files_extension(file)
        tmp_tim = None
        date = None
        file_name = None
        try :
            print(file)
            image= Image.open("./image/"+file)
        
            image_info = image._getexif()

            tmp_tim = image_info[36867].split()
            print(tmp_tim)
            date = tmp_tim[0].split(':')
            image.close()

            file_name = date[0] + "-" + date[1] + "-" + date[2] 
            
        except Exception:
            create_time = os.path.getctime('./image/'+file)
            create_timestamp = datetime.datetime.fromtimestamp(create_time)
            file_name = datetime.datetime.strftime(create_timestamp, '%Y-%m-%d')
        
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