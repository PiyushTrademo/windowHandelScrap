from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from constants import constValues


#Define driver


if constValues.browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(constValues.url)
elif constValues.browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get(constValues.url)
else:
    print('Please enter correct Browser Name ')



