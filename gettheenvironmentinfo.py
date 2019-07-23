
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'															                    '
'	This module makes a complete search on the standard shared directories      '
'   in order to find the user account information to the user (when called via  '
'	console); if the module is imported inside another pyhon module, the        '
'	information is parsed/returned as a python "tuple"							'
'															         			'
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


from   bs4  import BeautifulSoup
import glob
import os
import re
import sys


def scan(envrnmt_id):

	# validating if the parameter provided is empty, like ".scan('')"
	# if is null, it will just return an exception error: TypeError: scan() missing 1 required positional argument
	if (envrnmt_id.strip()) == '':
		print('\n\t Some ID is required for continue. Please, run again with any ID!\n')
		return 

	_envrnmt_id = '_' + envrnmt_id + " - "
	
	# go to the standard repository
	os.chdir(r'\\swntdev2\mSeriesDeploy\Installation\Environments\Active\mSeries')


	# check if there is a directory with the provided ID ...
	try:
		dir = glob.glob('*{}*'.format(_envrnmt_id))[0]
	# if not, interrupt execution
	except IndexError:
		print('\n\t Not found directory with the ID name provided.')

	try:
		
		# if there is a directory with the provided ID, "enter" on that directory
		os.chdir(os.path.abspath(dir))
		
		
		# bring the 'EnvironmentSummary.html' as a beautiful soup instance, please
		with open("EnvironmentSummary.html") as htmlopened:
			soup = BeautifulSoup(htmlopened, features="html.parser")
		
		
		# getting the text contained on the table-td style3
		envrnmtname = soup.find("td", {"class": "style3"}).text.strip().split(' ')
		envrnmtname = envrnmtname[0]

		
		# getting the div which contains only the information we want
		splitted = soup.find("div", {"class": "style3"}).text.split('- ')
		
		
		# getting only the part afer ":" for the fields Database and Server
		# (without its labels)
		database = splitted[1].split(': ')[1]
		server = splitted[2].split(': ')[1]
		
		
		# getting the related (standard) Shared Folder for the Inbox directory ...
		for a in soup.find_all('a', href=True):
			inbox_folder = (a['href'].split('/'))[-1]
			
		# ... and complementing it with the Inbox directory
		inbox_folder = inbox_folder + r"\FileIntegration\Users\operatorbr\Import\Inbox"
		
		
		# mounting the complete job string for later executions
		sql_jobname = (soup(text=re.compile('FORTE7 File Integration'))[0].split(': ')[1])
		
		
		# packaging all the important data in one single tuple (better security)
		environmentdata = (envrnmtname, server, database, inbox_folder, sql_jobname)
		
		return environmentdata
	
	# if not, print an error for the user notification
	except UnboundLocalError as error:
		# Output expected UnboundLocalErrors.
		print('\n\t Please, run again with your another (correct) ID!')



# just get the result tuple and print the data in a user-friendly formatted output
def formattedoutput(string):

	environmentdata = string

	temp = "\n Environment Summary"
	temp = temp + "\n ==============================================="
	temp = temp + "\n  Environment Name    : {envrnmtname} \n"
	temp = temp + "\n  Server              : {server} \n"
	temp = temp + "\n  Database            : {database} \n"
	temp = temp + "\n  Import Inbox Folder : {inbox_folder} \n"
	temp = temp + "\n  SQL Job Name        : {sql_jobname}"
	temp = temp + "\n ==============================================="
	
	print(temp.format(envrnmtname = environmentdata[0], server = environmentdata[1], database =  environmentdata[2], inbox_folder = environmentdata[3], sql_jobname = environmentdata[4]))



def nowplease():

	try:
		# message if the user forgets to input the interface's name for the searching
		if (len(sys.argv)) == 1:
			print('\n\t Please, run again with your environment ID!')
			exit()
		else:	
			envrnmt_id = str(sys.argv[1])
	
		data = scan(envrnmt_id)
		
		# in case of comand via console, we return (print on screen) the
		# data just in time for the user appreciation
		if (__name__ == '__main__') and (data != None):
			formattedoutput(data)

	except NameError:
		exit()

	return data


if __name__ == '__main__':
	
	nowplease()
