
import os
from shutil import copy
import filecmp as filecomparison
import sys

global interfacename, basicstress_data, source_path, path


if (len(sys.argv)) == 1:
	print('\n\t Please, run again with a interface name!')
	interfacename = 'None'
else:
	interfacename = str(sys.argv[1])
	

source_path = 'C:\\TFS\\SWProjects\\Unilever - Forte7\\Source Code\\DevBranchs\\Integration\\IntegrationData\\{}\\'

desktop_dirname = 'C:\\Users\\vit.amota\\Desktop'

basicstress_data = [['BasicData','basic'], ['StressData','stress']]

listpath = [source_path.format(basicstress_data[0][0]), source_path.format(basicstress_data[1][0])]

originalfiles, desktopfiles = [], []


def findfileswithinterfacename():
	
	for each in listpath:
	
		os.chdir(each)
		
		files_on_dir = os.listdir()

		for i in range(len(files_on_dir)):
			# if we find a file correspondig to the interface's name, we proceed
			if (files_on_dir[i].startswith(interfacename + '_')) == True:
				originalfiles.append(each + files_on_dir[i])
	
	if len(originalfiles) == 0:
		print('\n\t Not found files with the interafece name: ' + interfacename + '\n')
		return (None)
	
	else:
		return originalfiles


def checkifilesaresamesize(originalfiles):

	if originalfiles == None :
		print ('\n\t No files provided!' + '\n')
	
	elif (filecomparison.cmp(originalfiles[0], originalfiles[1])) == True:
		originalfiles.remove(originalfiles[0])

	return originalfiles

	
def renamedesktopfiles(originalfiles):
	
	for each in originalfiles:
		desktopfiles.append(each.replace(os.path.dirname(each), desktop_dirname))
	
	for i in range(len(desktopfiles)):
		desktopfiles[i] = desktopfiles[i].replace('.txt', '_'+basicstress_data[i][1]+'.txt')
		
	return desktopfiles
	
	
def copythefiles(originalfiles, desktopfiles):

	for i in range(len(originalfiles)):
		copy(originalfiles[i], desktopfiles[i])


def main():

	myfiles = findfileswithinterfacename()
	
	if myfiles == None:
		pass
		
	else:
		myfiles = checkifilesaresamesize(myfiles)
		myfiles = renamedesktopfiles(myfiles)
		
		copythefiles(originalfiles, desktopfiles)	
	
main()	
	