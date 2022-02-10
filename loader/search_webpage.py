import time
from datetime import datetime

import driver as driver
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
driver.get('https://testsheepnz.github.io/BasicCalculator.html')

WebDriverWait(driver, 1).until(expected_conditions.presence_of_element_located((By.ID, "number1Field")))

for i in range(3):
    try:
        if "Display" == driver.find_element_by_id("number1Field"):
            print("Display")
            break
    finally:
        pass
    time.sleep(0.5)
    print("waiting...")

    try:
        if "Display" == driver.find_element_by_id("number1Field"):
            print("Display")
            print("waiting...1")
            break
    finally:
        pass








# browser = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
# browser.get('https://testsheepnz.github.io/BasicCalculator.html')
# delay = 10000  # seconds
# while True:
#     try:
#         # WebDriverWait(browser, timeout=1000, poll_frequency=5000).until(EC.presence_of_element_located((By.ID, 'number1Field')))
#         # WebDriverWait(browser, delay).until(EC.presence_of_element_located(browser.find_element(By.ID, 'number1Field')))
#         # element = WebDriverWait(browser, 1000).until(
#         #     lambda x: x.find_element_by_id("number1Field"))
#         # browser.get('https://testsheepnz.github.io/BasicCalculator.html')
#         # wait = WebDriverWait(browser, 30)  # timeout in seconds -> 30
#         # wait.until(expected_conditions.element_to_be_clickable((By.ID, "number1Field")));
#
#         print("Checking id webpage loaded" + browser.current_url)
#
#         page_state = WebDriverWait(browser, 10000).until(lambda x: x.find_element_by_id('number1Field'))
#         # page_state = browser.execute_script('return document.readyState;')
#         i = 60  # seconds
#         while page_state is not "complete":
#             if i > 60:
#                 break
#             time.sleep(5)
#             i = i + 5
#         print(page_state)  # instead of printing use the variable for other purposes
#
#         # wait = WebDriverWait(browser, 100)
#         # myElem = WebDriverWait(browser, 0).until(EC.visibility_of_element_located((By.ID, 'number1Field')))
#         # wait.until(EC.presence_of_element_located(By.ID, 'number1Field'))
#         print("Page is ready!")
#         break  # it will break from the loop once the specific element will be present.
#     except TimeoutException:
#         print("Loading took too much time!-Try again")



# elem = WebDriverWait(driver, 10000).until(lambda x: x.find_element_by_id('number1Field'))
# elem = WebDriverWait(driver, timeout=1000, poll_frequency=5000).until(EC.presence_of_element_located((By.ID, 'number1Field')))
# print(elem)


# n = 10
# while n > 0:
#     # driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
#     driver.get('https://testsheepnz.github.io/BasicCalculator.html')
#     time.sleep(2)
#     # n -= 1
#     # print("Blasoff")
#
#     try:
#         start = datetime.now()
#         element = WebDriverWait(driver, 5).until(
#             EC.presence_of_element_located((By.ID, 'number1Field'))
#         )
#         end = datetime.now()
#         total_time = end - start
#
#         print("hi: ", element)
#         print("Time: ", start)
#         print("Time: ", end)
#         print("Total time: ", total_time)
#         n -= 1
#     finally:
#         driver.quit()


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
