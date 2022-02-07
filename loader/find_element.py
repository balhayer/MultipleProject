from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import chrome
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import ui
from selenium.webdriver.support.wait import WebDriverWait


class js_variable_true(object):
    def __init__(self, variable):
        self.variable = variable

    def __call__(self, driver):
        return driver.execute_script("return {0};".format(self.variable))


def is_visible(locator, timeout=30):
    driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')

    driver.get("https://testsheepnz.github.io/BasicCalculator.html")
    driver.implicitly_wait(5)

    try:
        element = WebDriverWait(chrome, 5).until(js_variable_true("prependExistingHelpBlock.visible"))
    finally:
        chrome.quit()

    try:
        ui.WebDriverWait(chrome, timeout).until(EC.visibility_of_element_located((By.ID, 'prependExistingHelpBlock')))
        return True
    except TimeoutException:
        return False

    print("prependExistingHelpBlock [false]: ", element)
