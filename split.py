from glob import glob
from sklearn.model_selection import train_test_split
import yaml

img_list = glob('/home/aa/dataset/export/images/*.jpg')
txt_list = glob('/home/aa/dataset/export/labels/*.txt')

print(len(img_list))
print(len(txt_list))

train_img_list, val_img_list = train_test_split(img_list, test_size = 0.2, random_state=2000)

print(len(train_img_list), len(val_img_list))

with open('/home/aa/dataset/export/train.txt', 'w') as f :
	f.write('\n'.join(train_img_list) + '\n')

with open('/home/aa/dataset/export/val.txt', 'w') as f :
	f.write('\n'.join(val_img_list) + '\n')

with open('/home/aa/dataset/data.yaml', 'r') as f :
	data = yaml.safe_load(f)

print(data)

data['train'] = '/home/aa/dataset/export/train.txt'
data['val'] = '/home/aa/dataset/export/val.txt'

with open('/home/aa/dataset/data.yaml', 'w') as f :
	yaml.dump(data, f)

print(data)
