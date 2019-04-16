
import pyodbc
from prettytable import PrettyTable
from os import system, name 
    
class colors:
	HEADER    = '\033[95m'
	BLUE      = '\033[94m'
	GREEN     = '\033[92m'
	WARNING   = '\033[93m'
	FAIL 	  = '\033[91m'    
	BOLD 	  = '\033[1m'
	UNDERLINE = '\033[4m'
	CLEANUP	  = '\033[0m'
	
	
server = 'BR-SRVVMCOPA-01\PROJ2014'
database = 'MSERIES_FOR7E_INT_ALE_AT'
username = 'operatorbr'
password = 'access'
tcon = 'yes'


string = 'MSERIES_FOR7E_INT_ALE_AT - FOR7E_INT_ALEAT - '
jobname = 'FORTE7 File Integration'
#jobname = 'Custom Export Process'


query = "EXEC msdb.dbo.sp_start_job N'{}'".format(string+jobname)


connection = pyodbc.connect(driver='{SQL Server}', host=server, database=database, trusted_connection=tcon, user=username, password=password)
connection.execute(query)

'''
# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls')

clear()	
'''

print("\n")
x = PrettyTable(["Executando o job :"])
x.add_row([jobname])
print(x)
print("\n")



# tabela de consulta de status de execução de job
#SELECT * FROM msdb.dbo.sysjobhistory
