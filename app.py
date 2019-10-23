import os
from shutil import copyfile
dir_p = r'C:\Users\OmarDasser\Desktop\test\test\PNEUMONIA'
dir_b = r'C:\Users\OmarDasser\Desktop\test\bact'
dir_v = r'C:\Users\OmarDasser\Desktop\test\virus'
for img in os.listdir(dir_p):
	if img.split('_')[1] =='bacteria':
		copyfile(dir_p+'/'+img,dir_b+'/'+img)
	else:
		copyfile(dir_p+'/'+img,dir_v+'/'+img)