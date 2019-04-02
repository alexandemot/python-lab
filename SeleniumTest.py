


def getTableText():
	tabletext = driver.find_element_by_id("tbRow").text
	return tabletext
	

from selenium import webdriver

from selenium.webdriver.common.keys import Keys


chromedriverlocation = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver'

driver = webdriver.Chrome(chromedriverlocation)
driver.get('https://prjap-03.springwireless.com/FOR7E_INT_AMATIntegrationStudio/Login.aspx?ReturnUrl=%2fFOR7E_INT_AMATIntegrationStudio')


driver.maximize_window()


inputElement = driver.find_element_by_id("Login")
inputElement.send_keys('operatorbr')

inputElement = driver.find_element_by_id("Password")
inputElement.send_keys('access')

inputElement.send_keys(Keys.ENTER)

driver.get('https://prjap-03.springwireless.com/FOR7E_INT_AMATIntegrationStudio/Interface.aspx/TestInterface/440')

a = getTableText()

print(a)


	

'''
inputElement = driver.find_element_by_name("Enter")
inputElement.submit()

assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
'''