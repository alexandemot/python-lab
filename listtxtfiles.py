
import os

os.getcwd()

os.chdir('C:\\Users\\vit.amota\\Desktop')

os.listdir()


for file in os.listdir():
	if file.endswith('.txt'):
		print(file)