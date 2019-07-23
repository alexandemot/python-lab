
# list the header's name of each colum  of a given Microsoft SQL table

import pyodbc

server = 'BR-SRVVMCOPA-01\PROJ2014'
database = 'MSERIES_FOR7E_INT_ALE_AT'
username = 'operatorbr'
password = 'access'
tcon = 'yes'


connection = pyodbc.connect(driver='{SQL Server}', host=server, database=database, trusted_connection=tcon, user=username, password=password)

cursor = connection.cursor()

tablename = 'bzAccountXAttribute'

querie = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{}'".format(tablename)

cursor.execute(querie)

name = cursor.fetchall()

colnameslist = []

for i in range (len(name)):
	colnameslist.append(name[i][0])
	
for each in colnameslist:
	print(each)