import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from utility.utilityFunct import driver

# Home page elements
try:
    startDate = driver.find_element(By.XPATH, '//input[@id="vVFCHINI"]')
    endDate = driver.find_element(By.CSS_SELECTOR, '#vVFCHFNL')
    hsCodeInput = driver.find_element(By.XPATH, '//input[@id="vPARTIDA"]')
    confirmButton = driver.find_element(By.XPATH, '//input[@id="BUTTON1"]')
    listText = driver.find_element(By.XPATH, '//span[@title="Descripción Aduana"][contains(text(),"Aduana")]')


except NoSuchElementException :
    print("Element not found")


