
import pyodbc
from prettytable import PrettyTable
import os
from shutil import copy
import filecmp as filecomparison

import time
import deterministicaleatorysimulation as deterministic

global interfacename, basicstress_data, source_path, path

#interfacename = 'NonEczieste'
#interfacename = 'ImportPrice'
interfacename = 'ImportVisitInstance'


source_path = 'C:\\TFS\\SWProjects\\Unilever - Forte7\\Source Code\\DevBranchs\\Integration\\IntegrationData\\{}\\'

desktop_dirname = 'C:\\Users\\vit.amota\\Desktop'

basicstress_data = [['BasicData','basic'], ['StressData','stress']]

listpath = [source_path.format(basicstress_data[0][0]), source_path.format(basicstress_data[1][0])]

listfiles, desktop_path = [], []


def findfileswithinterfacename():
	
	for each in listpath:
	
		os.chdir(each)
		
		x = os.listdir()

		for i in range(len(x)):
			# if we find a file correspondig to the interface's name, we proceed
			if (x[i].startswith(interfacename + '_')) == True:
				listfiles.append(each + x[i])
				break
			# if not, we do nothing	
			else:
				pass
	return listfiles


def checkifilesaresamesize(listfiles):
	if (filecomparison.cmp(listfiles[0], listfiles[1])) == True:
		listfiles.remove(listfiles[0])
	else:
		pass
	return listfiles

	
def test(listfiles):

	print(listfiles)
	
	for each in listfiles:
		desktop_path.append(each.replace(os.path.dirname(each), desktop_dirname))
		
	for i in range(len(listfiles)):
		print(desktop_path[i].replace('.txt', '_'+basicstress_data[i][1]+'.txt'))
	
	return desktop_path

def main():

	x = findfileswithinterfacename()
	checkifilesaresamesize(x)
	print(test(x))
	

main()	
	
	
	
