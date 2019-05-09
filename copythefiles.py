
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
import gettheenvironmentinfo as get

global desktop, inbox


desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')



# search/list the txt files - that is, the ones for submitting for testing - which there is on Desktop
def list_txtfiles_ondesktop():
	
	
	os.chdir(desktop)
	
	print(desktop)
	
	
	mydir, myfiles = os.listdir(), []

	[myfiles.append(file) for file in mydir if file.endswith('.txt')] 
	# tuples were chosen for providing fixed positions (doesn't allow modifications as lists does)
	return tuple(myfiles)


# just "organize" the files in order by size (in Bytes) correlated to basic ("lighter") and stress ("heavy")
def sortfiles_bysize(myfiles):

	if len(myfiles) == 1:
		pass
	else:
		# here, the checking and the files manipulation/ordenation
		if (os.path.getsize(myfiles[0])) > (os.path.getsize(myfiles[1])):
			myfiles[0], myfiles[1] = myfiles[1], myfiles[0]
	return tuple(myfiles)
	

# just copy the files from the Desktop to the Inbox Folder (basic and stress, respectively)
def copy_fromdesktop_toinbox(myfiles, inbox):

	for each in myfiles:
		source = desktop + '\\' + each
		print("\t Copying now the file: " + each + '\n')
		copy(source, inbox)
		print("\n[ Done! ] \n")
		

def main():

	x = list_txtfiles_ondesktop()
	x = sortfiles_bysize(x)
	copy_fromdesktop_toinbox(x, inbox)


if __name__ == '__main__':

	# getting the File Inbox folder, from the user and the standard directory
	inbox = get.nowplease()[3]
	
	main()
	

else:

	def from_desktop_to_inbox(inbox):

		_inbox = inbox

		x = list_txtfiles_ondesktop()
		x = sortfiles_bysize(x)
		copy_fromdesktop_toinbox(x, _inbox)
	