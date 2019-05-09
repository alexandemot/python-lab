
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'															                    '
'	This module makes a complete search for files on the default user (local)   '
'	TFS directory, rename them as basic/stress and send a copy of each one		'
'	to the same user/machine Desktop                                            '
'															         			'
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
from shutil import copy
import filecmp as filecomparison
import sys

global interfacename, select_basic_or_stress, source_path, path


# the default local TFS directory
source_path = 'C:\\TFS\\SWProjects\\Unilever - Forte7\\Source Code\\DevBranchs\\Integration\\IntegrationData\\{}\\'

desktop = os.path.join(os.environ["HOMEPATH"], "Desktop")

select_basic_or_stress = [['BasicData','basic'], ['StressData','stress']]

# format the TFS directory name either for BasicData and StressData for later searching/manipulation
listpath = [source_path.format(select_basic_or_stress[0][0]), source_path.format(select_basic_or_stress[1][0])]

originalfiles, desktopfiles = [], []


# this function is executed when called by console
def main():

	try:
		# message if the user forgets to input the interface's name
		if (len(sys.argv)) == 1:
			print('\n\t Please, run again with a interface name!')
		else:	
			interfacename = str(sys.argv[1])
			get_thefiles(interfacename)
		
	except NameError:
		exit()



# check if there is files either on Basic either on StressData directories
def findfiles_with_interfacename(interfacename):
	
	for each in listpath:
	
		os.chdir(each)
		
		files_on_dir = os.listdir()

		for i in range(len(files_on_dir)):
			# if we find a file correspondig to the interface's name, we proceed
			if (files_on_dir[i].startswith(interfacename + '_')) == True:
				originalfiles.append(each + files_on_dir[i])
	
	# if there is no file matching the interface provided, let the user know
	if len(originalfiles) == 0:
		if interfacename == '':
			interfacename = interfacename + '\n'
		print('\n\t Not found files with the interface name: ' + interfacename)
		return (None)
	
	else:
		return originalfiles



# check if basic and stress files has the same size (in bytes)
def checkif_filesare_samesize(originalfiles):

	if originalfiles == None :
		print ('\n\t No files provided!' + '\n')
	# if they has the same size, list only one of them for copying the files to Desktop
	elif (filecomparison.cmp(originalfiles[0], originalfiles[1])) == True:
		originalfiles.remove(originalfiles[0])

	return originalfiles


	
# prepare the files' names for the Desktop and files' manipulation during the tests ("*_basic.txt" or "*_stress.txt")
def rename_desktopfiles(originalfiles):
	
	for each in originalfiles:
		desktopfiles.append(each.replace(os.path.dirname(each), desktop))
	
	for i in range(len(desktopfiles)):
		desktopfiles[i] = desktopfiles[i].replace('.txt', '_'+select_basic_or_stress[i][1]+'.txt')
		
	return desktopfiles
	


# copy the files found on TFS to the user Desktop - with their new names ("*_basic.txt" or "*_stress.txt")
def copythefiles(originalfiles, desktopfiles):

	for i in range(len(originalfiles)):
		copy(originalfiles[i], desktopfiles[i])



# the main function
def get_thefiles(interfacename):

	print('\n\t Searching for an file with the name provided ("{}")...\n'.format(interfacename))

	myfiles = findfiles_with_interfacename(interfacename)
	
	# first: check if the the file(s) exist
	if myfiles == None:
		pass
		
	else:
		# second: check if the the file(s) are of same size (to decide if run or not the comparison
		myfiles = checkif_filesare_samesize(myfiles)
		
		# third: rename the file(s) with "*_basic.txt" or "*_stress.txt" (for convenience)
		myfiles = rename_desktopfiles(myfiles)
		
		# check if already has such files on Desktop
		result = [os.path.exists(each) for each in myfiles]
		
		if result[0] == True:
		
			print("\n\t There is such file(s) on Desktop, already. Bypassing!")
			pass
		
		else:
		
			# fourth: finally, copy/move the files to the Desktop
			copythefiles(originalfiles, desktopfiles)	
		
			# last: notify (let the user know)
			print("\n [ Done! ] Please, check the file(s) in your Desktop.\n \n")
	


if __name__ == '__main__':

	main()