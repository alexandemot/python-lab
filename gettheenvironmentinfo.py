
import os
from   bs4 	   import BeautifulSoup
from   fnmatch import fnmatch, fnmatchcase
import re

# supposing that the EnvironmentSummary.html file is on Desktop
os.chdir('C:\\Users\\vit.amota\\Desktop')


# bring the html as a beautiful soup instance
with open("EnvironmentSummary.html") as htmlopened:
	soup = BeautifulSoup(htmlopened, features="html.parser")


# getting the div which contains the information we want
splitted = soup.find("div", {"class": "style3"}).text.split('- ')


# getting only the part afer ":" for the fields Database and Server
database = splitted[1].split(': ')[1]
server = splitted[2].split(': ')[1]


# mounting the complete job string for later executions
completejobname = (soup(text=re.compile('FORTE7 File Integration'))[0].split(': ')[1])

print('\n' + database)
print('\n' + server)
print('\n' + completejobname)
