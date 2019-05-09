
x = list(map(str, x))

string = "\n"
string = "\n {x0}"
string = string + "\n ========================================== \n"
string = string + "  File size       : {x2} bytes"
string = string + "\n  Number of items : {x6}"
string = string + "\n  Elapsed time    : {x3} ms"
string = string + "\n  Items generated : {x4}"
string = string + "\n  Items with some"
string = string + "\n  kind of error   : {x5}"
string = string + "\n  Result          : {x1}"
string = string + "\n ========================================== "


string = string.format( x0 = x[0], x1 = x[1], x2 = x[2], x3 = x[3], x4 = x[4], x5 = x[5], x6 = x[6] )    


try:
	with open('results.txt', "w") as data:
		print(string, file=data)
	
except IOError as err:
	print('File error: ' + str(err))

print("\n")
	