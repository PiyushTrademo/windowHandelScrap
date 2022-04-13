import errno
import time

from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

from utility.utilityFunct import driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import constValues
from locators import uruguayLocators

driver.implicitly_wait(5)
driver.maximize_window()
driver.implicitly_wait(10)
print(driver.title)
time.sleep(2)
wait = WebDriverWait(driver, 20)
action = ActionChains(driver)

wait.until(EC.element_to_be_clickable(uruguayLocators.startDate))

uruguayLocators.startDate.send_keys(constValues.startDateText)
time.sleep(1)
uruguayLocators.startDate.send_keys(Keys.ENTER)
uruguayLocators.startDate.send_keys(Keys.TAB)
uruguayLocators.endDate.send_keys(constValues.endDateText)
time.sleep(1)
hsconst = constValues.hsCode


def hsCodeListSearch(hs):
    try:
        uruguayLocators.hsCodeInput.clear()
        time.sleep(3)
        uruguayLocators.hsCodeInput.send_keys(hs)
        uruguayLocators.hsCodeInput.send_keys(Keys.TAB)
        time.sleep(4)
        uruguayLocators.confirmButton.click()
        time.sleep(7)
    except Exception as ex:
        print(ex.args)


parentWindow = driver.current_window_handle


def openhscodeInNewWindow():
    duaTable = driver.find_element(By.XPATH, '//table[@class="gx-tab-spacing-fix-2 Grid"]')
    duaListLink = duaTable.find_elements(By.TAG_NAME, 'a')
    print(len(duaListLink))
    for ele in duaListLink:
        action.key_down(Keys.COMMAND).click(ele).key_up(Keys.COMMAND).perform()


hsCodeListSearch(hsconst)


def windowHandle(parentWindow):
    allWindowHandles = driver.window_handles
    size = len(allWindowHandles)
    for x in range(size):
        if allWindowHandles[x] != parentWindow:
            driver.switch_to.window(allWindowHandles[x])
            print(driver.title)
            driver.close()


def getAllDataForHScode():
    nextButton = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//button[@class="PagingButtonsNext"][@title="Siguiente"]')))
    nextlastpage = driver.find_element(By.XPATH, '//button[@title="Ultimo"]')
    next_button_isenabled = nextlastpage.is_enabled()

    if next_button_isenabled:
        openhscodeInNewWindow()
        windowHandle(parentWindow)
        driver.switch_to.window(parentWindow)
        time.sleep(4)
        print(driver.title)
        nextButton = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="PagingButtonsNext"][@title="Siguiente"]')))
        wait.until(EC.element_to_be_clickable(nextButton))
        nextButton.click()
        driver.switch_to.window(parentWindow)
        wait.until(EC.visibility_of(nextlastpage))
        time.sleep(3)
        getAllDataForHScode()


# Elements
nextButton = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="PagingButtonsNext"][@title="Siguiente"]')))
duaTable = driver.find_element(By.XPATH, '//table[@class="gx-tab-spacing-fix-2 Grid"]')
duaListLink = duaTable.find_elements(By.TAG_NAME, 'a')
getAllDataForHScode()

# driver.quit()
