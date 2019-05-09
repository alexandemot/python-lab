
import mmap
import re



def test():
	
	filename = ['_basic', '_stress']
	
	x = []
	
	for i in range(2):
		x.append(compileresults(filename[i]))
		
	return x



def compileresults(filename):

	_filename = filename
	
	print(_filename)

	#_filename = 'basic'
	compiled_results = []
	
	
	with open('logs.txt', 'rb', 0) as file, mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as map:
	
		try:

			# find the point on the file/text which there is the word "basic" or "stress"
			# offset of 50 bytes, encompassing the complete filename
			startpoint = (map.rfind(bytes(_filename, 'utf-8')) - 50)
			
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
		filename = " ".join(slice_of_text[0].split()[-1:])
		
		
		# from the line with the results, I just only want the Result itself
		result = " ".join(slice_of_text[4].split()[-1:])
		
		
		# just insert the file name and the result on the compiled_results's list 
		compiled_results.extend([filename, result])
		
		
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
	

def printresultsontxtfile(compiled_results):

	# parsing the var inside the function
	_compiled_results = compiled_results


	# convert all items in the _compiled_results list into characters
	_compiled_results = list(map(str, _compiled_results))


	# prepare the temporary resulting table in a large string
	temp = "\n"
	temp = "\n {filename}\n"
	temp = temp + "  File size       : {filesize} bytes"
	temp = temp + "\n  Number of items : {number_of_items}"
	temp = temp + "\n  Elapsed time    : {elapsed_time} ms"
	temp = temp + "\n  Items generated : {items_generated}"
	temp = temp + "\n  Items with some"
	temp = temp + "\n  kind of error   : {items_with_some_kind_of_error}"
	temp = temp + "\n  Result          : {result}"
	
	
	# populate each line from the temp table with each of the related data
	# obtained from compiled_results
	temp = temp.format( filename = _compiled_results[0], filesize = _compiled_results[2], elapsed_time = _compiled_results[3], items_generated = _compiled_results[4], items_with_some_kind_of_error = _compiled_results[5], number_of_items = _compiled_results[6], result = _compiled_results[1] )
	
	
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
	temp = temp[:slice+1] + "\n " + equals_line + temp[slice+1:]
	temp = temp + "\n " + equals_line
	
	
	# put all into a txt file
	# *** later I am gonna improve it with interface's name, date and time print
	try:
		with open('results.txt', "w") as data:
			print(temp, file=data)
		
	except IOError as err:
		print('File error: ' + str(err))
	


# the main/master function
def main():

	x = test()
	
	for each in x:
		print(each)
		printresultsontxtfile(each)
		
	#printresultsontxtfile(x)
	
	
# executing main()
main()