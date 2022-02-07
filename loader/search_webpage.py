import time
from datetime import datetime

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
driver.get('https://testsheepnz.github.io/BasicCalculator.html')


try:
    start = datetime.now()
    element = WebDriverWait(driver, 0).until(
        EC.presence_of_element_located((By.ID, 'number1Field'))
    )
    end = datetime.now()
    total_time = end - start
finally:
    driver.quit()

print("hi: ", element)
print("Time: ", start)
print("Time: ", end)
print("Total time: ", total_time)



# print(driver.execute_script('return document.getElementById("prependExistingHelpBlock = false")'))

# ''''' Test case 1 - The required div-id is not present on the web-page '''''
# # while True:
# try:
#     element_present = EC.presence_of_element_located((By.ID, 'prependExistingHelpBlock'))
#     WebDriverWait(driver, timeout).until(element_present)
#     print("1 - Element is present on the page")
# #        break
# except TimeoutException as ex:
#     print("1 - Timed out waiting for page to load " + str(ex))
# #        break
#
# ''''' Test case 2 - The required div-id is not present on the web-page '''''
# # while True:
# try:
#     element_present = EC.presence_of_element_located((By.ID, 'prependExistingHelpBlock'))
#     WebDriverWait(driver, timeout).until(element_present)
#     print("2 - Element is present on the page")
# #        break
# except TimeoutException as ex:
#     print("2 - Timed out waiting for page to load " + str(ex))
# #        break
#
# ''' Free up the resources'''
# driver.close()
# driver.quit()

# pageLoad Strategy = EAGER, NONE
# https://stackoverflow.com/questions/44770796/how-to-make-selenium-not-wait-till-full-page-load-which-has-a-slow-script

# PageLoad Stopwatch
# https://sqa.stackexchange.com/questions/18853/how-to-measure-client-side-page-load-time

# expected condition = EC
# https://www.selenium.dev/selenium/docs/api/py/_modules/selenium/webdriver/support/expected_conditions.html

# Example Site
# https://testsheepnz.github.io/BasicCalculator.html

# SelectorHub for Xpath

# https://www.youtube.com/watch?v=qP1U_PJIQK0

# Timeout - Page Load Time
# driver.manage().timeouts().pageloadTimeout(3, TimeUnit.SECONDS)
# https://www.youtube.com/watch?v=tXYG5SVlo8k

