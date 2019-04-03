
from bs4 import *                                              
import requests                                                
import sys

from colorama import Fore, Style

class colors:
	HEADER    = '\033[95m'
	BLUE      = '\033[94m'
	GREEN     = '\033[92m'
	WARNING   = '\033[93m'
	FAIL 	  = '\033[91m'    
	BOLD 	  = '\033[1m'
	UNDERLINE = '\033[4m'
	CLEANUP	  = '\033[0m'

print("\n\tCheck of the status of Github website starting now ...")

try:                                                           
	page = requests.get("https://www.githubstatus.com")         
	pageText = page.text                                        
	renderedpage = BeautifulSoup(pageText, 'html.parser')       
	divstatus = renderedpage.find("div",{"class":"page-status"})
	status = divstatus.get_text()                               
	status = status.strip()                                     

except:
	print(colors.WARNING + "\n\tSomething has gone wrong!" + colors.CLEANUP)
	sys.exit(2)   
	
if status == "All Systems Operational":
	print('\n\t' + colors.GREEN + status + colors.CLEANUP)
	sys.exit(0) 
	
else:
	print("\nI have a bad felling about this!")
	sys.exit(1)  