
import pyodbc
from prettytable import PrettyTable
import colorama
	
global jobname, jobquery, checkquery


#==========================================#
#			environments presets		   #
#==========================================#

server = 'BR-SRVVMCOPA-01\PROJ2014'
database = 'MSERIES_FOR7E_INT_LE_AT'
username = 'operatorbr'
password = 'access'
tcon = 'yes'
envrnmt_index = 'MSERIES_FOR7E_INT_LE_AT - FOR7E_INT_LEAT - '
jobname = 'FORTE7 File Integration'

#==========================================#

jobquery = "EXEC msdb.dbo.sp_start_job N'{}'".format(envrnmt_index + jobname)


#checkquery = "select top 1 message, instance_id from msdb.dbo.sysjobhistory order by instance_id desc"


# formatted execution message for alerting the user (on console screen)
def message():
	
	print("\n")
	message = PrettyTable(["Executing the job :"])
	message.add_row(["FORTE7 File Integration"])
	print(message)
	print("\n")


# function for executing the SQL query
def executequery(query):

	_query = query

	# start a connection
	connection = pyodbc.connect(driver='{SQL Server}', host=server, database=database, 
	trusted_connection=tcon, user=username, password=password)

	# create a cursor
	mycursor = connection.cursor()

	# send the query to the SQL server
	mycursor.execute(_query)
	
	# print the execution message on screen
	message()

	# closes the SQL cursor
	mycursor.close()
	

'''
def checkifjobhasended(instance_id):

	previous_instance_id = instance_id
	
	mycursor = connection.cursor()
	
	# send the query to the SQL server
	mycursor.execute(checkquery)
	myresult = mycursor.fetchall()
	
	_instance_id = myresult[0][1]

	# if the message does not contains "succeeded", the result is -1
	if ((myresult[0][0]).find('succeeded') != -1): # that is, found the "succeeded" word
		print(colors.BLUE + '\t Job executed with success! \n'.format(_instance_id) + colors.CLEANUP)
	else:
		# that is, the the message does not contains the word "succeeded" return "-1"
		print(colors.RED + '\t Job not yet finished! Please, wait for some seconds. \n' + colors.CLEANUP)
		
	# closes the SQL cursor
	mycursor.close()


# send the query to the SQL server
mycursor.execute(checkquery)

myresult = mycursor.fetchall()
instance_id = myresult[0][1]
'''

executequery(jobquery)


# execute the function for checking if the job has ended
#checkifjobhasended(instance_id)