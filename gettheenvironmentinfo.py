
import os
from   bs4  import BeautifulSoup
import re
import sys
import glob


# message if the user forgets to input the interaface's name
if (len(sys.argv)) == 1:
	print('\n\t Please, run again with your environment nick name!')
	exit()
else:
	envrnmt_id = '_' + str(sys.argv[1]) + " - "


# supposing that the EnvironmentSummary.html file is on Desktop
#os.chdir('C:\\Users\\vit.amota\\Desktop')

# go to the standard repository
os.chdir(r'\\swntdev2\mSeriesDeploy\Installation\Environments\Active\mSeries')

# check if there is a directory with the provided ID
dir = glob.glob('*{}*'.format(envrnmt_id))[0]

# enters inside the users directory
os.chdir(os.path.abspath(dir))


# bring the 'EnvironmentSummary.html' as a beautiful soup instance
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
