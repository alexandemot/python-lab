
import subprocess

	
pathToTheExecFile = r'\\BR-SRVVMCOPA-01\Jobs\FOR7E_INT_AM\AT\FileImport\test.exe'

subprocess.call(pathToTheExecFile, shell=True)
#subprocess.Popen(pathToTheExecFile, shell=True)