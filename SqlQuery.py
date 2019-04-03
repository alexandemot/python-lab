# list the header's name of each colum  of a given Microsoft SQL table

import pyodbc
from prettytable import from_db_cursor


server = 'BR-SRVVMCOPA-01\PROJ2014'
database = 'MSERIES_FOR7E_INT_AM_AT'
username = 'operatorbr'
password = 'access'
tcon = 'yes'


connection = pyodbc.connect(driver='{SQL Server}', host=server, database=database, trusted_connection=tcon, user=username, password=password)

cursor = connection.cursor()

tablename = 'bzAccount'

getcolumns = "select column_name from information_schema.columns where table_name = '{}'".format(tablename)

# list all the columns names from the table
querie = getcolumns

# select only ten first result items
#querie = "select top 10 idAccount, cdAccount from {}".format(tablename)


cursor.execute(querie)

# print the result table on console in a fashionable way
#resulttable = from_db_cursor(cursor)

name = cursor.fetchall()

idAccount = []

for i in range (len(name)):
	idAccount.append(name[i][0])
	
print(idAccount)

# closes the SQL cursor
cursor.close()