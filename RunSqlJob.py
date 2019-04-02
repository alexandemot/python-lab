
import pyodbc

server = 'BR-SRVVMCOPA-01\PROJ2014'
database = 'MSERIES_FOR7E_INT_AM_AT'
username = 'operatorbr'
password = 'access'
tcon = 'yes'


connection = pyodbc.connect(driver='{SQL Server}', host=server, database=database, trusted_connection=tcon, user=username, password=password)

connection.execute("EXEC msdb.dbo.sp_start_job N'MSERIES_FOR7E_INT_AM_AT - FOR7E_INT_AMAT - FORTE7 File Integration'")