
import mmap
import re
from   prettytable import PrettyTable


def compileresults():

	_filename = 'stress'
	
	compiledresults = []
		
	with open('logs.txt', 'rb', 0) as file, mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as map:

		# find the point on the file/text which there is the word "basic" or "stress"
		# offset of 50 bytes, encompassing the complete filename
		startpoint = (map.rfind(bytes(_filename, 'utf-8')) - 50)
		
		# put the file pointer on that point
		map.seek(startpoint)
		
		# get the point on the file/text which there is the word "kind of error" for delimitating
		# the endpoint of the piece of the text to be sliced
		endpoint = (map.find(bytes("kind of error", 'utf-8')))
		
		# this is to get the end of the line and not ignore the complete sentence
		map.seek(endpoint)
		map.readline()
		
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
		
		# first, lets remove the map byte (b') and 'return carriage/new line' strings ('\r\n')
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
		
		
		# just insert the file name and the result on the compiledresults's list 
		compiledresults.extend([filename, result])
		
		
		# last - but not least - sanitizing the other elements, taking only results' vales (numbers)
		for each in slice_of_text:
		
			each = [int(s) for s in each.split() if s.isdigit()]
			if not each:
				pass
			else:	
				compiledresults.append(each[0])
				
		compiledresults.append(compiledresults[4] + compiledresults[5])
	
	# mounting and returning a tuple (instead a list) in order to keep each element in order
	# (tuples are more "secure" than lists due its immutability behavior
	return (tuple(compiledresults))
	

def main():


	x = compileresults()
	
	
	print("\n")
	
	print(" "+str(x[0]))
	print("================================")
	print(" File size       : "+ str(x[2]) + " bytes")
	print("\n Number of items : "+ str(x[6]))
	print("\n Elapsed time    : "+ str(x[3]) + " ms")
	print("\n Items generated : "+ str(x[4]))
	print("\n Items with some") 
	print(" kind of error   : "+ str(x[5]))
	print("\n Result          : "+ str(x[1]))
	print("================================")
	
main()