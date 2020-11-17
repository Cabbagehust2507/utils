import subprocess
import os
import io
import whatimage
import pyheif
import traceback
from PIL import Image
from shutil import copyfile

def decodeImage(bytesIo):
    try:
        fmt = whatimage.identify_image(bytesIo)
        if fmt in ['heic']:
            i = pyheif.read_heif(bytesIo)
            img_data = Image.frombytes(mode=i.mode, size=i.size, data=i.data) 
            # img_data.save('test.jpg', format="jpeg")
    except:
        traceback.print_exc()
    
    return img_data

def read_image_file_rb(file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    return file_data

if __name__ == "__main__":
    new_folder = 'converted_dataset1'
    folder_pth = 'dataset1'
    subfolder_list = os.listdir(folder_pth)
    img_data = None
    for sub in subfolder_list:
        new_sub_pth = os.path.join(new_folder, str(sub))
        sub_pth = os.path.join(folder_pth, str(sub))
        img_in_folder = os.listdir(sub_pth)
        for img in img_in_folder:
            img_pth = os.path.join(sub_pth, str(img))
            new_img_pth = os.path.join(new_sub_pth, str(img))
            if img.find('HEIC') != -1:
                # print(img_pth)
                new_path = new_img_pth.replace('.HEIC', '.jpg')
                data = read_image_file_rb(img_pth)
                img_data = decodeImage(data)
                img_data.save(new_path, format = "jpeg")
                os.remove(new_img_pth)
    
    print("Done!")




