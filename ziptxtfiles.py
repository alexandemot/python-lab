

import zipfile
import os

os.getcwd()

os.chdir('C:\\Users\\vit.amota\\Desktop')

os.listdir()


for file in os.listdir():
	if file.endswith('.txt'):
		print(file)
		fileunderwork = zipfile.ZipFile(file+'.zip', 'w')
		fileunderwork.write(file, compress_type=zipfile.ZIP_DEFLATED)
		fileunderwork.close()