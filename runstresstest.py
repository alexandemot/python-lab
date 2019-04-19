
import pyodbc
from prettytable import PrettyTable
import os
from shutil import copy as cp
import filecmp as filecomparison

import time
import deterministicaleatorysimulation as deterministic

global interfacename, option, path

#interfacename = 'NonEczieste'
interfacename = 'ImportPrice'
#interfacename = 'ImportVisitInstance'

option = ['BasicData', 'StressData']

source_path = 'C:\\TFS\\SWProjects\\Unilever - Forte7\\Source Code\\DevBranchs\\Integration\\IntegrationData\\{}\\'

desktop_path = 'C:\\Users\\vit.amota\\Desktop'

path = (source_path, desktop_path)



def findfiles_with_interfacename():
	x = os.listdir()

	for i in range(len(x)):
		# if we find a file correspondig to the interface's name, we proceed
		if (x[i].startswith(interfacename + '_')) == True:
			return x[i]
			break
		# if not, we do nothing	
		else:
			pass



def getlistpaths():

	listpaths = []

	for each in option:
	
		_option = each
		
		print(each)
		
		# tuple "tuple_path" containing the shortcut to BasicData and StressData folder (one at each iteration
		tuple_path = (path[0].format(_option), path[1].format(_option))
		
		os.chdir(tuple_path[0])
		
		original_filename = findfiles_with_interfacename()
		
		if original_filename == None:
			break
		
		
		final_name = tuple_path[0] + original_filename
		
		listpaths.append(final_name)
		
		x = os.path.dirname(final_name)
		
		if _option == "BasicData":
			append = '_basic.txt'
		elif _option == "StressData":
			append = '_stress.txt'
			
		final_name = final_name.replace(x, desktop_path).replace('.txt', append)
		
		listpaths.append(final_name)
	return listpaths



def copyfilestodesktop():

	sourceXdestiny = getlistpaths()
	
	print(sourceXdestiny)
	
	if sourceXdestiny == []:
		print('\n Do nothing!')
	else:	
		for i in range(0,3,2):
			cp(sourceXdestiny[i], sourceXdestiny[i+1])



copyfilestodesktop()


'''	
class colors:
	HEADER    = '\033[95m'
	BLUE      = '\033[94m'
	GREEN     = '\033[92m'
	RED       = '\033[93m'
	FAIL 	  = '\033[91m'    
	BOLD 	  = '\033[1m'
	UNDERLINE = '\033[4m'
	CLEANUP	  = '\033[0m'


server = 'BR-SRVVMCOPA-01\PROJ2014'
database = 'MSERIES_FOR7E_INT_ALEX_AT'
username = 'operatorbr'
password = 'access'
tcon = 'yes'
string = 'MSERIES_FOR7E_INT_ALEX_AT - FOR7E_INT_ALEXAT - '
jobname = 'FORTE7 File Integration'

query = "EXEC msdb.dbo.sp_start_job N'{}'".format(string+jobname)

connection = pyodbc.connect(driver='{SQL Server}', host=server, database=database, trusted_connection=tcon, user=username, password=password)

connection.execute(query)

print("\n")
x = PrettyTable(["Executando o job :"])
x.add_row([jobname])
print(x)

mysim = deterministic.Simulator

def checkstatus(waitingtime, mysim):

	name = 'Dydylan'
	
	sort = mysim.runsimulation()

	while sort == False:
		print(colors.RED + "\n\t // Job is still running. Waiting for {} more seconds.".format(waitingtime) + colors.CLEANUP)		
		time.sleep(waitingtime)
		waitingtime = waitingtime + 1
		sort = mysim.runsimulation()
	print(colors.BLUE + "\n\t // Job executed. Proceeding!" + colors.CLEANUP)	

waitingtime = 1
checkstatus(waitingtime, mysim)

name = 'Ale'
a = sqlquery.Teste
a.printingtest(name)

'''