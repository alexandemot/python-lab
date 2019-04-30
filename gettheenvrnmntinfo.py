
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'															                    '
'	This module makes a complete search on the standard shared directories      '
,   in order to find the user account information to the user (when called via  '
'	console); if the module is imported inside another pyhon module, the        '
'	information is parsed/returned as a python "tuple"							'
'															         			'
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import os
from   bs4  import BeautifulSoup
import re
import sys
import glob


def scan(envrnmt_id):

	# validating if the parameter provided is empty, like ".scan('')"
	# if is null, it will just return an exception error: TypeError: scan() missing 1 required positional argument
	if (envrnmt_id.strip()) == '':
		print('\n\t Some ID is required for continue. Please, run again with any ID!\n')
		return 

	_envrnmt_id = '_' + envrnmt_id + " - "
	
	# go to the standard repository
	os.chdir(r'\\swntdev2\mSeriesDeploy\Installation\Environments\Active\mSeries')


	# check if there is a directory with the provided ID
	try:
		dir = glob.glob('*{}*'.format(_envrnmt_id))[0]
	# if not, interrupt execution
	except IndexError:
		print('\n\t Not found directory with the ID name provided.')

	try:
		# if there is a directory with the provided ID, enters inside the users directory
		os.chdir(os.path.abspath(dir))
		
		# bring the 'EnvironmentSummary.html' as a beautiful soup instance, please
		with open("EnvironmentSummary.html") as htmlopened:
			soup = BeautifulSoup(htmlopened, features="html.parser")

		# getting the div which contains the information we want
		splitted = soup.find("div", {"class": "style3"}).text.split('- ')

		# getting only the part afer ":" for the fields Database and Server
		database = splitted[1].split(': ')[1]
		server = splitted[2].split(': ')[1]

		# mounting the complete job string for later executions
		completejobname = (soup(text=re.compile('FORTE7 File Integration'))[0].split(': ')[1])
		
		environmentdata = (server, database, completejobname)
		
		return environmentdata
	
	except UnboundLocalError as error:
		# Output expected UnboundLocalErrors.
		print('\n\t Please, run again with your another (correct) ID!')
		
		
def nowplease():

	try:
		# message if the user forgets to input the interface's name for the searching
		if (len(sys.argv)) == 1:
			print('\n\t Please, run again with your environment ID!')
			exit()
		else:	
			envrnmt_id = str(sys.argv[1])
	
		data = scan(envrnmt_id)
		
		# in case of comand via console, we return (print on screen) the data just in time
		if data != None:
			for each in data:
				print(each)
		
	except NameError:
		exit()



if __name__ == '__main__':
	
	nowplease()
