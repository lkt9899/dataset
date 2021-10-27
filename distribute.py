from glob import glob
import os
import shutil

img_list = glob('/home/aa/dataset/export/*.jpg')
txt_list = glob('/home/aa/dataset/export/*.txt')

print(len(img_list))
print(len(txt_list))

for jpg in img_list :
  shutil.move(jpg, '/home/aa/dataset/export/images')

for txt in txt_list :
  shutil.move(txt, '/home/aa/dataset/export/labels')
