import easyocr
import os

folder_path = '.\\plates'
files = os.listdir(folder_path)
num_files = len(files)

reader = easyocr.Reader(['en'])
count = 0
while (count < num_files):
    result = reader.readtext("plates/scaned_img_" + str(count) + ".jpg")
    for (bbox, text, prob) in result:
        print(text)
    count += 1
    