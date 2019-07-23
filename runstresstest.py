
import os
import sys

import gettheenvironmentinfo as get
import getthefiles
import copythefiles
import executejob
import compiletestresults

import time


def example():
	print('\n\t python test.py <interface name> <environment ID>')


# message if the user forgets to input the interface's name for the searching
if (len(sys.argv)) == 1:
	print('\n\t Please, run again informing an interface name *and* an environment ID!')
	example()
	exit()


# check if the two parameters ("Interface Name" and "Environment ID") had been parsed
elif (len(sys.argv)) == 2:
	print('\n\t Please, run again informing an environment ID!')
	example()
	exit()


# check if *more than two* parameters had been parsed
elif (len(sys.argv)) > 3:
	print('\n\t Please, run again informing *only one* interface name *and only one* environment ID!')
	example()
	exit()


# if all conditions above are correct, proceed
else:

	# first check if if there are files matching the provided interface name
	# and copy them to the user Desktop
	interfacefiles = getthefiles.main()
	
	try:
		environment_info = get.scan(sys.argv[2])
		
		inbox_folder = environment_info[3]
		
		
	except:
		print("\n\t We had some problem (*probably* network connection lost)!")
		
	
	# second, move (copy) that files to the related user (operatorbr) Inbox folder
	files_on_desktop = copythefiles.from_desktop_to_inbox(inbox_folder)


	# third: run the job
	executejob.now(environment_info)

	# better than just wayt for a while, is to watch the logfile status and, as soon as
	# it is free (finished all the job proccess) get the results parameters
	time.sleep(60)

	# last, compile the result(s)
	compiletestresults.main(files_on_desktop)
