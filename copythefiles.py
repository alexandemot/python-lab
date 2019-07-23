
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'															                    '
'	This module just move (create a copy) the basic and stress files from the	'
'	user Desktop - eventually provided by the getthefiles method/application    '
'	- , to the File Integration Inbox Folder (in order to further run the File 	'
'	Integration Job). In adition, the files are then marked with a timestamp    '
'   in order to track them on the resulting logs (executejob.py step)           '
'																				'
'	In addition, the method does it respecting the order specified for such     '
' 	tests - that is, basic first, followed by stress; it accomplish that, 		'
'	selecting each one of the files by its size (in Bytes), considering that	'
'	- obviously - the basic files tends to be shorter (in size) than the 		'
'	stress ones.																'
'															         			'
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


import datetime
import gettheenvironmentinfo
import os
from   shutil import copy


global desktop, inbox, testfiles


desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

timestamp = (datetime.datetime.now()).strftime("%Y%m%d%H%M%S")



# search/list the txt files - that is, the ones for submitting for testing - which there is on Desktop
def list_txtfiles_ondesktop():
		
	os.chdir(desktop)

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



def rename_files(myfiles):

	myfiles = myfiles.split('_')[0] + '_' + timestamp + '_' + myfiles.split('_')[2]
	return (myfiles)



# just copy the files from the Desktop to the Inbox Folder (basic and stress, respectively)
def copy_fromdesktop_toinbox(myfiles, inbox):

	myfiles = list(myfiles)

	for i in range(len(myfiles)):

		source_file = desktop + '\\' + myfiles[i]

		destiny_file = inbox + '\\' + 	rename_files(myfiles[i])
		print("\t Copying now the file: " + destiny_file.split('Inbox\\')[-1] + '\n')	
		
		copy(source_file, destiny_file)
		print("\n[ Done! ] \n")


def main():

	files_on_desktop = list_txtfiles_ondesktop()

	files_on_desktop = sortfiles_bysize(files_on_desktop)
	
	copy_fromdesktop_toinbox(files_on_desktop, inbox)
	


if __name__ == '__main__':

	# getting the File Inbox folder, from the user and the standard directory
	inbox = gettheenvironmentinfo.nowplease()[3]
	
	main()
	

else:

	inbox = gettheenvironmentinfo.nowplease()[3]	

	def from_desktop_to_inbox(inbox):

		main()
	