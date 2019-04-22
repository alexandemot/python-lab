
import os
from   os import system
from   shutil import copy
import time

global desktop, inbox

os.chdir(r'C:\Users\vit.amota\Desktop')

desktop = os.getcwd() + "\\"

inbox = r"//BR-SRVVMCOPA-01/SpringWireless/Project/Shared/FOR7E_INT_LE/AT/FileIntegration/Users/operatorbr/Import/Inbox"



def listthefiles():
	
	mydir, myfiles = os.listdir(), []

	[myfiles.append(file) for file in mydir if file.endswith('.txt')]

	return myfiles


def sortfilesbysize(myfiles):

	if len(myfiles) == 1:
		pass
	else:
		if (os.path.getsize(myfiles[0])) > (os.path.getsize(myfiles[1])):
			myfiles[0], myfiles[1] = myfiles[1], myfiles[0]
	
	return myfiles
	

def copythefilestoInboxFolder(myfiles):

	for each in myfiles:
		source = desktop + each
		print("\n\t Moving the file: " + each + '\n')
		print(copy(source, inbox))
		os.system('cls')
		print("\n\t [ Done! ] \n")
		

def main():

	x = listthefiles()
	x = sortfilesbysize(x)
	copythefilestoInboxFolder(x)
	
main()