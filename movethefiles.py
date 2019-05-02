
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'															                    '
'	This module just move (create a copy) the basic and stress files from the	'
'	user Desktop - eventually provided by the _getthefiles_ method/application  '
'	-, to the File Integration Inbox Folder (in order to further run the File 	'
'	Integration Job).															'
'																				'
'	In addition, the method does it respecting the order specified for such     '
' 	tests - that is, basic first, followed by stress; it accomplish that, 		'
'	selecting each one of the files by its size (in Bytes), considering that	'
'	- obviously - the basic files tends to be shorter (in size) than the 		'
'	stress ones.																'
'															         			'
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


import os
from   shutil import copy


desktop = os.path.join(os.environ["HOMEPATH"], "Desktop")

inbox = r"//BR-SRVVMCOPA-01/SpringWireless/Project/Shared/FOR7E_MOBL_ALE/Dev/FileIntegration/Users/operatorbr/Import/Inbox"




# search/list the txt files - that is, the ones for submitting for testing - which there is on Desktop
def listtxtfilesondesktop():
	
	os.chdir(desktop)
	
	mydir, myfiles = os.listdir(), []

	[myfiles.append(file) for file in mydir if file.endswith('.txt')] 
	# tuples were chosen for providing fixed positions (doesn't allow modifications as lists does)
	return tuple(myfiles)


# just "organize" the files in order by size (in Bytes) correlated to basic ("lighter") and stress ("heavy")
def sortfilesbysize(myfiles):

	if len(myfiles) == 1:
		pass
	else:
		# here, the checking and the files manipulation/ordenation
		if (os.path.getsize(myfiles[0])) > (os.path.getsize(myfiles[1])):
			myfiles[0], myfiles[1] = myfiles[1], myfiles[0]
	return tuple(myfiles)
	

# just copy the files from the Desktop to the Inbox Folder (basic and stress, respectively)
def copythefilestoInboxFolder(myfiles):

	for each in myfiles:
		source = desktop + '\\' + each
		print("\n\t Moving the file: " + each + '\n')
		copy(source, inbox)
		os.system('cls')
		print("\n\t [ Done! ] \n")
		

def main():

	x = listtxtfilesondesktop()
	x = sortfilesbysize(x)
	copythefilestoInboxFolder(x)


if __name__ == '__main__':

	main()