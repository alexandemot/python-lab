
import pyodbc
from prettytable import PrettyTable
from os import system, name



class Parameters:

    server = 'BR-SRVVMCOPA-01\PROJ2014'
    database = 'MSERIES_FOR7E_INT_ALE_AT'
    username = 'operatorbr'
    password = 'access'
    jobname = 'FORTE7 File Integration'

    job = database + ' - FOR7E_INT_ALEAT - ' + jobname

    query = "EXEC msdb.dbo.sp_start_job N'{}'".format(job)


def main():

    connection = pyodbc.connect(driver='{SQL Server}', host=Parameters.server, database=Parameters.database, trusted_connection='yes', user=Parameters.username, password=Parameters.password)
   
    connection.execute(Parameters.query)

    print("\n")
    x = PrettyTable(["Executando o job :"])
    x.add_row([Parameters.jobname])
    print(x)
    print("\n")


if __name__ == "__main__":

    # now execute the job
    main()


else:

    def now(environment_info):
        
        myParameters = Parameters

        myParameters.server = environment_info[1]

        myParameters.database = environment_info[2]

        myParameters.job = environment_info[4]

        main()


