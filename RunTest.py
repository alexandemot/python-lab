
class RunTestClass:

	def openBrowser(datainputed):
	
		_datainputed = datainputed
		
		from selenium import webdriver
		from selenium.webdriver.common.keys import Keys
		
		from selenium.webdriver.chrome.options import Options
		chrome_options.add_experimental_option("detach", True)


		chromedriverlocation = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver'

		driver = webdriver.Chrome(chromedriverlocation)
		driver.get('https://prjap-03.springwireless.com/FOR7E_INT_AMATIntegrationStudio/Login.aspx?ReturnUrl=%2fFOR7E_INT_AMATIntegrationStudio')


		driver.maximize_window()


		inputElement = driver.find_element_by_id("Login")
		inputElement.send_keys('operatorbr')

		inputElement = driver.find_element_by_id("Password")
		inputElement.send_keys('access')

		inputElement.send_keys(Keys.ENTER)

		driver.get('https://prjap-03.springwireless.com/FOR7E_INT_AMATIntegrationStudio/Interface.aspx')
		
		locateInterface(_datainputed)


def locateInterface(data):
	_data = data
	print(_data)
		