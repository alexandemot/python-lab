
import copythefiles
import datetime
from decimal import Decimal
import mmap
import os
from prettytable import PrettyTable
import re



def get_the_logfilename():
	# here, it is necessary (pending) to implement/get the Logs from the user 
	# in running time (EnvironmentSummary.html)	
	os.chdir(r'\\BR-SRVVMCOPA-01\SpringWireless\Project\Shared\FOR7E_INT_ALE\AT\FileIntegration\Users\operatorbr\LogFiles')
	logfilename = os.listdir()[-1]
	return logfilename


def compile_results(testfilename):

	_testfilename = testfilename

	compiled_results = []
	
	logfile = get_the_logfilename()

	print(_testfilename)

	print(logfile)
	
	with open(logfile, 'rb', 0) as file, mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as map:
	
		try:

			# find the point on the file/text which there is the respectively testfilename
			startpoint = map.rfind(bytes(_testfilename, 'utf-8'))
			
			# put the file pointer on that point
			map.seek(startpoint)
			
					
		except ValueError:
			print("\n\t Interface result not found !!! \n")
			exit()

		
		# get the point on the file/text which there is the word "kind of error" for delimitating
		# the endpoint of the piece of the text to be sliced
		endpoint = (map.find(bytes("kind of error", 'utf-8')))
		
		# this is to get the end of the line and not ignore the complete sentence
		map.seek(endpoint)
		map.readline()
		
		# get the actual point
		endpoint = map.tell()

		# defines the range of the slice
		diff = endpoint - startpoint
		
		# returns the file pointer on the previous start
		map.seek(startpoint)
		
		# finally, cut/get the slice of text
		slice_of_text = str(map.read(diff))
		
		# close the map for good
		map.close()
	
		
		'''''''''''''''''''''''''''''''''''''''
		'   sanitizing/formating the data     '
		'''''''''''''''''''''''''''''''''''''''
		
		# first, lets remove the map byte (b') and 'return carriage/new line' temps ('\r\n')
		slice_of_text = slice_of_text.replace("b'", '').replace(r"\r\n", ', ')
		
	
		# second, lets sanitize it a little, eliminating the log time print
		# (we just want the log's text)
		slice_of_text = re.sub('\d\d:\d\d:\d\d \d\d\d - ','', slice_of_text)
		
		
		# finally converting the text in a list (separation defined by the commas)
		slice_of_text = re.split(',', slice_of_text)
		

		# we had some problems with some logs containing the number of records,
		# so that, this line of code, remove elements which contains such text		
		matching = [slice_of_text.remove(s) for s in slice_of_text if "records" in s]
		
		
		# from the first line, I just only want the name of the file itself
		testfilename = " ".join(slice_of_text[0].split()[-1:])
		
		
		# from the line with the results, I just only want the Result itself
		result = " ".join(slice_of_text[4].split()[-1:])
		
		
		# just insert the file name and the result on the compiled_results's list 
		compiled_results.extend([testfilename, result])
		
		
		# last - but not least - sanitizing the other elements, taking only results' vales (numbers)
		for each_line in slice_of_text:
		
			has_digit = [int(s) for s in each_line.split() if s.isdigit()]
			if not has_digit:
				pass
			else:	
				compiled_results.append(has_digit[0])
				
		compiled_results.append(compiled_results[4] + compiled_results[5])
	
	
	# mounting and returning a tuple (instead a list) in order to keep each element in order
	# (tuples are more "secure" than lists due its immutability behavior
	return (tuple(compiled_results))
	

def format_the_results(compiled_results, timestamp):

	# parsing the values inside the function
	_compiled_results = compiled_results
	_timestamp = timestamp


	# convert all items in the _compiled_results list into characters
	_compiled_results = list(map(str, _compiled_results))


	# prepare the temporary resulting table in a large string
	temp = "\n"
	temp = "\n # {testfilename}\n"
	temp = temp + "  File size       : {filesize} bytes"
	temp = temp + "\n  Number of items : {number_of_items}"
	temp = temp + "\n  Elapsed time    : {elapsed_time} ms"
	temp = temp + "\n  Items generated : {items_generated}"
	temp = temp + "\n  Items with some"
	temp = temp + "\n  kind of error   : {items_with_some_kind_of_error}"
	temp = temp + "\n  Result          : {result}"

	
	# populate each line from the temp table with each of the related data
	# obtained from compiled_results
	temp = temp.format( testfilename = _compiled_results[0], filesize = _compiled_results[2], elapsed_time = _compiled_results[3], items_generated = _compiled_results[4], items_with_some_kind_of_error = _compiled_results[5], number_of_items = _compiled_results[6], result = _compiled_results[1] )
	
	
	# create a list, splitting the original text by commas (",") 
	list_from_string_temp = temp.split('\n')
	
	
	# generates one list with the number of strings of each line
	list_of_number_of_strings = [len(s) for s in list_from_string_temp]
	
	
	# sort the values obtained above (in crescent order)
	list_of_number_of_strings.sort()
	
	
	# and select the second - not the first - larger one (the preffered number of "=s")
	number_of_equals = list_of_number_of_strings[-2]
	
	
	# folds the "=s" n times the value obtained just above
	#in order to create a line like "================="
	equals_line = number_of_equals * "="
	
	
	# formatting the final string with the data and "=================s"
	slice = temp.index('.txt') + 3
	temp = temp[ : slice + 1 ] + "\n " + equals_line + temp[ slice + 1 :]
	temp = temp + "\n " + equals_line

	print(temp)
	
	interfacename = _compiled_results[0].split('_')[0]

	results_file = '[results] ' + interfacename + '_' + _timestamp + '.txt'

	# check if there is a file already created
	exists = os.path.isfile(results_file)
	
	if not exists:
		# if the results txt file doesnt exist yet, creates a new one from scratch
		option = 'w'
		print_results_on_txtfile(results_file, option, temp)
	else:
		# else, just insert the data on the previous one
		option = 'a'
		print_results_on_txtfile(results_file, option, temp)

	return results_file


# this function write the results on the txt file
def print_results_on_txtfile(results_file, option, temp):

	
	desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')	
	os.chdir(desktop)

	# put all into a txt file
	try:
		with open(results_file, option) as data:
			print(temp, file=data)
		
	except IOError as err:
		print('File error: ' + str(err))



# this function computates the results and package them in a table
def calculator(calc, timestamp):

	# calculate each result (stress/basic)
	size_ratio  		 = round(Decimal(calc[1][0] / calc[0][0]), 2)
	numberofitems_ratio  = round(Decimal(calc[1][2] / calc[0][2]), 2)
	processingtime_ratio = round(Decimal(calc[1][1] / calc[0][1]), 2)

	# put all on the table
	results_table = PrettyTable()
	results_table.field_names = ["Parameter ratio", "result"]
	results_table.add_row([" size \n"     , size_ratio])
	results_table.add_row([" items \n", numberofitems_ratio])
	results_table.add_row([" processing time", processingtime_ratio])
	# format the results aligned on the left
	results_table.align = "l"

	results_table = 2*('\n') + " # Test Results" + "\n" + str(results_table)

	print(results_table)
	
	return(results_table)



# the main/master function
def main(files_on_desktop):

	_files_on_desktop = files_on_desktop

	calc = []
	
	timestamp = (datetime.datetime.now()).strftime("%Y-%m-%d-%Hh%M")

	
	# if there is a basic and stress file, follow the comparison path
	if len(_files_on_desktop) == 2:

		for each in _files_on_desktop:

			result = compile_results(each)

			file_created = format_the_results(result, timestamp)

			calc.append([result[2], result[3], result[4]])


		results_table = calculator(tuple(calc), timestamp)
		
		print_results_on_txtfile(file_created, 'a', results_table)

		
	
	# if not, it is not necessary (just execute and compile the results obtained on the logs)
	else:
	
		result = compile_results(_files_on_desktop[0])

		file_created = format_the_results(result, timestamp)


		

if __name__ == '__main__':

	files_on_desktop = copythefiles.list_txtfiles_ondesktop()

	main(files_on_desktop)