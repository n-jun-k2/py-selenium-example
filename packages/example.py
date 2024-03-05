from selenium import webdriver

CHROME_COMMAND_EXECUTOR = "http://selenium:4444/wd/hub"
options = webdriver.ChromeOptions()
driver = webdriver.Remote(options=options, command_executor=CHROME_COMMAND_EXECUTOR)


driver.implicitly_wait(10)